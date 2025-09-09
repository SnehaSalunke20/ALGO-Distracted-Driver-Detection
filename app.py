# # app.py

# # =================================================================================================
# # SECTION 0: IMPORTING REQUIRED LIBRARIES
# # =================================================================================================
# import streamlit as st
# import streamlit.components.v1 as components
# from streamlit_option_menu import option_menu
# import base64
# import gettext

# # --- Import custom modules from your other files ---
# # This structure keeps your code organized and clean.
# # FIX: Removed 'create_login_panel' as it is not used in this application.
# from homepage import homepage_v3
# from dashboard import demo_dashboard
# from utils.load import custom_footer, apply_custom_style

# # =================================================================================================
# # SECTION 1: LANGUAGE AND SESSION STATE SETUP
# # =================================================================================================
# # Initialize session state for language selection if it doesn't exist
# if "lang" not in st.session_state:
#     st.session_state.lang = "en"

# # Setup for multi-language support (gettext).
# _gettext = gettext.gettext
# try:
#     # This looks for translation files if you decide to add them later.
#     localizator = gettext.translation("base", localedir="locales", languages=[st.session_state.lang])
#     localizator.install()
#     _gettext = localizator.gettext
# except Exception:
#     # If translation files aren't found, it defaults to English without crashing.
#     pass

# def session_state_lang_change_callback():
#     """Clears key parts of the session state when the user changes the language."""
#     # A list of session state keys to reset
#     keys_to_clear = ['past', 'generated', 'text_value', 'analysis_result', 'image_to_analyze']
#     for key in keys_to_clear:
#         if key in st.session_state:
#             del st.session_state[key]

# # Configure the page settings (title, layout, icon) that appear in the browser tab.
# st.set_page_config(
#     page_title=_gettext("Distracted Driver Detection App"),
#     layout="wide",
#     page_icon="ui_assets/images/algo-logo.png"
# )

# # =================================================================================================
# # SECTION 2: STYLING AND UI FUNCTIONS
# # =================================================================================================
# # Load custom CSS from your external file
# try:
#     with open("css/style.css") as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# except FileNotFoundError:
#     st.warning("css/style.css not found. The app will use default styling.")

# # Apply any additional global styles from your utils/load.py file
# apply_custom_style()

# def navbar():
#     """Creates and displays the top navigation bar of the application."""
#     try:
#         # Load the logo image and encode it to embed directly in HTML
#         with open("ui_assets/images/algo-logo.png", "rb") as img_file:
#             brand_image = base64.b64encode(img_file.read()).decode()
#     except FileNotFoundError:
#         st.error("Logo file 'ui_assets/images/algo-logo.png' not found.")
#         brand_image = ""

#     app_name1 = _gettext("Applications Powered By Large Language Models")
#     # Use Streamlit columns for a responsive layout
#     navbar1, navbar_lang = st.columns([0.92, 0.08])
#     with navbar1:
#         # Inline CSS for the navbar's appearance
#         navbar_style = """
#         <style>
#         .navbar { display: flex; flex-direction: row; justify-content: space-between; align-items: center; padding: 1rem 2rem; background-color: #E1EDFA; border-radius: 5px; }
#         .navbar-title-logo { display: flex; align-items: center; }
#         .app-name { font-size: 1.5rem; font-weight: bold; margin-left: 1rem; padding: 0.5rem 0; color: #263557; }
#         .navbar-buttons a { text-decoration: none; color: white; }
#         .button { color: white; background-color: #799BE6; border: none; border-radius: 4px; padding: 5px 10px; font-size: 16px; cursor: pointer; }
#         </style>
#         """
#         llm_dashboard_text = "LLM Dashboard" if st.session_state.lang == "en" else "LLMダッシュボード"
#         # The HTML structure of the navbar
#         navbar_html = f"""
#         <div class="navbar">
#             <div class="navbar-title-logo">
#                 <img src="data:image/png;base64,{brand_image}" width="70">
#                 <h3 class="app-name">{app_name1}</h3>
#             </div>
#             <div class="navbar-links-buttons">
#                 <div class="navbar-buttons">
#                     <button class="button">
#                         <a href="https://apps.onestop.ai/llm-dashboard/" target="_blank">{llm_dashboard_text}</a>
#                     </button>
#                 </div>
#             </div>
#         </div>
#         """
#         st.markdown(navbar_html + navbar_style, unsafe_allow_html=True)

