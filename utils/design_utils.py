import streamlit as st
from PIL import Image
import json
from streamlit_lottie import st_lottie
import gettext
_gettext = gettext.gettext


def create_featurecard(text,background_color='#FFFFF',font_size='20px'):
    st.markdown(
            f"""
            <div style='background-color: {background_color}; 
            padding: 20px; 
            border-radius: 
            0px; 
            width: 100%;
            height: 300px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            '>
            
            <span style='color: black;
            text-align: center;font-size: {font_size};
            color: #635F5F;
            '>{text}</span>
            </div>
            """,
            unsafe_allow_html=True
            )
    
   
def create_specific_feature(text_heading, description,image_path, heading_font_size='30px',description_font_size ='18px',image_present=True,image_right_side=True,lottie_image=True):
    
        
        with st.container():
            #first_section, second_section = st.columns((2,1))
            
            if image_right_side==True:
                #content_section = first_section
                #image_section=second_section 
                content_section, image_section = st.columns((2,1))
                             
            else:
                #content_section = second_section
                #image_section=first_section
                image_section, content_section = st.columns((1,2))
                
                
                
                
            
            with content_section:
                background_color = 'white'#'#eaebf0'
                
                
                #text = 'Stay Informed with Curated Daily News'
                #description = 'Stay updated with the latest developments in the stock market effortlessly. Our app curates news related to the stocks you care about on a daily basis. We understand that staying informed is crucial for making well-informed investment decisions.'
                st.markdown(
                f"""
                <div style='background-color: {background_color}; 
                padding: 20px; 
                border-radius: 
                0px; 
                width: 100%;
                height: 300px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                text-align: start;
                '>
                
                <span style='color: black;
                text-align: start;font-size: {heading_font_size};
                color: #799BE6;/*#635F5F*/
                '>{text_heading}</span>
                <br>
                <br>
                <span style='color: black;
                text-align: start;font-size:{description_font_size};
                color: #635F5F;
                '>{description}</span>
                
                </div>
                
                
                """,
                unsafe_allow_html=True
                )
                
            with image_section:
                if image_present:
                    if lottie_image:
                        lottie_img = load_lottiefile(image_path)
                        st_lottie(lottie_img,height=300,speed=0.5)
                    else:
                        news_image = Image.open(image_path)
                        st.image(news_image)

@st.cache_resource 
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

@st.cache_resource 
def display_output(title, content, heading_type='normal'):
    if heading_type == 'button':
        title_style = "background-color: #007bff; color: white; padding: 5px 10px; border-radius: 5px; display: inline-block; font-weight: bold;"
    elif heading_type == 'h1':
        title_style = "font-size: 24px; font-weight: bold; margin-bottom: 15px;"
    else:
        title_style = ""

    st.markdown(f"<div class='glassmorphism'><h4 style='{title_style}'>{title}</h4><p style='color:#535050; font-size: 14px;'>{content}</p></div>", unsafe_allow_html=True)







@st.cache_resource

def setup_common_styles():
    # Common styles for both English and Japanese messages
    common_styles = """
        <style>
            @keyframes fadeIn {
                0% { opacity: 0; transform: translateY(-20px); }
                100% { opacity: 1; transform: translateY(0); }
            }
            .welcome-message {
                padding: 4px 4px 10px 4px;
                border: 1px dashed #d0d0d0;
                border-radius: 0px; 
                background: linear-gradient(to right, #f7f7f7, #e7e7e7);
                color: #333333;
                box-shadow: 0 10px 20px rgba(0,0,0,0.1); 
                text-align: center;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                animation: fadeIn 1s ease-in-out;
                margin-top: -08px;
                margin-bottom: 2px;
            }
            .welcome-message h2 {
                margin-bottom: 0.3em; 
                font-weight: 600; 
                font-size: 1.2em;
            }
            .welcome-message p {
                margin-bottom: 0.5em; 
                font-size: 1em;
            }
            .welcome-message:hover {
                transform: scale(1.03);
                box-shadow: 0 8px 20px rgba(0,0,0,0.15);
            }
        </style>
    """
    st.markdown(common_styles, unsafe_allow_html=True)

def display_english_welcome_message():
    # English message setup
    h1 = "Welcome to Insights! 👋"
    h2 = "Discover the story hidden in your data. Upload your document and click <b>'Analyze'</b> to start exploring."
    h3 = "Embark on your journey of data discovery!"
    display_welcome_message(h1, h2, h3)

def display_japanese_welcome_message():
    # Japanese message setup
    h1 = "インサイトへようこそ！ 👋"
    h2 = "データに隠されたストーリーを発見しましょう。ドキュメントをアップロードして<b>'分析'</b>をクリックして探索を開始してください。"
    h3 = "データ発見の旅に出ましょう！"
    display_welcome_message(h1, h2, h3)

def display_welcome_message(h1, h2, h3):
    # Common HTML setup for both messages
    message_html = f"""
    <div class='welcome-message'>
        <h2>{h1}</h2>
        <p>{h2}</p>
        <p>{h3}</p>
    </div>
    """
    st.markdown(message_html, unsafe_allow_html=True)

# Call this function at the start of your app to set up common styles
#setup_common_styles()

# Then you can call either of these functions based on the user's language preference
# display_english_welcome_message()
# display_japanese_welcome_message()
