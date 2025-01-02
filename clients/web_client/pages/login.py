# filepath: /C:/Users/Namous Mohamed/Desktop/ocr-microservices/clients/web_client/pages/login.py
import streamlit as st
import requests
import re

def show():
    st.title("Login")
    login_email = st.text_input("Email", key="login_email")
    login_password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login"):
        if not login_email or not login_password:
            st.error("All fields are required")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", login_email):
            st.error("Invalid email address")
            return

        if len(login_password) < 8:
            st.error("Password must be at least 8 characters long")
            return

        response = requests.post("http://127.0.0.1:8000/login", json={
            "email": login_email,
            "password": login_password
        })
        if response.status_code == 200:
            st.success("Login successful")
            token = response.json().get("access_token")
            st.write(f"Access Token: {token}")
        else:
            st.error(response.json().get("detail"))