#     with navbar_lang:
#         # The language selection dropdown
#         st.selectbox("Language", ("en", "ja"), key="lang", on_change=session_state_lang_change_callback, label_visibility="collapsed")

#     # JavaScript to fine-tune the navbar's appearance within Streamlit's layout
#     components.html("""
#     <script>
#         var navbar = window.parent.document.querySelector('div[data-testid="stHorizontalBlock"]');
#         if (navbar) {
#             navbar.style.backgroundColor = '#E1EDFA';
#             navbar.style.gap = 0;
#             var selectbox = navbar.children[1];
#             if (selectbox) { selectbox.style.padding = '1.5rem 0.5rem'; }
#         }
#     </script>
#     """, height=0)

# # =================================================================================================
# # SECTION 3: MAIN APP LAYOUT AND NAVIGATION
# # =================================================================================================
# # Display the navbar at the top of the page
# navbar()

# # Initialize session state for the menu if it doesn't already exist
# if "option_menu" not in st.session_state:
#     st.session_state.option_menu = _gettext("Overview")

# # This logic allows the "Try Demo" button on the homepage to switch the tab
# if st.session_state.get("demo_button", False):
#     st.session_state.option_menu = _gettext("Demo")
#     st.session_state["demo_button"] = False # Reset the button state to prevent looping

# # Create the main navigation menu (tabs) using streamlit_option_menu
# selected_tab = option_menu(
#     None, [_gettext("Overview"), _gettext("Demo")],
#     icons=["house-fill", "camera-fill"],
#     key="option_menu",
#     menu_icon="cast",
#     default_index=0,
#     orientation="horizontal",
#     styles={
#         "container": {"padding": "0.01", "background-color": "#E1EDFA00"},
#         "nav-link": {"font-size": "15px", "color": "grey", "text-align": "center", "margin": "0px", "--hover-color": "#E1EDFA"},
#         "nav-link-selected": {"background-color": "#789BE600", "color": "#789BE6"},
#     }
# )

# # --- Page Routing Logic ---
# # Based on the selected tab, call the appropriate function to render the page content.
# if st.session_state.option_menu == _gettext("Overview"):
#     # If "Overview" is selected, call the function from homepage.py
#     homepage_v3(_gettext)
#     # FIX: Pass the _gettext function to the footer for language translation
#     custom_footer(_gettext)
# elif st.session_state.option_menu == _gettext("Demo"):
#     # If "Demo" is selected, call the function from dashboard.py
#     demo_dashboard(_gettext)



# app.py

# =================================================================================================
# SECTION 0: IMPORTING REQUIRED LIBRARIES
# =================================================================================================
import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import base64
import gettext

# --- Import custom modules from your other files ---
# This structure keeps your code organized and clean.
from homepage import homepage_v3
from dashboard import demo_dashboard
from utils.load import custom_footer, apply_custom_style

# =================================================================================================
# SECTION 1: LANGUAGE AND SESSION STATE SETUP
# =================================================================================================
# Initialize session state for language selection if it doesn't exist
if "lang" not in st.session_state:
    st.session_state.lang = "en"

# Setup for multi-language support (gettext).
_gettext = gettext.gettext
try:
    # This looks for translation files if you decide to add them later.
    localizator = gettext.translation("base", localedir="locales", languages=[st.session_state.lang])
    localizator.install()
    _gettext = localizator.gettext
except Exception:
    # If translation files aren't found, it defaults to English without crashing.
    pass

def session_state_lang_change_callback():
    """Clears key parts of the session state when the user changes the language."""
    # A list of session state keys to reset
    keys_to_clear = ['past', 'generated', 'text_value', 'analysis_result', 'image_to_analyze']
    for key in keys_to_clear:
        if key in st.session_state:
            del st.session_state[key]

# Configure the page settings (title, layout, icon) that appear in the browser tab.
st.set_page_config(
    page_title=_gettext("Distracted Driver Detection App"),
    layout="wide",
    page_icon="ui_assets/images/algo-logo.png"
)

