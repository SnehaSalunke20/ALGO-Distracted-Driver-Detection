import base64
import streamlit as st
from utils.load import custom_footer
from utils.load import apply_custom_style

# Function to convert image to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def homepage_v3(_gettext):
    apply_custom_style()
    # Styling for the 'Try Demo' button
    button_style = """
    <style>
    div.stButton > button:first-child {
        display: inline-block;
        padding: 10px 20px;
        margin: 10px 0;
        border-radius: 25px;
        background-color: #0a4e8d;
        color: white;
        border: none;
        cursor: pointer;
        font-size: 18px;
        transition: background-color 0.3s, box-shadow 0.3s;
    }
    div.stButton > button:first-child:hover {
        background-color: #00008b;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    }
    @media (max-width: 768px) {
        div.stButton > button:first-child {
            padding: 8px 15px;
            font-size: 16px;
        }
    }
    @media (max-width: 480px) {
        div.stButton > button:first-child {
            padding: 6px 12px;
            font-size: 14px;
            width: 80%;
            margin: 10px auto;
            display: block;
        }
    }
    </style>
    """
    
    st.markdown(button_style, unsafe_allow_html=True)

    # Display Header
    h1_text = "Respiratory Disease Detection Dashboard"
    h2_text = "AI-powered analysis of respiratory sounds for faster, smarter health insights"

    st.markdown(f"""
    <div style="text-align: center;">
        <h1 style="font-weight: 600; color: #0a4e8d; text-shadow: 0px 2px 4px rgba(0,0,0,0.2);">{h1_text}</h1>
        <h2 style="font-weight: 300; color: #555;">{h2_text}</h2>
    </div>
    """, unsafe_allow_html=True)

    # Columns for Try Demo button
    left_col, button_col, right_col = st.columns([4, 1, 4])
    with button_col:
        st.button("Try Demo", key='demo_button')

    # Load feature images
    image1_base64 = image_to_base64("ui_assets/images/respiratory_1.jpg")
    image2_base64 = image_to_base64("ui_assets/images/respiratory_2.jpg")
    image3_base64 = image_to_base64("ui_assets/images/respiratory_4.jpg")

    # Feature details
    feature1_heading = "Real-Time Respiratory Analysis"
    feature1_description = ("Instantly processes uploaded audio to detect potential respiratory issues, "
                             "providing immediate feedback. This reduces diagnostic delays and supports "
                             "quicker medical decisions, especially useful for telemedicine and remote health monitoring.")

    feature2_heading = "Spectrogram Visualization"
    feature2_description = ("Generates high-quality spectrograms from audio inputs, allowing healthcare professionals "
                             "to visually interpret respiratory sound patterns for more accurate and explainable diagnosis.")

    feature3_heading = "AI-Powered Disease Prediction"
    feature3_description = ("Utilizes advanced AI models to predict respiratory diseases based on audio features, "
                             "enhancing diagnostic accuracy and enabling proactive healthcare measures. "
                             "This feature supports conditions like asthma, COPD, and pneumonia.")
    

    

    # Features section
    st.markdown(f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
            .features-container {{
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                margin-top: 10px;
                gap: 15px;
            }}
            .card {{
                flex-basis: 25%;
                margin: 5px;
                padding: 20px;
                background: linear-gradient(135deg, #ffffff 0%, #e6e9f0 100%);
                border-radius: 20px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }}
            .card:hover {{
                transform: translateY(-10px);
                box-shadow: 0 12px 20px rgba(0, 0, 0, 0.2);
            }}
            .card img {{
                max-width: 100%;
                max-height: 300px;
                border-radius: 10px;
                transition: transform 0.3s ease-in-out;
            }}
            .card img:hover {{
                transform: scale(1.05);
            }}
            .card h3 {{
                margin-top: 15px;
                font-weight: 600;
                color: #2c3e50;
            }}
            .card p {{
                font-weight: 300;
                line-height: 1.7;
            }}
            @media (max-width: 768px) {{
                .card {{
                    flex-basis: calc(100% - 30px);
                }}
            }}
        </style>
        <div class="features-container">
            <div class="card">
                <img src="data:image/jpeg;base64,{image1_base64}" alt="Real-Time Respiratory Analysis">
                <h3>{feature1_heading}</h3>
                <p>{feature1_description}</p>
            </div>
            <div class="card">
                <img src="data:image/jpeg;base64,{image2_base64}" alt="Spectrogram Visualization">
                <h3>{feature2_heading}</h3>
                <p>{feature2_description}</p>
            </div>
            <div class="card">
                <img src="data:image/jpeg;base64,{image3_base64}" alt="AI-Powered Disease Prediction">
                <h3>{feature3_heading}</h3>
                <p>{feature3_description}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

        # Rectangular Box Section
    st.markdown("""
        <style>
            .info-box {
                margin-top: 30px;
                padding: 20px;
                background: linear-gradient(135deg, #ffffff 0%, #e6e9f0 100%);
                border-radius: 15px;
                color: #2c3e50;
                text-align: center;
                box-shadow: 0 6px 15px rgba(0,0,0,0.2);
                max-width: 1300px;
                margin-left: auto;
                margin-right: auto;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .info-box h2 {
                font-weight: 500;
                margin-bottom: 10px;
            }
            .info-box p {
                font-weight: 300;
                font-size: 18px;
                line-height: 1.6;
            }
            .info-box:hover {
                transform: translateY(-10px);
                box-shadow: 0 12px 20px rgba(0, 0, 0, 0.2);
            }
        </style>
         
        <div class="info-box">
           <h1 style="font-weight: 600; color: #0a4e8d; text-shadow: 0px 2px 4px rgba(0,0,0,0.2);">Use Cases of Respiratory Disease Analysis</h1>
            <h2>Healthcare & Hospitals </h2>
            <p>
                AI-based respiratory analysis enables early diagnosis, remote monitoring, and real-time decision support for doctors.
                It reduces hospital visits for chronic patients and improves accuracy in detecting asthma, COPD, or pneumonia
            </p>
            <h2>Workplace Safety & Occupational Health  </h2>
            <p>
                Monitors lung health of workers exposed to dust, fumes, or chemicals in industries.
                Supports compliance, insurance claims reduction, and workplace air quality assessment.
            </p>
            <h2>Public Health & Government </h2>
            <p>
                Helps in large-scale screening and epidemic tracking 
                Enables data-driven policy, resource allocation, and population health analytics.
            </p>
        </div>
    """, unsafe_allow_html=True)

    #usecases
    st.markdown("""
        <style>
            .info-box {
                margin-top: 30px;
                padding: 20px;
                background: linear-gradient(135deg, #ffffff 0%, #e6e9f0 100%);
                border-radius: 15px;
                color: #2c3e50;
                text-align: center;
                box-shadow: 0 6px 15px rgba(0,0,0,0.2);
                max-width: 1300px;
                margin-left: auto;
                margin-right: auto;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .info-box h2 {
                font-weight: 500;
                margin-bottom: 10px;
            }
            .info-box p {
                font-weight: 300;
                font-size: 18px;
                line-height: 1.6;
            }
            .info-box:hover {
                transform: translateY(-10px);
                box-shadow: 0 12px 20px rgba(0, 0, 0, 0.2);
            }
        </style>
         
        <div class="info-box">
           <h1 style="font-weight: 600; color: #0a4e8d; text-shadow: 0px 2px 4px rgba(0,0,0,0.2);">Audio Analytics Use cases in Other Industries</h1>
            <h2>Transportation & Automotive </h2>
            <p>
                Detects engine issues through sound; analyzes driver voice for stress or fatigue detection
            </p>
            <h2> Banking & Finance  </h2>
            <p>
                Uses voice biometrics for fraud prevention; monitors calls for compliance and regulatory breaches.
            </p>
            <h2>Security & Surveillance</h2>
            <p>
                Recognizes gunshots, glass breaks, or aggression; strengthens authentication with voice recognition.
            </p>
        </div>
    """, unsafe_allow_html=True)


   