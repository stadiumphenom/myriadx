from stabilitydreamloop import dreamloop_generate
import streamlit as st
import requests
import base64
from PIL import Image
from io import BytesIO
import os

# Stability AI API Key from environment variable
API_KEY = os.getenv("sk-Vd5S5SG1mZVlyJjySkhVW5ZcbarHfKEAtITgj5gQszKQO5aG")
API_URL = "https://api.stability.ai/v2beta/stable-image/generate/sd3"

st.set_page_config(page_title="Dreamloop Lite", layout="centered")
st.title("🎨 Dreamloop Lite - Powered by Stability AI")

if not API_KEY:
    st.error("API key not found. Please set the STABILITY_API_KEY environment variable.")
else:
    prompt = st.text_input("Enter a prompt:", "a futuristic cityscape at sunset")
    uploaded_file = st.file_uploader("(Optional) Upload an image to guide the generation", type=["jpg", "jpeg", "png"])

    if st.button("Generate"):
    if not prompt:
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating image..."):
            try:
                image_bytes = uploaded_file.read() if uploaded_file else None
                result = dreamloop_generate(prompt, image_bytes)
                img = Image.open(BytesIO(result))
                st.image(img)
                st.download_button("Download", data=result, file_name="dreamloop.png")
            except Exception as e:
                st.error(f"Error: {e}")