# =================================================================================================
# SECTION 2: STYLING AND UI FUNCTIONS
# =================================================================================================
# Load custom CSS from your external file
try:
    with open("css/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("css/style.css not found. The app will use default styling.")

# Apply any additional global styles from your utils/load.py file
apply_custom_style()

def navbar():
    """Creates and displays the top navigation bar of the application."""
    try:
        # Load the logo image and encode it to embed directly in HTML
        with open("ui_assets/images/algo-logo.png", "rb") as img_file:
            brand_image = base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error("Logo file 'ui_assets/images/algo-logo.png' not found.")
        brand_image = ""

    app_name1 = _gettext("Applications Powered By Large Language Models")
    # Use Streamlit columns for a responsive layout
    navbar1, navbar_lang = st.columns([0.92, 0.08])
    with navbar1:
        # Inline CSS for the navbar's appearance
        navbar_style = """
        <style>
        .navbar { display: flex; flex-direction: row; justify-content: space-between; align-items: center; padding: 1rem 2rem; background-color: #E1EDFA; border-radius: 5px; }
        .navbar-title-logo { display: flex; align-items: center; }
        .app-name { font-size: 1.5rem; font-weight: bold; margin-left: 1rem; padding: 0.5rem 0; color: #263557; }
        .navbar-buttons a { text-decoration: none; color: white; }
        .button { color: white; background-color: #799BE6; border: none; border-radius: 4px; padding: 5px 10px; font-size: 16px; cursor: pointer; }
        </style>
        """
        llm_dashboard_text = "LLM Dashboard" if st.session_state.lang == "en" else "LLMダッシュボード"
        # The HTML structure of the navbar
        navbar_html = f"""
        <div class="navbar">
            <div class="navbar-title-logo">
                <img src="data:image/png;base64,{brand_image}" width="70">
                <h3 class="app-name">{app_name1}</h3>
            </div>
            <div class="navbar-links-buttons">
                <div class="navbar-buttons">
                    <button class="button">
                        <a href="https://apps.onestop.ai/llm-dashboard/" target="_blank">{llm_dashboard_text}</a>
                    </button>
                </div>
            </div>
        </div>
        """
        st.markdown(navbar_html + navbar_style, unsafe_allow_html=True)

    with navbar_lang:
        # The language selection dropdown
        st.selectbox("Language", ("en", "ja"), key="lang", on_change=session_state_lang_change_callback, label_visibility="collapsed")

    # JavaScript to fine-tune the navbar's appearance within Streamlit's layout
    components.html("""
    <script>
        var navbar = window.parent.document.querySelector('div[data-testid="stHorizontalBlock"]');
        if (navbar) {
            navbar.style.backgroundColor = '#E1EDFA';
            navbar.style.gap = 0;
            var selectbox = navbar.children[1];
            if (selectbox) { selectbox.style.padding = '1.5rem 0.5rem'; }
        }
    </script>
    """, height=0)

# =================================================================================================
# SECTION 3: MAIN APP LAYOUT AND NAVIGATION
# =================================================================================================
# Display the navbar at the top of the page
navbar()

# Initialize session state for the menu if it doesn't already exist
if "option_menu" not in st.session_state:
    st.session_state.option_menu = _gettext("Overview")

# This logic allows the "Try Demo" button on the homepage to switch the tab
if st.session_state.get("demo_button", False):
    st.session_state.option_menu = _gettext("Demo")
    st.session_state["demo_button"] = False # Reset the button state to prevent looping

# Create the main navigation menu (tabs) using streamlit_option_menu
selected_tab = option_menu(
    None, [_gettext("Overview"), _gettext("Demo")],
    icons=["house-fill", "camera-fill"],
    key="option_menu",
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0.01", "background-color": "#E1EDFA00"},
        "nav-link": {"font-size": "15px", "color": "grey", "text-align": "center", "margin": "0px", "--hover-color": "#E1EDFA"},
        "nav-link-selected": {"background-color": "#789BE600", "color": "#789BE6"},
    }
)

# --- Page Routing Logic ---
# Based on the selected tab, call the appropriate function to render the page content.
if st.session_state.option_menu == _gettext("Overview"):
    # If "Overview" is selected, call the function from homepage.py
    homepage_v3(_gettext)
    custom_footer(_gettext)
elif st.session_state.option_menu == _gettext("Demo"):
    # If "Demo" is selected, call the function from dashboard.py
    demo_dashboard(_gettext)

