# streamlit_app.py
from stabilitydreamloop import dreamloop_generate
import streamlit as st
from PIL import Image
from io import BytesIO
import os
from dotenv import load_dotenv
load_dotenv()  # Load .env file containing STABILITY_API_KEY

st.set_page_config(page_title="Dreamloop Lite", layout="centered")
st.title("🎨 Dreamloop Lite - Powered by Stability AI")

prompt = st.text_input("Enter a prompt:", "a futuristic cityscape at sunset")
uploaded_file = st.file_uploader("Optional: Upload an image to guide generation", type=["jpg", "jpeg", "png"])
use_sdxl = st.checkbox("Use SDXL model (higher quality)", value=True)

if st.button("Generate"):
    if not prompt:
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating image..."):
            try:
                image_bytes = uploaded_file.read() if uploaded_file else None
                result = dreamloop_generate(prompt, image_bytes, use_sdxl=use_sdxl)
                img = Image.open(BytesIO(result))
                st.image(img, caption="Generated Image")
                st.download_button("Download Image", data=result, file_name="dreamloop_output.png")
            except Exception as e:
                st.error(f"Error: {e}")
