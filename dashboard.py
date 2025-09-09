# dashboard.py

# =================================================================================================
# SECTION 0: IMPORTING REQUIRED LIBRARIES
# =================================================================================================
# --- Core Libraries ---
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import google.generativeai as genai
import markdown
import io
import base64
import gettext

# --- Import custom utility functions ---
# Assuming these are in a utils/load.py file as per your app.py structure
from utils.load import custom_footer

# =================================================================================================
# SECTION 1: GEMINI API AND MODEL CONFIGURATION
# =================================================================================================
# This section ensures the dashboard module has access to the Gemini model.
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except (KeyError, FileNotFoundError):
    # Display an error if the API key is not configured
    st.error("API Key not found. Please ensure it is set in your Streamlit secrets.")
    st.stop()

def get_gemini_response(input_prompt, image):
    """Sends prompt and image to Gemini and returns the response."""
    try:
        response = model.generate_content([input_prompt, image[0]])
        return response.text
    except Exception as e:
        return f"An error occurred during API call: {e}"

def prepare_image(image_object):
    """Prepares an image file (uploaded or PIL) for the API."""
    if image_object is not None:
        bytes_data = None
        mime_type = None
        if hasattr(image_object, 'getvalue'): # For uploaded files
            bytes_data = image_object.getvalue()
            mime_type = image_object.type
        elif isinstance(image_object, Image.Image): # For local PIL images
            with io.BytesIO() as output:
                image_object.save(output, format="JPEG")
                bytes_data = output.getvalue()
            mime_type = "image/jpeg"
            
        if bytes_data and mime_type:
            return [{"mime_type": mime_type, "data": bytes_data}]
    raise FileNotFoundError("No file or invalid image type provided")

