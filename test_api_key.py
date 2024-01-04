import google.generativeai as genai
from pathlib import Path
import gradio as gr
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Configure the GenerativeAI API key using the loaded environment variable
# GCP project: gen-lang-client-0311766049
genai.configure(api_key=os.getenv("GOOGLE_GEN_LANG_API_KEY"))

# Test the API key
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
