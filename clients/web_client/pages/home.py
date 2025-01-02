import streamlit as st

def show():
    st.title("Welcome to the Home Page")
    st.write("### Your ID Text Extraction Tool")

    st.write("""
    This application allows you to extract text from Moroccan ID cards efficiently. 
    It provides user-friendly features for registration, login, and profile management.
    """)

    st.image("https://example.com/image.png", caption="Your ID Extraction in Action")  # Replace with an actual image URL

    st.write("### Getting Started")
    st.write("1. **Register** for an account.")
    st.write("2. **Log in** to your account.")
    st.write("3. **Upload** your ID card for text extraction.")