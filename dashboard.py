import os
import streamlit as st
from respiratory import process_audio_diagnosis 

# Folder containing available respiratory audio files
AUDIO_DIR = "temp_audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

def _clear_state():
    for k in ["selected_audio_path", "diagnosis_result"]:
        st.session_state[k] = None

def demo_dashboard(_gettext):

    if st.button("⬅️ Back", key="back_top"):
        st.session_state["show_dashboard"] = False
        st.rerun()

    st.session_state.setdefault("selected_audio_path", None)
    st.session_state.setdefault("diagnosis_result", None)

    left, right = st.columns([4, 5])

    with left:
        st.subheader("Select Audio File")

        # List available audio files
        audio_files = [f for f in os.listdir(AUDIO_DIR) if f.lower().endswith((".wav", ".mp3"))]

        if not audio_files:
            st.warning("No audio files found in the directory.")
        else:
            selected_file = st.selectbox("Choose an audio file:", audio_files)
            if selected_file:
                st.session_state.selected_audio_path = os.path.join(AUDIO_DIR, selected_file)
                st.session_state.diagnosis_result = None
                st.audio(st.session_state.selected_audio_path, format="audio/wav")

    with right:
        st.subheader("Analysis")
        cols = st.columns([1, 1])
        with cols[0]:
            run_disabled = not st.session_state.selected_audio_path
            run = st.button("Run Diagnosis", disabled=run_disabled)
        with cols[1]:
            clear = st.button("Clear")
        if clear:
            _clear_state()

        if run and not run_disabled:
            with st.spinner("Processing audio and generating diagnosis..."):
                try:
                    diagnosis = process_audio_diagnosis(st.session_state.selected_audio_path)

                    if not diagnosis or diagnosis.strip() == "":
                        diagnosis = (
                            "No exact match found. "
                            "Based on the audio, the respiratory condition could not be determined precisely."
                        )

                    st.session_state.diagnosis_result = diagnosis
                except Exception as e:
                    st.error(f"Error processing file: {e}")

        
        if st.session_state.diagnosis_result:
            with st.container(border=True):
                st.subheader("Diagnosis Result")
                st.write(st.session_state.diagnosis_result)


if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Respiratory Disease Detection")
    demo_dashboard()