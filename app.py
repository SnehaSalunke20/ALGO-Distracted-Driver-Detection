# Importing required libraries

import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import os
import io
import base64

from homepage import homepage_v3
from dashboard import demo_dashboard
from auth.login_ui import create_login_panel
from utils.load import custom_footer
from utils.load import apply_custom_style

if "lang" not in st.session_state:
    st.session_state.lang = "en"

# TRANSLATE
# =============================================================================================================
import gettext

_gettext = gettext.gettext

try:
    localizator = gettext.translation(
        "base", localedir="locales", languages=[st.session_state.lang]
    )
    localizator.install()
    _gettext = localizator.gettext
except Exception as e:
    print("inside exception")
    print(e)
# =============================================================================================================

def session_state_lang_change_callback():
    st.session_state['past'] = []
    st.session_state['generated'] = []
    st.session_state.text_value = ''

st.set_page_config(
    page_title=_gettext("Respiratory Disease Analysis App"), layout="wide", page_icon="ui_assets/images/algo-logo.png"
)

with open("css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def on_click_js(url):
    st.write("Redirecting")
    return f"""
        <script>
            var win = window.open('{url}', '_blank');
            win.focus();
        </script>
    """

apply_custom_style()
def navbar():
    with open("ui_assets/images/algo-logo.png", "rb") as img_file:
        brand_image = base64.b64encode(img_file.read()).decode()

    app_name1 = _gettext("Applications Powered By Large Language Models")
    navbar1, navbar_lang = st.columns([0.92, 0.08])
    with navbar1:
        navbar_style = """
        <style>
        .navbar {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 2rem;
            background-color: #E1EDFA;
            border-radius: 5px;
        }
        @media (min-width: 768px) {
            .navbar {
            flex-direction: row;
            }
        }

        .navbar-item {
            display: flex;
            align-items: center;
        }
        .navbar-links-buttons {
            display: flex;
            gap: 1rem;
            align-items: center;
        }
        .navbar-links-buttons a {
            color: #263557;
            text-decoration: none;
        }
        .navbar-buttons a {
            text-decoration: none;
            color:white;
        }
        .navbar-title-logo {
            display: flex;
            align-items: center;
        }   
        .app-name {
            font-size: 1.5rem;
            font-weight: bold;
            margin-left: 1rem;
            padding: 0.5rem 0;
        }
        .navbar-tabs {
            display: flex;
            gap: 1rem;
        }
        .tab-item {
            font-size: 1rem;
            font-weight: bold;
            color: #263557;
            text-decoration: none;
        }
        .navbar-buttons {
            display: flex;
            gap: 1rem;
        }
        .button {
            color: white;
            background-color: #799BE6;
            border: none;
            border-radius: 4px;
            padding: 5px 10px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
        .lang-selector {
            padding: 5px;
            font-size: 1rem;
        }
        </style>
        """

        llm_dashboard_text = "LLM Dashboard" if st.session_state.lang == "en" else "LLMダッシュボード"
        
        navbar_html = f"""
        <div class="navbar">
                <div class="navbar-title-logo">
                    <img src="data:image/png;base64,{brand_image}" width="70">
                    <h3 class="app-name">{app_name1}</h3>
                </div>
                <div class="navbar-links-buttons">
                    <div class = "navbar-buttons">
                        <button class="button">
                            <a href="https://apps.onestop.ai/llm-dashboard/" target="_blank">{llm_dashboard_text}</a>
                        </button>
                    </div>
                </div>
        </div>
        """

        st.markdown(navbar_html + navbar_style, unsafe_allow_html=True)

    with navbar_lang:
        option = st.selectbox(
            label="Language Selector",
            options=("en", "ja"),
            label_visibility="collapsed",
            key="lang",
            on_change=session_state_lang_change_callback
        )

    navbarJs = f"""
        <script>
        // Select first as navbar will be at top
        var navbar = window.parent.document.querySelector('div[data-testid="stHorizontalBlock"]');
        
        // Modify navbar column base style
        navbar.style.backgroundColor = '#E1EDFA';
        navbar.style.gap = 0;
        
        // Modify selectbox style
        var selectbox = navbar.children[1]
        
        // Second child is the selectbox
        selectbox.style.padding = '1.5rem 0.5rem';
        </script>
        """
    components.html(navbarJs, height=0, width=0)

# Call navbar function
navbar()


def FAQSection(_gettext):
    faq_list = [
        {
            "question": _gettext("What is the purpose of this respiratory diagnosis dashboard?"),
            "answer": _gettext("This dashboard enables healthcare professionals and researchers to analyze respiratory audio files using AI-powered algorithms to identify potential disease patterns. It helps in early detection, reducing diagnosis time, and supporting decision-making."),
        },
        {
            "question": _gettext("How accurate are the AI-generated results?"),
            "answer": _gettext("The accuracy depends on the quality of the input audio and the AI model used. The system is trained on medical datasets, but it is not a replacement for professional diagnosis. Results should be used as an additional aid for healthcare experts."),
        },
        {
            "question": _gettext("Is my uploaded audio file stored permanently"),
            "answer": _gettext("No, all uploaded audio files are processed temporarily during the analysis session and are not stored permanently. This ensures data privacy and compliance with security standards."),
        },
        {
            "question": _gettext("What audio formats are supported for analysis?"),
            "answer": _gettext("The system supports common audio formats such as WAV and MP3. Ensure that the audio file is clear and of good quality for optimal analysis results."),
        },
        {
            "question": _gettext("Can this tool detect multiple respiratory diseases?"),
            "answer": _gettext("Yes, depending on the trained model, the tool can identify various respiratory conditions such as asthma, bronchitis, pneumonia, and COVID-related lung sounds. Future updates may expand its disease detection capabilities."),
        },
        {
            "question": _gettext("How can I provide feedback or report issues with the dashboard?"),
            "answer": _gettext("You can provide feedback or report issues through the contact form available on the dashboard. Your input is valuable for improving the system and user experience."),
        },
    ]


    faq_styles = """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&display=swap" rel="stylesheet">
    <style>
    .faq-section {
        padding: 1rem 5vw;
    }
    .faq-section-title-div {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .faq-section-title {
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
        text-align: center;
        font-family: 'Poppins', sans-serif;
        font-size: 1.5rem;
        font-weight: 400;
        background-color: #799BE6;
        color: white;
    }
    .faq-section-questions-list {
        width: 75%;
        padding: 1rem 0;
        margin: 0 auto;
    }
    .faq-section-question-split {
        display: flex;
        align-items: start;
        padding: 1rem 0;
        border-bottom: 1px solid #789BE6;
    }
    .faq-section-question-answer {
        font-family: 'DM Sans', 'Poppins', sans-serif;
        flex-grow: 1;
    }
    .faq-section-question {
        margin: 0.5rem 0;
        font-size: 1.5rem;
        font-weight: 500;
        color: #789BE6;
    }
    .faq-section-answer {
        margin: 0.5rem 0;
        font-size: 1.25rem;
        color: #6F6C90;
        overflow: hidden;
        overflow-y: scroll;
    }
    .faq-section-question-dropdown {
        background-color: transparent;
        border: none;
        outline: none;
        cursor: pointer;
        padding: 0.5rem;
    }
    .faq-section-question-dropdown:hover {
        border: none;
        outline: none;
    }
    .faq-section-question-dropdown-img {
        width: 2rem;
    }
    </style>"""
    
    # Map over the FAQ list to generate the HTML
    faq_questions_html = ""
    for i in range(len(faq_list)):
        faq = faq_list[i]
        faq_questions_html += f"""<div class="faq-section-question-split">
            <div class="faq-section-question-answer">
                <div class="faq-section-question">
                {faq['question']}
                </div>
                <div id="faq-section-answer-{i}" class="faq-section-answer" style="max-height:0px;">
                {faq['answer']}
                </div>
            </div>
            <button id="faq-section-question-dropdown-{i}" class="faq-section-question-dropdown">
                <img
                class="faq-section-question-dropdown-img"
                alt="close"
                src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxZW0iIGhlaWdodD0iMWVtIiB2aWV3Qm94PSIwIDAgMjQgMjQiPjxwYXRoIGZpbGw9ImN1cnJlbnRDb2xvciIgZD0iTTE4IDEyLjk5OGgtNXY1YTEgMSAwIDAgMS0yIDB2LTVINmExIDEgMCAwIDEgMC0yaDV2LTVhMSAxIDAgMCAxIDIgMHY1aDVhMSAxIDAgMCAxIDAgMiIvPjwvc3ZnPg=="
                />
            </button>
        </div>"""
    faq_section_title = _gettext("Frequently Asked Questions")


    faq_html = f"""
    <div class="faq-section">
        <div class="faq-section-title-div">
            <div class="faq-section-title">{faq_section_title}</div>
        </div>
        <div class="faq-section-questions-list">
        {faq_questions_html}
        </div>
    </div>
    """

    faq_js = """
    <script>
    console.log('FAQ Section JS')
    const faqDropdownButtons = window.parent.document.querySelectorAll('.faq-section-question-dropdown');
    const faqAnswers = window.parent.document.querySelectorAll('.faq-section-answer');
    console.log(faqDropdownButtons);
    faqDropdownButtons.forEach((button, index) => {
        button.addEventListener('click', () => {
            console.log('clicked dropdown button {index}');
            const answer = faqAnswers[index];
            // Toggle the display of the answer
            console.log(answer.style.maxHeight, answer.style.maxHeight === '0px');
            if (answer.style.maxHeight === '0px') {
                answer.style.maxHeight = 'fit-content';
                button.children[0].src = 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxZW0iIGhlaWdodD0iMWVtIiB2aWV3Qm94PSIwIDAgMjQgMjQiPjxwYXRoIGZpbGw9ImN1cnJlbnRDb2xvciIgZD0iTTE4IDEyLjk5OEg2YTEgMSAwIDAgMSAwLTJoMTJhMSAxIDAgMCAxIDAgMiIvPjwvc3ZnPg==';
            } else {
                answer.style.maxHeight = '0px';
                button.children[0].src = 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxZW0iIGhlaWdodD0iMWVtIiB2aWV3Qm94PSIwIDAgMjQgMjQiPjxwYXRoIGZpbGw9ImN1cnJlbnRDb2xvciIgZD0iTTE4IDEyLjk5OGgtNXY1YTEgMSAwIDAgMS0yIDB2LTVINmExIDEgMCAwIDEgMC0yaDV2LTVhMSAxIDAgMCAxIDIgMHY1aDVhMSAxIDAgMCAxIDAgMiIvPjwvc3ZnPg==';
            }
        });
    });
    </script>
    """

    st.markdown(
        faq_styles + faq_html,
        unsafe_allow_html=True,
    )
    components.html(faq_js, height=0, width=0)

if "option_menu" not in st.session_state:
    st.session_state.option_menu = "Overview"

if st.session_state.get("demo_button", False):
    st.session_state["manual_select"] = 1
    manual_select = st.session_state["manual_select"]
else:
    manual_select = None

selected_tab = option_menu(
    None,
    [_gettext("Overview"), _gettext("Demo")],  # ,_gettext('Login')
    icons=["house-fill", "arrow-up-circle-fill"],  #'box-arrow-in-right'
    key="option_menu",
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    manual_select=manual_select,
    styles={
        "container": {
            "padding": "0.01",
            "background-color": "#E1EDFA00",
        },  # E1EDFA99
        # "icon": {"font-size": "20px"}, #"#789BE6"
        "nav-link": {
            "font-size": "15px",
            "color": "grey",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#E1EDFA",
            "--background-color": "grey",
            "background-color": "rgb(33 61 120 / 21%)",
        },
        "nav-link-selected": {"background-color": "#789BE600", "color": "#789BE6"},
    },
)

if st.session_state.option_menu in ["Overview", "概要"]:  # ==_gettext("Home")

    homepage_v3(_gettext)
    custom_footer(_gettext)


# ---------Dashboard-----------------------------
elif st.session_state.option_menu in ["Demo", "デモ"]:  # ==_gettext('Demo Dashboard')

    # Readjusting the styling for demo dashboard containers to get displayed as expected
    st.markdown(
        """
    <style>
        div[data-testid="column"]:nth-of-type(1)
        {
            align-items: center
        } 

        div[data-testid="column"]:nth-of-type(2)
        {
            
            text-align: start;
        } 
        div[data-testid="column"]:nth-of-type(3)
        {
            text-align: center;
            
        } 
    </style>
    """,
        unsafe_allow_html=True,
    )
    
    # App Title Section
    app_title_name = _gettext("Respiratory Disease Detection App")
    app_title_tagline = _gettext("AI-powered analysis of respiratory sounds for faster, smarter health insights")

    back_button_text = "Back" if st.session_state.lang == "en" else "戻る"
    readme_button_text = "Readme" if st.session_state.lang == "en" else "お読みください"

    # Define the readme_text with fallback for Japanese
    try:
        readme_text = _gettext("""
            Welcome to the Respiratory Disease Detection App

            Log in using the form on the right, or explore the features with sample respiratory  audio data
            by following the steps below.

            1) Upload or Select Sample Audio — Utilize the provided respiratory sound recordings  or upload
             your own .wav files for analysis.

            2) Click on 'Analyze Audio' — The system will process the sound to identify patterns,anomalies,
             and possible disease indications using advanced AI/ML models.

            3) View Diagnostic Insights — The results will be displayed on the interface, including
             spectrograms, predicted disease categories, and confidence levels.

            4) Download Analysis Reports — Export the detailed diagnostic summary in formats like PDF,CSV,
             or Excel for further reference or sharing with healthcare professionals.

            5) Use Insights for Medical Guidance — Leverage the AI-generated analysis to assist doctors
             in making early and informed medical decisions
        """)
        if st.session_state.lang == 'ja' and "Welcome to the Respiratory Disease Detection App" in readme_text:
            readme_text = """
                カスタマー フィードバック分析アプリへようこそ

                右側のフォームを使用してログインを開始するか、次の手順に従ってログインせずにサンプル データで機能を探索できます。

                1. 提供されたサンプル フィードバック データを使用して、顧客の感情を分析します。
                2. 関連するデータを入力または選択した後、「フィードバックを分析」ボタンをクリックします。
                3. ユーザー インターフェイスに直接表示される洞察と傾向を、わかりやすい形式で表示します。
                4. 必要に応じて、PDF、CSV、Excel などのさまざまな形式で分析レポートをダウンロードできます。
                5. 洞察を活用してビジネスの意思決定を行い、顧客満足度を向上させます。
            """
    except Exception as e:
        if st.session_state.lang == 'ja':
            readme_text = """
                カスタマー フィードバック分析アプリへようこそ

                右側のフォームを使用してログインを開始するか、次の手順に従ってログインせずにサンプル データで機能を探索できます。

                1. 提供されたサンプル フィードバック データを使用して、顧客の感情を分析します。
                2. 関連するデータを入力または選択した後、「フィードバックを分析」ボタンをクリックします。
                3. ユーザー インターフェイスに直接表示される洞察と傾向を、わかりやすい形式で表示します。
                4. 必要に応じて、PDF、CSV、Excel などのさまざまな形式で分析レポートをダウンロードできます。
                5. 洞察を活用してビジネスの意思決定を行い、顧客満足度を向上させます。
            """
        else:
            readme_text = """
                Welcome to the Respiratory Disease Detection App

            Let's begin by logging in using the form on the right, or alternatively, you can explore the functionality with sample respiratory 
            audio data without logging in by following the instructions below:

            1) Upload or Select Sample Audio — Utilize the provided respiratory sound recordings or 
            upload your own .wav files for analysis.

            2) Click on 'Analyze Audio' — The system will process the sound to identify patterns, 
            anomalies, and possible disease indications using advanced AI/ML models.

            3) View Diagnostic Insights — The results will be displayed on the interface, including 
            spectrograms, predicted disease categories, and confidence levels.

            4) Download Analysis Reports — Export the detailed diagnostic summary in formats like PDF, 
            CSV, or Excel for further reference or sharing with healthcare professionals.

            5) Use Insights for Medical Guidance — Leverage the AI-generated analysis to assist doctors 
            in making early and informed medical decisions
            """

    app_title_styles = """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900&display=swap" rel="stylesheet">
    <style>
        .app-title-div {
            padding: 0;
            padding-bottom: 2vh;
            text-align: center;
            position: relative;
        }
        .app-title-button-link {
            text-decoration: none;
        }
        .app-title-button {
            position: absolute;
            background-color: white;
            display: grid;
            grid-auto-flow: column;
            align-items: center;
            border-radius: 0.375rem;
            padding-left: 0.5rem;
            padding-right: 0.5rem;
            padding-top: 0.25rem;
            padding-bottom: 0.25rem;
            border: 2px solid black;
        }
        .app-title-button:hover {
            background-color: #799BE6;
            color: white;
            border-color: #799BE6;
        }
        .app-title-button img {
            height: 1.5rem;
            margin: 0 0.25rem;
            padding: 0.25rem;
        }
        .app-title-button-back {
            top: 0;
            left: 0;
        }
        .app-title-button-readme {
            top: 0;
            right: 0;
        }
        .app-title-text {
            margin: 0.5rem 0;
            color: #1F2937;
            font-size: 1.875rem;
            font-weight: 700;
        }
        @media (min-width: 768px) {
            .app-title-text {
                padding: 0;
                font-size: 2.25rem;
            }
        }
        .app-title-subtext {
            margin: 0.5rem 0;
            color: #4B5563;
            font-size: 1rem;
        }
        @media (min-width: 768px) {
            .app-title-subtext {
                font-size: 1.125rem;
            }
        }
        .readme-dialog {
            z-index: -10;
            width: 70%;
            max-height: 60vh;
            margin-top: 20vh;
            overflow-y: auto;
            padding: 1rem;
            border: 2px solid #789BE6;
            transform: translate(0,-100%);
            transition: transform 1s;
            display: block;
        }
        .readme-dialog[open] {
            z-index: 10;
            transform: translate(0,0);
            pointer-events: inherit;
        }
        .readme-dialog::backdrop {
            background-color: rgba(0, 0, 0, 0.5);
        }
        .readme-dialog-text {
            padding: 1rem 2rem;
        }
        .readme-dialog-text * {
            font-family: 'Poppins', sans-serif;
            font-size: 1.1rem !important;
            font-weight: 400;
            line-height: 1.5rem;
        }
    </style>
    """

    app_title_html = f"""
    <div class="app-title-div">
        <a target="_self" href="/" class="app-title-button-link">
            <button class="app-title-button app-title-button-back">
                <img alt="" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxZW0iIGhlaWdodD0iMWVtIiB2aWV3Qm94PSIwIDAgMTAyNCAxMDI0Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0yMjQgNDgwaDY0MGEzMiAzMiAwIDEgMSAwIDY0SDIyNGEzMiAzMiAwIDAgMSAwLTY0Ii8+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJtMjM3LjI0OCA1MTJsMjY1LjQwOCAyNjUuMzQ0YTMyIDMyIDAgMCAxLTQ1LjMxMiA0NS4zMTJsLTI4OC0yODhhMzIgMzIgMCAwIDEgMC00NS4zMTJsMjg4LTI4OGEzMiAzMiAwIDEgMSA0NS4zMTIgNDUuMzEyeiIvPjwvc3ZnPg==" />
                <div>{back_button_text}</div>
            </button>
        </a>
        <div class="app-title-text-div">
            <div style="text-align: center;">
                <h1 style="font-weight: 600; color: #0a4e8d; text-shadow: 0px 2px 4px rgba(0,0,0,0.2);">{app_title_name}</h1>
                <h2 style="font-weight: 300; color: #555;">{app_title_tagline}</h2>
            </div>
        </div>
        <button id="open-readme-dialog" class="app-title-button app-title-button-readme">
            <div>{readme_button_text}</div>
            <img alt="" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxZW0iIGhlaWdodD0iMWV3Qm94PSIwIDAgMjYgMjYiPjxwYXRoIGZpbGw9ImN1cnJlbnRDb2xvciIgZD0iTTQgMEMxLjc5NSAwIDAgMS43OTUgMCA0djE4YzAgMi4yMDUgMS43OTUgNCA0IDRoMTNjMS4wNjMgMCAyLjUzOS0xLjUzNSA0LjI1LTMuMjgxYy4yNC0uMjQ0LjQ3LS40NzMuNzE5LS43MTljLjI0Ni0uMjQ4LjUwNi0uNTEuNzUtLjc1QzI0LjQ2NiAxOS41MzggMjYgMTguMDYzIDI2IDE3VjRjMC0yLjIwNS0xLjc5NS00LTQtNHptMCAyaDE4YTIgMiAwIDAgMSAyIDJ2MTNjMCAuOTk1LTEuMDAyIDEtMiAxaC0zYy0uNTUxIDAtMSAuNDQ5LTEgMXYzLjA2M2MwIC44ODcuMDAyIDEuNzUzLS43MTkgMS45MzdINGEyIDIgMCAwIDEtMi0yVjRhMiAyIDAgMCAxIDItMm0yLjgxMyA2QTEuMDAxIDEuMDAxIDAgMCAwIDcgMTBoMTJhMSAxIDAgMSAwIDAtMkg3YTEgMSAwIDAgMC0uMDk0IDBhMS4wMDEgMS4wMDEgMCAwIDAtLjA5MyAwbTAgNUExLjAwMSAxLjAwMSAwIDAgMCA3IDE1aDEwYTEgMSAwIDEgMCAwLTJIN2ExIDEgMCAwIDAtLjA5NCAwYTEuMDAxIDEuMDAxIDAgMCAwLS4wOTMgMCIvPjwvc3ZnPg==" />
        </button>
    </div>
    """

    app_title_readme_html = f"""
    <dialog id="readme-dialog" class="readme-dialog">
    <div class="readme-dialog-text">
    {readme_text}
    </div>
    </dialog>
    """

    app_title_readme_js = """
        <script>
        const dialog = window.parent.document.getElementById('readme-dialog');
        
        dialog.addEventListener('click', function(event) {
            const rect = dialog.getBoundingClientRect();
            const isInDialog = (rect.top <= event.clientY && event.clientY <= rect.top + rect.height &&
            rect.left <= event.clientX && event.clientX <= rect.left + rect.width);
            if (!isInDialog) {
            dialog.close();
            }
        });

        const readmeButton = window.parent.document.getElementById('open-readme-dialog');
        readmeButton?.addEventListener('click', (event) => {
            dialog.showModal();
        });
        </script>
    """

    st.markdown(
        app_title_styles + app_title_html + app_title_readme_html,
        unsafe_allow_html=True,
    )

    components.html(app_title_readme_js, height=0, width=0)
    tab1, login_tab = st.tabs([_gettext("Demo Dashboard"), _gettext("Login")])

    with login_tab:
        col1, login_column, col3 = st.columns((1, 1, 1))

        # --------content column-------------------------
        with login_column:
            create_login_panel(_gettext)

        custom_footer(_gettext)

    with tab1:
        demo_dashboard(_gettext)
        st.write()
        st.markdown("<br>", unsafe_allow_html=True) 
        st.markdown("<br>", unsafe_allow_html=True) 
        st.markdown("<br>", unsafe_allow_html=True) 
        FAQSection(_gettext)
        custom_footer(_gettext)


elif st.session_state.option_menu in ["Login", "ログイン"]:
    col1, login_column, col3 = st.columns((1, 1, 1))

    # --------content column-------------------------
    with login_column:
        create_login_panel(_gettext)

    custom_footer(_gettext)


elif st.session_state.option_menu in ["Contact us", "お問い合わせ"]:
    st.markdown("<br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
    custom_footer(_gettext)
