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
                    id_data = response.json()
                    st.success("Text extracted successfully!")
                    st.write("### Extracted Information")
                    st.write(f"**ID Number:** {id_data['id_number']}")
                    st.write(f"**Full Name (Latin):** {id_data['full_name_latin']}")
                    st.write(f"**Birth Date:** {id_data['birth_date']}")
                    st.write(f"**Expiry Date:** {id_data['expiry_date']}")
                else:
                    st.error("Failed to extract text from the image.")

if __name__ == "__main__":
    show()