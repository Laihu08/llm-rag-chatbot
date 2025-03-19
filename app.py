import streamlit as st
import subprocess
import openai
from streamlit_chat import message

# Streamlit UI
st.title("LLM RAG Chatbot (OpenAI / Ollama)")

# Model Selection
model_option = st.selectbox("Choose AI Model:", ["OpenAI GPT", "Ollama (Local)"])

# 👉 ADD THIS SECTION RIGHT HERE 👈
if model_option == "Ollama (Local)":
    st.warning("⚠️ **Make sure to run `ollama serve` in your terminal before using this option!**")


# OpenAI API Key (Optional, only needed for OpenAI users)
if model_option == "OpenAI GPT":
    openai_api_key = st.text_input("Enter your OpenAI API Key:", type="password")
    if openai_api_key:
        openai.api_key = openai_api_key

# Function to generate responses using OpenAI
def generate_openai_response(prompt):
    if not openai.api_key:
        return "❌ OpenAI API key is required!"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Function to generate responses using Ollama (Mistral)
def generate_ollama_response(prompt):
    try:
        response = subprocess.run(
            ["ollama", "run", "mistral", prompt],
            capture_output=True,
            text=True
        )
        return response.stdout
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Chat Input
user_input = st.text_input("You: ")

if user_input:
    if model_option == "OpenAI GPT":
        bot_response = generate_openai_response(user_input)
    else:
        bot_response = generate_ollama_response(user_input)

    # Display chat messages
    message(user_input, is_user=True)
    message(bot_response)