# =================================================================================================
# SECTION 2: UI HELPER FUNCTIONS (FAQ Section)
# =================================================================================================
def FAQSection(_gettext):
    """
    Creates and displays the animated FAQ section, adapted for the driver use case.
    """
    faq_list = [
        {"question": _gettext("What is the purpose of this distracted driver dashboard?"), "answer": _gettext("This dashboard uses AI to analyze images of drivers to detect signs of distraction...")},
        {"question": _gettext("How accurate is the AI-generated analysis?"), "answer": _gettext("The accuracy depends on the image quality...")},
        {"question": _gettext("Are my uploaded images stored permanently?"), "answer": _gettext("No, all uploaded images are processed temporarily...")},
        {"question": _gettext("What image formats are supported for analysis?"), "answer": _gettext("The system supports common image formats such as JPG, JPEG, and PNG...")},
        {"question": _gettext("What types of distractions can this tool detect?"), "answer": _gettext("The tool can identify various distractions like using a mobile phone...")},
        {"question": _gettext("How can I provide feedback or report issues with the dashboard?"), "answer": _gettext("You can provide feedback or report issues through a designated contact channel...")},
    ]

    faq_styles = """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500&family=Poppins:wght@400&display=swap" rel="stylesheet">
    <style>
        .faq-section { padding: 1rem 5vw; }
        .faq-section-title-div { display: flex; justify-content: center; align-items: center; margin-bottom: 1rem;}
        .faq-section-title { padding: 0.5rem 1.5rem; border-radius: 0.5rem; text-align: center; font-family: 'Poppins', sans-serif; font-size: 1.5rem; font-weight: 400; background-color: #799BE6; color: white; }
        .faq-section-questions-list { max-width: 800px; margin: 0 auto; }
        .faq-section-question-split { display: flex; align-items: center; padding: 1rem 0; border-bottom: 1px solid #789BE6; }
        .faq-section-question-answer { font-family: 'DM Sans', sans-serif; flex-grow: 1; }
        .faq-section-question { margin: 0; font-size: 1.25rem; font-weight: 500; color: #789BE6; }
        .faq-section-answer { margin-top: 0.5rem; font-size: 1.1rem; color: #6F6C90; overflow: hidden; transition: max-height 0.3s ease-in-out; }
        .faq-section-question-dropdown { background: transparent; border: none; cursor: pointer; padding: 0.5rem; }
        .faq-section-question-dropdown-img { width: 1.5rem; height: 1.5rem; }
    </style>
    """
    faq_questions_html = ""
    for i, faq in enumerate(faq_list):
        faq_questions_html += f"""<div class="faq-section-question-split">
            <div class="faq-section-question-answer">
                <div class="faq-section-question">{faq['question']}</div>
                <div id="faq-section-answer-{i}" class="faq-section-answer" style="max-height:0px;">{faq['answer']}</div>
            </div>
            <button id="faq-section-question-dropdown-{i}" class="faq-section-question-dropdown">
                <img class="faq-section-question-dropdown-img" alt="toggle" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxZW0iIGhlaWdodD0iMWVtIiB2aWV3Qm94PSIwIDAgMjQgMjQiPjxwYXRoIGZpbGw9ImN1cnJlbnRDb2xvciIgZD0iTTE4IDEyLjk5OGgtNXY1YTEgMSAwIDAgMS0yIDB2LTVINmExIDEgMCAwIDEgMC0yaDV2LTVhMSAxIDAgMCAxIDIgMHY1aDVhMSAxIDAgMCAxIDAgMiIvPjwvc3ZnPg=="/>
            </button>
        </div>"""
    
    faq_section_title = _gettext("Frequently Asked Questions")
    faq_html = f"""
    <div class="faq-section">
        <div class="faq-section-title-div"><div class="faq-section-title">{faq_section_title}</div></div>
        <div class="faq-section-questions-list">{faq_questions_html}</div>
    </div>"""
    
    faq_js = """
    <script>
        const buttons = window.parent.document.querySelectorAll('.faq-section-question-dropdown');
        buttons.forEach((button, index) => {
            button.addEventListener('click', () => {
                const answer = window.parent.document.getElementById(`faq-section-answer-${index}`);
                const img = button.querySelector('img');
                if (answer.style.maxHeight === '0px' || answer.style.maxHeight === '') {
                    answer.style.maxHeight = answer.scrollHeight + 'px';
                    img.src = 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxZW0iIGhlaWdodD0iMWVtIiB2aWV3Qm94PSIwIDAgMjQgMjQiPjxwYXRoIGZpbGw9ImN1cnJlbnRDb2xvciIgZD0iTTE4IDEyLjk5OEg2YTEgMSAwIDAgMSAwLTJoMTJhMSAxIDAgMCAxIDAgMiIvPjwvc3ZnPg==';
                } else {
                    answer.style.maxHeight = '0px';
                    img.src = 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxZW0iIGhlaWdodD0iMWVtIiB2aWV3Qm94PSIwIDAgMjQgMjQiPjxwYXRoIGZpbGw9ImN1cnJlbnRDb2xvciIgZD0iTTE4IDEyLjk5OGgtNXY1YTEgMSAwIDAgMS0yIDB2LTVINmExIDEgMCAwIDEgMC0yaDV2LTVhMSAxIDAgMCAxIDIgMHY1aDVhMSAxIDAgMCAxIDAgMiIvPjwvc3ZnPg==';
                }
            });
        });
    </script>"""
    st.markdown(faq_styles + faq_html, unsafe_allow_html=True)
    components.html(faq_js, height=0, width=0)

