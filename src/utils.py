import streamlit as st
import extra_streamlit_components as stx
import datetime

def check_password():
    """Returns `True` if the user had a correct password."""
    
    # Initialize cookie manager
    cookie_manager = stx.CookieManager(key="auth_cookie_manager")
    
    # Check if user is already authenticated via cookie
    if cookie_manager.get("authenticated") == "true":
        return True

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if "passcode" not in st.secrets or "password" not in st.secrets["passcode"]:
            st.error("Passcode not configured. Please check .streamlit/secrets.toml")
            st.session_state["password_correct"] = False
            return

        if st.session_state["password"] == st.secrets["passcode"]["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
            # Set cookie to expire in 1 day
            expires = datetime.datetime.now() + datetime.timedelta(days=1)
            cookie_manager.set("authenticated", "true", expires_at=expires)
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password incorrect, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True
