import streamlit as st
from auth.authenthication import setup_authenticator

def create_login_panel(_gettext):
    st.info(_gettext('Login to use chat functionality'))

    # ---------- Authentication ------------------------------
    authenticator = setup_authenticator()
    authenticator.login(location='main')

    # get login info from session_state
    name = st.session_state.get("name")
    authentication_status = st.session_state.get("authentication_status")
    username = st.session_state.get("username")

    if authentication_status:    
        authenticator.logout('Logout', location='main')
        
        # Handle translation for 'Login Successful !!'
        try:
            login_success_message = _gettext('Login Successful !!')
            if st.session_state.lang == 'ja' and login_success_message == 'Login Successful !!':
                login_success_message = 'ログイン成功 !!'
        except Exception:
            if st.session_state.lang == 'ja':
                login_success_message = 'ログイン成功 !!'
            else:
                login_success_message = 'Login Successful !!'
        
        st.success(login_success_message)
        
        # Handle translation for 'Welcome *{name}*'
        try:
            welcome_message = _gettext(f'Welcome *{name}*')
            if st.session_state.lang == 'ja' and welcome_message == f'Welcome *{name}*':
                welcome_message = f'ようこそ *{name}*'
        except Exception:
            if st.session_state.lang == 'ja':
                welcome_message = f'ようこそ *{name}*'
            else:
                welcome_message = f'Welcome *{name}*'
        
        st.success(welcome_message)

    # check authentication   
    if authentication_status == False:
        st.error(_gettext('Username/password is incorrect'))
        
    if authentication_status is None:
        st.error(_gettext("New User? For credentials, Contact info@algoanalytics.com"))
