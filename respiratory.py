import os
import io
import base64
import json
import pickle
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

import torch
import torchvision.models as models
import torchvision.transforms as transforms

import faiss
import google.generativeai as genai
from dotenv import load_dotenv

import streamlit as st

from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing import image

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from joblib import dump, load

# Allow MKL duplication on some Windows setups (librosa + tf + torch combo)
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# --- LOAD ENVIRONMENT VARIABLES ---
load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("Google API key not found. Please set GOOGLE_API_KEY in your .env file or environment variables.")
genai.configure(api_key=GOOGLE_API_KEY)

# --- CONFIGURATION ---
RETRIEVAL_DB = "data/retrieved_examples"            # folder with reference spectrogram PNGs
LABEL_CSV_PATH = "data/audio_with_labels.csv"       # CSV mapping audio filenames -> labels
FAISS_DIR = "data/faiss"
MODELS_DIR = "data/models"

os.makedirs(FAISS_DIR, exist_ok=True)
os.makedirs(MODELS_DIR, exist_ok=True)

FAISS_INDEX_PATH = os.path.join(FAISS_DIR, "resp_index.faiss")
FAISS_FILENAMES_PATH = os.path.join(FAISS_DIR, "filenames.json")
FAISS_LABELS_PATH = os.path.join(FAISS_DIR, "labels.pkl")

CLASSIFIER_PATH = os.path.join(MODELS_DIR, "resp_clf.joblib")
LABEL_ENCODER_PATH = os.path.join(MODELS_DIR, "label_encoder.pkl")

# Load labels CSV
labels_df = pd.read_csv(LABEL_CSV_PATH)

# --- HELPERS ---
def get_row_by_filename(filename_png: str):
    """
    Map spectrogram PNG filename back to its CSV row.
    The CSV has 'Filename' with .wav; we convert to .png to match.
    """
    row = labels_df[labels_df['Filename'].str.replace('.wav', '.png') == filename_png]
    return row.iloc[0] if not row.empty else None

