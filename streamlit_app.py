import streamlit as st
import requests

# Access the Hugging Face API key from Streamlit secrets
api_key = st.secrets["huggingface"]["api_key"]

# Base URL for Hugging Face Inference API
endpoint = "https://api-inference.huggingface.co/models/{model_id}"

# Set headers with the API key
headers = {"Authorization": f"Bearer {api_key}"}

# Custom CSS for a subtle, professional design
st.markdown("""
    <style>
        body {
            background-color: #1E1E2F;
            color: #CFCFCF;
            font-family: 'Helvetica', sans-serif;
        }
        .stTitle {
            color: #FFD700;
            font-size: 34px;
            font-weight: bold;
            text-align: center;
        }
        .stCaption {
            color: #A9A9A9;
            font-size: 15px;
            font-style: italic;
            text-align: center;
        }
        .stSelectbox, .stTextInput input {
            background-color: #2C2C3D;
            color: #E0E0E0;
            border: 1px solid #FFD700;
            border-radius: 10px;
            padding: 10px;
        }
        .stMarkdown {
            color: #CFCFCF;
            font-size: 16px;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 12px;
            padding: 8px 20px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
        }
        .stButton button:hover {
            background-color: #45A049;
        }
    </style>
""", unsafe_allow_html=True)

# Set the title and caption
st.title("🧠 Mental State Evaluation Tool 🌿✨")
st.caption("Explore your mental well-being with the power of AI. 🌟 Let's begin the journey! 🛤️")

# Map models to Hugging Face API IDs

model_mapping = {
    'distilgpt2 🧩': "meta-llama/Llama-3.2-1B-Instruct",
    'bart 📖': "google/gemma-1.1-2b-it",
    'flan-t5 🌟': "tiiuae/falcon-7b-instruct",
    'gpt-neo 💡': 'google/gemma-1.1-2b-it'
}

selected_model = st.selectbox("Select Model 🔍", list(models.keys()))
selected_model_id = models[selected_model]

# Query input box
user_query = st.text_input("Type your question here 💬:")

# Handle user input and generate a response
if user_query:
    try:
        # Prepare the payload
        payload = {"inputs": user_query}

        # Send the request to Hugging Face API
        response = requests.post(
            endpoint.format(model_id=selected_model_id),
            headers=headers,
            json=payload
        )

        # Process the response
        if response.status_code == 200:
            result = response.json()
            generated_text = result.get("generated_text", "No response generated.")
            st.markdown(f"### *{selected_model} Response:* 🧑‍⚕️✨", unsafe_allow_html=True)
            st.markdown(f"<div class='stMarkdown'>{generated_text}</div>", unsafe_allow_html=True)
        else:
            st.error(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        st.error(f"⚠️ An error occurred: {e} 😔")
