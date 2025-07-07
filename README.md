 Mental State Evaluation Tool
This is a Streamlit web app that uses various Large Language Models (LLMs) from Hugging Face to evaluate and respond to users' mental state descriptions. The app allows users to describe how they’re feeling, choose the severity, select emotions, and get a meaningful response from a selected AI model.

🚀 Features
🤖 Model Options: Choose between distilgpt2, bart, gpt-neo, and flan-t5

🧠 Mental State Input: Describe your feelings through a text area

🌡️ Severity Slider: Rate your mental state from 1 to 10

🎭 Emotions Multiselect: Select multiple emotions you're experiencing

💬 AI Response: Get a generated response from the chosen model via Hugging Face API

🛠️ Tech Stack
Python 🐍

Streamlit for web interface

Hugging Face Inference API for LLMs

📦 Installation & Setup
Clone the Repository:


git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Install Required Libraries:


pip install streamlit huggingface_hub
Add Your Hugging Face API Key:

Open app.py

Replace the api_key variable with your Hugging Face token:


api_key = "your_huggingface_api_key"
Run the App:


streamlit run app.py
(Optional) Deploy via LocalTunnel or ngrok on Colab
Use LocalTunnel to expose your Streamlit app externally:


!pip install streamlit
!npm install -g localtunnel
!streamlit run app.py & npx localtunnel --port 8501


