import streamlit as st
from PIL import Image

def local_css():
    st.markdown("""
        <style>
        /* General Styling */
        body {
            background-color: #121212;  /* Dark mode background */
            color: #e0e0e0;  /* Light text color for readability */
            font-family: 'Arial', sans-serif;
        }
        h1, h2, h3, h4 {
            color: #ffffff; /* White titles */
        }
        p {
            color: #b0bec5; /* Light gray text */
        }

        /* Hero Section */
        .hero-container {
            padding: 3rem;
            background: linear-gradient(135deg, #1f6feb 0%, rgba(255, 255, 255, 0.1) 100%);
            border-radius: 20px;
            margin-bottom: 2rem;
            text-align: center;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
            animation: fadeIn 2s ease-in-out;
        }
        .big-title {
            font-size: 3.5rem;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 1rem;
        }
        .subtitle {
            font-size: 1.3rem;
            color: #b0bec5;
            margin-bottom: 2rem;
        }

        /* Features Section */
        .feature-card {
            background: rgba(255, 255, 255, 0.05);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
            transition: transform 0.3s, box-shadow 0.3s;
            margin-bottom: 1rem;
            text-align: center;
        }
        .feature-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 25px rgba(0, 0, 0, 0.5);
        }
        .icon-text {
            font-size: 1.5rem;
            color: #1f6feb;
            font-weight: bold;
            margin-bottom: 1rem;
        }

        /* How It Works Section */
        img {
            border-radius: 15px;
            transition: transform 0.3s ease-in-out;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        }
        img:hover {
            transform: scale(1.05);
        }

        /* CTA Section */
        .cta-card {
            background: #1f6feb;
            color: white;
            padding: 3rem;
            border-radius: 15px;
            text-align: center;
            margin-top: 2rem;
            animation: fadeInUp 1s ease-in-out;
        }
        .cta-card h2 {
            margin-bottom: 1rem;
        }
        .cta-card p {
            margin-bottom: 1.5rem;
        }
        .cta-button {
            background-color: #ffffff;
            color: #1f6feb;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 1rem;
            font-weight: bold;
            cursor: pointer;
            transition: background-color 0.3s ease, color 0.3s ease;
        }
        .cta-button:hover {
            background-color: #e0e0e0;
            color: #121212;
        }

        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        </style>
    """, unsafe_allow_html=True)

def show():
    local_css()
    
    # Hero Section
    st.markdown("""
        <div class='hero-container'>
            <div class='big-title'>ID Text Extraction Service 🔍</div>
            <div class='subtitle'>Quickly extract and process information from Moroccan ID cards using advanced OCR technology.</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Features Section
    st.markdown("### Features")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class='feature-card'>
                <div class='icon-text'>🚀 Fast Processing</div>
                <p>Extract text from ID cards in seconds using state-of-the-art OCR.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class='feature-card'>
                <div class='icon-text'>🔒 Secure</div>
                <p>Your data is encrypted and securely processed with advanced security measures.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
            <div class='feature-card'>
                <div class='icon-text'>📊 Accurate</div>
                <p>High accuracy text extraction with advanced AI models.</p>
            </div>
        """, unsafe_allow_html=True)
    
    # How It Works Section
    st.markdown("### How It Works")
    steps_col1, steps_col2, steps_col3 = st.columns(3)
    
    with steps_col1:
        st.image("https://repository-images.githubusercontent.com/229240000/2b1bba00-eae1-11ea-8b31-ea57fe8a3f95", caption="1. Upload ID Card")
    with steps_col2:
        st.image("https://media.istockphoto.com/id/1033799364/vector/workflow-process-icon-in-flat-style-gear-cog-wheel-with-arrows-vector-illustration-on-white.jpg?s=612x612&w=0&k=20&c=w0GBtP-wdqzKXr-H2tEpXZleFuCVhNIeg-d4sypTTZ0=", caption="2. Process Image")
    with steps_col3:
        st.image("https://cdn.iconscout.com/icon/free/png-256/free-result-icon-download-in-svg-png-gif-file-formats--clipboard-check-mark-checklist-web-pack-seo-icons-2695735.png", caption="3. Get Results")
    
    # CTA Section
    st.markdown("""
        <div class='cta-card'>
            <h2>Ready to Start?</h2>
            <p>Upload your ID card and get instant results.</p>
            <button class='cta-button'>Upload Now</button>
        </div>
    """, unsafe_allow_html=True)
    
if __name__ == "__main__":
    show()
