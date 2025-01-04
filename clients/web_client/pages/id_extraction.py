# filepath: /C:/Users/Namous Mohamed/Desktop/ocr-microservices/clients/web_client/pages/id_extraction.py
import streamlit as st
import requests
from PIL import Image
import io

def show():
    st.title("ID Extraction")
    st.write("Upload your ID card to extract text.")

    uploaded_file = st.file_uploader("Choose an ID card image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded ID card.', use_container_width=True)

        if st.button("Extract Text"):
            with st.spinner("Extracting text..."):
                response = requests.post(
                    "http://127.0.0.1:8000/process",
                    files={"file": uploaded_file.getvalue()}
                )
                if response.status_code == 200:
                    extracted_text = response.json().get("extracted_text")
                    st.success("Text extracted successfully!")
                    st.write("### Extracted Information")
                    st.write(f"**Extracted Text:** {extracted_text}")
                else:
                    try:
                        error_detail = response.json().get("detail")
                    except requests.exceptions.JSONDecodeError:
                        error_detail = response.text
                    st.error(f"Failed to extract text from the image: {error_detail}")

if __name__ == "__main__":
    show()