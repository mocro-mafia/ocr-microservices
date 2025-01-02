import streamlit as st
import requests

def show():
    st.title("Profile")
    
    token = st.session_state.get("access_token")
    if not token:
        st.error("You need to log in to view this page.")
        return

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get("http://127.0.0.1:8000/user", headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        user_email = user_data["email"]
        user_full_name = user_data["full_name"]
    else:
        st.error("Failed to fetch user details")
        return

    st.write("### Update your profile details below:")

    col1, col2 = st.columns(2)
    with col1:
        new_email = st.text_input("Email", value=user_email, key="profile_email")
    with col2:
        new_full_name = st.text_input("Full Name", value=user_full_name, key="profile_full_name")
    
    new_password = st.text_input("New Password", type="password", key="profile_password")

    if st.button("Update Profile"):
        if not new_email or not new_full_name or not new_password:
            st.error("All fields are required")
            return

        response = requests.put("http://127.0.0.1:8000/update_profile", json={
            "email": new_email,
            "full_name": new_full_name,
            "password": new_password
        }, headers=headers)
        if response.status_code == 200:
            st.success("Profile updated successfully")
        else:
            st.error(response.json().get("detail"))