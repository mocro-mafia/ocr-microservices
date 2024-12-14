FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the required Python packages from the requirements.txt file
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Copy your Streamlit app code into the container
COPY intrface.py .

# Expose the port that Streamlit will run on
EXPOSE 8501

# Set the command to run Streamlit on container startup
ENTRYPOINT ["streamlit", "run", "intrface.py", "--server.port=8501", "--server.address=0.0.0.0"]