def audio_to_mel_spectrogram_in_memory(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    S = librosa.feature.melspectrogram(y=y, sr=sr)
    S_DB = librosa.power_to_db(S, ref=np.max)
    plt.figure(figsize=(5, 3))
    librosa.display.specshow(S_DB, sr=sr, x_axis='time', y_axis='mel')
    plt.axis('off')
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
    plt.close()
    buf.seek(0)
    img = Image.open(buf).convert('RGB')
    return img

def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def pil_image_to_base64(pil_img):
    buf = io.BytesIO()
    pil_img.save(buf, format='PNG')
    return base64.b64encode(buf.getvalue()).decode('utf-8')

# --- FEATURE EXTRACTOR (TF-Keras ResNet50 global-average-pooled) ---
resnet50 = ResNet50(weights='imagenet', include_top=False, pooling='avg')

def extract_features_from_pil(pil_image):
    try:
        img = pil_image.resize((224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)
        features = resnet50.predict(img_array, verbose=0)
        return features.flatten()
    except Exception as e:
        print(f"Error extracting features from PIL image: {e}")
        return None

# --- BUILD / LOAD FAISS + CLASSIFIER ---
def build_dataset_from_folder():
    """
    Walk RETRIEVAL_DB for .png files, extract features and labels using labels_df.
    Returns: features (N, D), labels_text (N,), filenames (N,)
    """
    features = []
    labels_text = []
    filenames = []

    png_files = [f for f in os.listdir(RETRIEVAL_DB) if f.lower().endswith(".png")]
    png_files.sort()

    for f in png_files:
        img_path = os.path.join(RETRIEVAL_DB, f)
        try:
            pil_img = Image.open(img_path).convert("RGB")
            vec = extract_features_from_pil(pil_img)
            if vec is None:
                continue
            row = get_row_by_filename(f)
            if row is None or pd.isna(row.get("Diagnosis", None)):
                # skip if no label
                continue
            label = str(row["Diagnosis"]).strip()
            features.append(vec)
            labels_text.append(label)
            filenames.append(f)
        except Exception as e:
            print(f"[WARN] Skipping {f}: {e}")

    if not features:
        raise RuntimeError("No features built from RETRIEVAL_DB. Ensure PNGs exist and labels map properly.")

    X = np.vstack(features).astype('float32')
    y_text = np.array(labels_text)
    fnames = np.array(filenames)
    return X, y_text, fnames

def save_faiss_index(X, filenames, labels_text):
    dim = X.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(X)
    faiss.write_index(index, FAISS_INDEX_PATH)
    with open(FAISS_FILENAMES_PATH, "w") as f:
        json.dump(filenames.tolist(), f)
    with open(FAISS_LABELS_PATH, "wb") as f:
        pickle.dump(labels_text, f)
    print(f"[INFO] Saved FAISS index with {index.ntotal} vectors.")

def load_faiss_index():
    if not (os.path.exists(FAISS_INDEX_PATH) and os.path.exists(FAISS_FILENAMES_PATH) and os.path.exists(FAISS_LABELS_PATH)):
        return None, None, None
    index = faiss.read_index(FAISS_INDEX_PATH)
    with open(FAISS_FILENAMES_PATH, "r") as f:
        filenames = np.array(json.load(f))
    with open(FAISS_LABELS_PATH, "rb") as f:
        labels_text = np.array(pickle.load(f))
    print(f"[INFO] Loaded FAISS index with {index.ntotal} vectors.")
    return index, filenames, labels_text

def train_and_save_classifier(X, y_text):
    le = LabelEncoder()
    y = le.fit_transform(y_text)
    clf = LogisticRegression(max_iter=500, n_jobs=None)
    clf.fit(X, y)
    dump(clf, CLASSIFIER_PATH)
    with open(LABEL_ENCODER_PATH, "wb") as f:
        pickle.dump(le, f)
    print("[INFO] Trained and saved classifier + label encoder.")

def load_classifier():
    if not (os.path.exists(CLASSIFIER_PATH) and os.path.exists(LABEL_ENCODER_PATH)):
        return None, None
    clf = load(CLASSIFIER_PATH)
    with open(LABEL_ENCODER_PATH, "rb") as f:
        le = pickle.load(f)
    return clf, le

# Global holders
faiss_index, faiss_filenames, faiss_labels_text = load_faiss_index()
clf, le = load_classifier()

if faiss_index is None or clf is None:
    print("[INFO] Building dataset, FAISS index, and classifier (first run)...")
    X_all, y_text_all, fnames_all = build_dataset_from_folder()
    save_faiss_index(X_all, fnames_all, y_text_all)
    train_and_save_classifier(X_all, y_text_all)
    # Reload to globals
    faiss_index, faiss_filenames, faiss_labels_text = load_faiss_index()
    clf, le = load_classifier()

# --- RETRIEVAL ---
def retrieve_similar_spectrograms(query_audio_path, n=2):
    if faiss_index is None or faiss_filenames is None:
        print("[ERROR] FAISS index or filenames not available.")
        return []
    try:
        query_spectrogram_pil = audio_to_mel_spectrogram_in_memory(query_audio_path)
        query_features = extract_features_from_pil(query_spectrogram_pil)
    except Exception as e:
        print(f"[ERROR] Retrieval failed: {e}")
        return []
    if query_features is None:
        return []
    q = np.array([query_features]).astype('float32')
    distances, indices = faiss_index.search(q, min(n, faiss_index.ntotal))
    return [faiss_filenames[i] for i in indices[0]]

# --- PROMPT BUILDING (LLM for explanation only) ---
def build_prompt(retrieved_files, query_image_b64, predicted_label):
    prompt = []

    # Provide a couple of labeled exemplars as context (optional, small)
    for f in retrieved_files:
        image_path = os.path.join(RETRIEVAL_DB, f)
        row = get_row_by_filename(f)
        diagnosis_text = (
            f"This spectrogram is from a patient diagnosed with **{row['Diagnosis']}**, "
            f"recorded at chest location: {row['Chest_Location']}."
            if row is not None else f"Spectrogram file {f} without matching label metadata."
        )
        prompt.append({"inline_data": {"mime_type": "image/png", "data": image_to_base64(image_path)}})
        prompt.append({"text": diagnosis_text})

    # Main query + strict instructions: model must NOT change the predicted label
    query_text = (
        "Analyze the following spectrogram and produce a patient-friendly explanation.\n"
        f"The predicted diagnosis (do not change this label): **{predicted_label}**.\n\n"
        "When explaining, you may mention signal aspects (e.g., 'low frequencies', 'high-pitched', 'irregular bursts'), "
        "but translate them to real-world respiratory effects (e.g., wheezing, airway narrowing, chest congestion, "
        "coughing, shortness of breath, fluid/infection signs). Do not compare with the above examples explicitly.\n\n"
        "**TASK**: Provide only the following fields:\n"
        "Reason: <connect spectrogram cues (like low/high frequencies, irregularity) to symptoms in simple terms>\n"
        "Precautions: <2–4 practical steps a patient can take>\n\n"
        "Keep it concise, clear, and non-technical.\n"
        "Do not restate the diagnosis; it is already provided."
    )

    prompt.append({"inline_data": {"mime_type": "image/png", "data": query_image_b64}})
    prompt.append({"text": query_text})
    return prompt

# --- GEMINI CALL ---
def call_gemini_vision_model(prompt_content):
    try:
        gemini_model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = gemini_model.generate_content(prompt_content)
        if hasattr(response, 'text'):
            return {"choices": [{"message": {"content": response.text}}]}
        else:
            return {"choices": []}
    except Exception as e:
        print(f"[ERROR] Error calling Gemini API: {e}")
        return {"choices": []}

# --- INFERENCE PIPELINE ---
def process_audio_diagnosis(audio_file_name):
    """
    Returns a formatted string:
    'Diagnosis: <label>\\nReason: ...\\nPrecautions: ...'
    """
    base_file_name = os.path.basename(audio_file_name)
    audio_path = audio_file_name
    print(f"[INFO] Processing file: {audio_file_name}")

    # 1) Make query spectrogram
    query_spectrogram_pil = audio_to_mel_spectrogram_in_memory(audio_path)
    query_image_b64 = pil_image_to_base64(query_spectrogram_pil)

    # 2) Extract features
    query_features = extract_features_from_pil(query_spectrogram_pil)
    if query_features is None:
        return "Error: could not extract features from audio."

    # 3) Predict label via trained classifier
    if clf is None or le is None:
        return "Error: classifier not available."
    pred_idx = clf.predict([query_features])[0]
    predicted_label = le.inverse_transform([pred_idx])[0]
    print(f"[INFO] Predicted label: {predicted_label}")

    # 4) Retrieve a couple of similar examples (optional, for gentle context)
    retrieved = retrieve_similar_spectrograms(audio_path, n=2)
    print(f"[INFO] Retrieved examples: {retrieved}")

    # 5) Ask Gemini to generate Reason + Precautions ONLY (label is fixed)
    full_prompt = build_prompt(retrieved, query_image_b64, predicted_label)
    print("[INFO] Prompt constructed.")

    response = call_gemini_vision_model(full_prompt)
    print("[INFO] Response received from LLM API.")

    try:
        explanation = response["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError):
        explanation = "Reason: Unable to generate explanation.\nPrecautions: Consult a physician; avoid irritants; follow medications."

    # 6) Compose final output (we control the Diagnosis line)
    output = f"Diagnosis: {predicted_label}\n{explanation}"
    print(output)
    return output
