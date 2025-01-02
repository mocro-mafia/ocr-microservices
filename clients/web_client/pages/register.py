# filepath: /C:/Users/Namous Mohamed/Desktop/ocr-microservices/clients/web_client/pages/register.py
import streamlit as st
import requests
import re

def show():
    st.title("Register")
    register_email = st.text_input("Email", key="register_email")
    register_full_name = st.text_input("Full Name", key="register_full_name")
    register_password = st.text_input("Password", type="password", key="register_password")

    if st.button("Register"):
        if not register_email or not register_full_name or not register_password:
            st.error("All fields are required")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", register_email):
            st.error("Invalid email address")
            return

        if len(register_password) < 8:
            st.error("Password must be at least 8 characters long")
            return

        response = requests.post("http://127.0.0.1:8000/register", json={
            "email": register_email,
            "full_name": register_full_name,
            "password": register_password
        })
        if response.status_code == 200:
            st.success("Registration successful")
            st.session_state["selected_page"] = "Login"
        else:
            st.error(response.json().get("detail"))