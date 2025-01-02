# filepath: /C:/Users/Namous Mohamed/Desktop/ocr-microservices/clients/web_client/main.py
import streamlit as st
from streamlit_option_menu import option_menu
from pages import home, about, login, register

st.set_page_config(page_title="ID Text Extraction", layout="centered")

if "selected_page" not in st.session_state:
    st.session_state["selected_page"] = "Home"

# Create a top navigation bar
selected = option_menu(
    menu_title=None,  # required
    options=["Home", "About", "Register", "Login"],  # required
    icons=["house", "info-circle", "person-plus", "box-arrow-in-right"],  # optional
    menu_icon="cast",  # optional
    default_index=["Home", "About", "Register", "Login"].index(st.session_state["selected_page"]),  # optional
    orientation="horizontal",
)

st.session_state["selected_page"] = selected

if selected == "Home":
    home.show()
elif selected == "About":
    about.show()
elif selected == "Register":
    register.show()
elif selected == "Login":
    login.show()