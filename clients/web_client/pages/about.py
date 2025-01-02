import streamlit as st

def local_css():
    st.markdown("""
        <style>
        body {
            background-color: #121212;  /* Dark background for dark mode */
            color: #e0e0e0;  /* Light text color for better readability */
        }
        .hero-container {
            padding: 2rem;
            background: linear-gradient(135deg, rgba(31, 110, 235, 0.2) 0%, rgba(255, 255, 255, 0.1) 100%);
            border-radius: 20px;
            text-align: center;
            margin-bottom: 2rem;
        }
        .big-title {
            font-size: 2.5rem;
            font-weight: 700;
            color: #ffffff; /* White title for contrast */
            margin-bottom: 1rem;
        }
        .subtitle {
            font-size: 1.5rem;
            color: #b0bec5; /* Light gray subtitle */
            margin-bottom: 2rem;
        }
        .feature-card {
            background: rgba(255, 255, 255, 0.1); /* Semi-transparent white for dark mode */
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
            margin: 1rem auto;
            max-width: 600px; /* Centering cards */
        }
        .developer-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 2rem; /* Increased gap between cards */
        }
        .developer-card {
            background: rgba(255, 255, 255, 0.1);
            padding: 1rem;
            border-radius: 15px;
            text-align: center;
            width: 220px; /* Slightly wider cards */
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
            transition: transform 0.3s; /* Smooth hover effect */
        }
        .developer-card:hover {
            transform: translateY(-5px); /* Lift effect on hover */
        }
        .developer-card img {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            margin-bottom: 0.5rem;
        }
        .developer-card h4 {
            color: #ffffff;
            margin-bottom: 0.5rem;
        }
        .developer-card p {
            color: #b0bec5; /* Light gray for roles */
        }
        </style>
    """, unsafe_allow_html=True)

def show():
    local_css()

    # Hero Section
    st.markdown("""
        <div class='hero-container'>
            <div class='big-title'>About Our ID Text Extraction Service</div>
            <div class='subtitle'>Harnessing the Power of OCR Technology</div>
        </div>
    """, unsafe_allow_html=True)

    # Description Section
    st.write("""
    Our service allows you to extract text from ID cards quickly and accurately using advanced Optical Character Recognition (OCR) techniques. 
    With our user-friendly interface, you can upload images of ID cards and receive extracted text in seconds.
    """)

    # Features Section
    st.markdown("### Key Features")

    features = [
        "🚀 **Fast Processing** - Extract text from ID cards in seconds.",
        "🔒 **Secure** - Your data is encrypted and securely processed.",
        "📊 **Accurate** - High accuracy text extraction using advanced AI models.",
        "🌍 **Multi-language Support** - Supports multiple languages for diverse users.",
        "📱 **User-Friendly Interface** - Easy to use for everyone."
    ]

    for feature in features:
        st.markdown(f"<div class='feature-card'>{feature}</div>", unsafe_allow_html=True)

    # Technology Section
    st.markdown("### How It Works")
    st.write("""
    Our OCR technology utilizes machine learning algorithms to recognize and extract text from images. 
    The process involves several steps:
    
    - **Image Preprocessing**: Enhancing image quality for better recognition.
    - **Text Detection**: Identifying areas containing text.
    - **Character Recognition**: Converting detected text into machine-readable format.
    
    This ensures high accuracy and reliability in extracting information from ID cards.
    """)

    # Developers Section
    st.markdown("### Meet the Developers")
    
    developers = [
        {"name": "Developer 1", "img": "https://via.placeholder.com/100", "role": "Frontend Developer"},
        {"name": "Developer 2", "img": "https://via.placeholder.com/100", "role": "Backend Developer"},
        {"name": "Developer 3", "img": "https://via.placeholder.com/100", "role": "AI Specialist"},
        {"name": "Developer 4", "img": "https://via.placeholder.com/100", "role": "UI/UX Designer"},
        {"name": "Developer 5", "img": "https://via.placeholder.com/100", "role": "Data Engineer"},
        {"name": "Developer 6", "img": "https://via.placeholder.com/100", "role": "Project Manager"},
        {"name": "Developer 7", "img": "https://via.placeholder.com/100", "role": "QA Specialist"},
    ]

    st.markdown("<div class='developer-container'>", unsafe_allow_html=True)
    
    for dev in developers:
        st.markdown(f"""
            <div class='developer-card'>
                <img src='{dev['img']}' alt='Developer Photo'>
                <h4>{dev['name']}</h4>
                <p>{dev['role']}</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

    # Conclusion Section
    st.markdown("### Get Started Today!")
    st.write("""
    Experience the convenience of our ID text extraction service. 
    Whether you're a business needing to process IDs or an individual looking to digitize your documents,
    our service is here to help!
    
    Upload your ID card now and see how easy it is to extract information with our advanced technology.
    
    **This project was developed as part of the PFA (Projet de Fin d'Année) at EMSI.**
    """)

if __name__ == "__main__":
    show()
