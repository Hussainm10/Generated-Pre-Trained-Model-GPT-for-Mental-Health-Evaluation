#Following is the main code.

%%writefile app.py

import streamlit as st
from huggingface_hub import InferenceClient

# Your Hugging Face API key (replace this with your actual key)
api_key = "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"  # Replace with your API key

# Initialize the Inference Client with the API key
client = InferenceClient(token=api_key)

# Custom CSS for a subtle, professional design
st.markdown("""
    <style>
        body {
            background-color: #1E1E2F;  /* Soft dark background */
            color: #CFCFCF;  /* Light gray text for contrast */
            font-family: 'Helvetica', sans-serif;  /* Clean, modern font */
        }
        .stTitle {
            color: #FFD700;  /* Golden text for the title */
            font-size: 34px;
            font-weight: bold;
            text-align: center;
        }
        .stCaption {
            color: #A9A9A9;  /* Subtle gray for captions */
            font-size: 15px;
            font-style: italic;
            text-align: center;
        }
        .stSelectbox, .stTextInput input {
            background-color: #2C2C3D;  /* Soft dark gray background for inputs */
            color: #E0E0E0;  /* Light text inside inputs */
            border: 1px solid #FFD700;  /* Golden border for highlighting */
            border-radius: 10px;
            padding: 10px;
        }
        .stMarkdown {
            color: #CFCFCF;  /* Light gray for markdown text */
            font-size: 16px;
        }
        .stButton button {
            background-color: #4CAF50;  /* Soft green for buttons */
            color: white;
            border-radius: 12px;
            padding: 8px 20px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
        }
        .stButton button:hover {
            background-color: #45A049;  /* Slightly brighter green on hover */
        }
    </style>
""", unsafe_allow_html=True)

# Set the title and caption with additional emojis
st.title("🧠 Mental State Evaluation Tool 🌿✨")
st.caption("Explore your mental well-being with the power of AI. 🌟 Let's begin the journey! 🛤️")

# Model selection with emojis
models = ['distilgpt2 🧩', 'bart 📖', 'gpt-neo 💡', 'flan-t5 🌟']
selected_model = st.selectbox('Select Model 🔍', models)

# Query input box with emoji prompt
user_query = st.text_input('Type your question here 💬:')

# Map models to Hugging Face API IDs
model_mapping = {
    'distilgpt2 🧩': "meta-llama/Llama-3.2-1B-Instruct",
    'bart 📖': "google/gemma-1.1-2b-it",
    'flan-t5 🌟': "tiiuae/falcon-7b-instruct",
    'gpt-neo 💡': 'google/gemma-1.1-2b-it'
}
selected_model_id = model_mapping.get(selected_model, "meta-llama/Llama-3.2-1B-Instruct")

# Handle user input and generate a response
if user_query:
    try:
        response = client.chat.completions.create(
            model=selected_model_id,
            messages=[{"role": "user", "content": user_query}],
            max_tokens=600
        )
        # Extract and display the model's response
        model_reply = response["choices"][0]["message"]["content"]
        st.markdown(f"### *{selected_model} Response:* 🧑‍⚕️✨", unsafe_allow_html=True)
        st.markdown(f"<div class='stMarkdown'>{model_reply}</div>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"⚠️ An error occurred: {e} 😔")
