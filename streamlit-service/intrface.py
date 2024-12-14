import streamlit as st
import pandas as pd
import requests


st.title("OCR App")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post("http://fastapi:8000/ocr/", files=files)

    if response.status_code == 200:
        st.subheader("Extracted Text:")
        st.text(response.json().get("text"))
    else:
        st.error("Error performing OCR")