# =================================================================================================
# SECTION 3: DEMO DASHBOARD FUNCTION
# =================================================================================================
def demo_dashboard(_gettext):
    """
    Renders the entire content for the 'Demo' tab, including the header,
    two-column layout for samples/uploads and analysis, and the footer/FAQ.
    """
    # --- Demo Page Header with Back Button and Readme Popup ---
    app_title_name = _gettext("Distracted Driver Detection App")
    app_title_tagline = _gettext("AI-powered analysis of driver behavior for enhanced road safety")
    back_button_text = _gettext("Back")
    readme_button_text = _gettext("Readme")
    readme_text = _gettext("""**Welcome to the Distracted Driver Detection App**

Let's begin by exploring the functionality with a sample image or your own by following the instructions below:

1) **Upload an Image** — Utilize the file uploader to provide a clear photograph of a driver. Accepted formats are .jpg, .jpeg, and .png.

2) **Click on 'Analyze Image'** — The system will process the image to identify patterns, driver focus, and possible distractions using the advanced Gemini AI model.

3) **View Driver Insights** — The results will be displayed on the interface, including a classification ('Alert' or 'Distracted') and the specific reasoning for the conclusion.
""")
    readme_html = markdown.markdown(readme_text)

    app_title_styles = """<style>...</style>""" # Omitted for brevity
    app_title_html = f"""<div class="app-title-div">...</div>""" # Omitted for brevity
    app_title_readme_html = f"""<dialog id="readme-dialog" class="readme-dialog"><div class="readme-dialog-text">{readme_html}</div></dialog>"""
    app_title_readme_js = """<script>...</script>""" # Omitted for brevity
    
    st.markdown(app_title_styles + app_title_html + app_title_readme_html, unsafe_allow_html=True)
    components.html(app_title_readme_js, height=0, width=0)

    st.markdown("---")
    
    # --- Main Two-Column Layout for Demo ---
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader(_gettext("Choose an Image"))
        
        # --- Sample Images Section ---
        st.markdown(_gettext("**Try Our Samples**"))
        sample_cols = st.columns(3)
        sample_image_paths = {
            "Sample 1": "ui_assets/images/samples/sample1.jpeg",
            "Sample 2": "ui_assets/images/samples/sample2.jpeg",
            "Sample 3": "ui_assets/images/samples/sample3.jpeg"
        }

        if 'image_to_analyze' not in st.session_state:
            st.session_state.image_to_analyze = None

        for label, path in sample_image_paths.items():
            if sample_cols.pop(0).button(label, key=f"sample_btn_{label}"):
                st.session_state.image_to_analyze = path
                st.session_state.analysis_result = None
                st.rerun()

        # --- User Upload Section ---
        st.markdown(_gettext("**Or Upload Your Own**"))
        uploaded_file = st.file_uploader(" ", type=["jpg", "jpeg", "png"], key="file_uploader")
        
        image_display = None
        if uploaded_file:
            st.session_state.image_to_analyze = uploaded_file
            st.session_state.analysis_result = None
        
        if st.session_state.image_to_analyze:
            try:
                if isinstance(st.session_state.image_to_analyze, str):
                    image_display = Image.open(st.session_state.image_to_analyze)
                else:
                    image_display = Image.open(st.session_state.image_to_analyze)
                
                if image_display:
                    st.image(image_display, caption=_gettext("Image to be Analyzed"), use_container_width=True)
            except Exception as e:
                st.error(f"Could not load image: {e}")

    with col2:
        st.subheader(_gettext("Analysis"))
        if st.button(_gettext("Analyze Image")):
            if st.session_state.image_to_analyze:
                with st.spinner("Analyzing..."):
                    image_for_api = st.session_state.image_to_analyze
                    if isinstance(image_for_api, str): 
                        image_for_api = Image.open(image_for_api)
                    
                    image_data = prepare_image(image_for_api)
                    input_prompt = """
                        You are an expert in driver safety analysis.
                        Analyze the provided image of a driver. Your task is to determine if the driver is distracted or not.
                        Carefully observe the driver's posture, gaze direction, hand positions, and any objects they might be interacting with.
                        Based on your analysis, provide the following:
                        1.  **Classification**: State clearly if the driver is 'Alert' or 'Distracted'.
                        2.  **Reasoning**: Briefly explain your reasoning. List the specific signs of distraction or alertness you observed.
                    """
                    response = get_gemini_response(input_prompt, image_data)
                    st.session_state.analysis_result = response
            else:
                st.warning("Please select a sample or upload an image first.")

        if 'analysis_result' in st.session_state and st.session_state.analysis_result:
            st.markdown(f"""<div style="background-color:#f0f2f6; border-left: 5px solid #799BE6; padding: 1rem; border-radius: 5px; min-height: 300px;">{st.session_state.analysis_result}</div>""", unsafe_allow_html=True)
        else:
            st.info("The analysis will appear here.")
    
    # Display the FAQ and Footer at the bottom of the demo page
    FAQSection(_gettext)
    custom_footer(_gettext)

