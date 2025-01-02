import streamlit as st
from streamlit_option_menu import option_menu
from pages import home, about, login, register

st.set_page_config(page_title="ID Text Extraction", layout="centered")

# Create a top navigation bar
selected = option_menu(
    menu_title=None,  # required
    options=["Home", "About", "Register", "Login"],  # required
    icons=["house", "info-circle", "person-plus", "box-arrow-in-right"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="horizontal",
)

if selected == "Home":
    home.show()
elif selected == "About":
    about.show()
elif selected == "Register":
    register.show()
elif selected == "Login":
    login.show()