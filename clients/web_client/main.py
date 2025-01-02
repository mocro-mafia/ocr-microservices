import streamlit as st
from streamlit_option_menu import option_menu
from pages import home, about, login, register, profile, id_extraction

st.set_page_config(page_title="ID Text Extraction", layout="centered")

if "selected_page" not in st.session_state:
    st.session_state["selected_page"] = "Home"

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# Check query params to update session state
query_params = st.query_params
if "logged_in" in query_params:
    st.session_state["logged_in"] = query_params["logged_in"] == "True"
if "selected_page" in query_params:
    st.session_state["selected_page"] = query_params["selected_page"][0]

# Define menu options based on login status
if st.session_state["logged_in"]:
    menu_options = ["Home", "About", "Profile", "ID Extraction", "Logout"]
    menu_icons = ["house", "info-circle", "person", "file-earmark-text", "box-arrow-right"]
else:
    menu_options = ["Home", "About", "Register", "Login"]
    menu_icons = ["house", "info-circle", "person-plus", "box-arrow-in-right"]

# Ensure the selected page is valid
if st.session_state["selected_page"] not in menu_options:
    st.session_state["selected_page"] = "Home"

# Create a top navigation bar
selected = option_menu(
    menu_title=None,  # required
    options=menu_options,  # required
    icons=menu_icons,  # optional
    menu_icon="cast",  # optional
    default_index=menu_options.index(st.session_state["selected_page"]),  # optional
    orientation="horizontal",
)

st.session_state["selected_page"] = selected

# Logout functionality
if selected == "Logout":
    st.session_state["logged_in"] = False
    st.session_state["selected_page"] = "Home"
    st.experimental_rerun()  # Use st.experimental_rerun to refresh the app

# Route to the selected page
if selected == "Home":
    home.show()
elif selected == "About":
    about.show()
elif selected == "Register":
    register.show()
elif selected == "Login":
    login.show()
elif selected == "Profile":
    profile.show()
elif selected == "ID Extraction":
    id_extraction.show()