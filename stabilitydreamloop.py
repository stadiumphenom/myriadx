# stabilitydreamloop.py
import requests
import base64
from io import BytesIO
import os

def dreamloop_generate(prompt, image_bytes=None, use_sdxl=True):
    API_KEY = os.getenv("key")
    API_URL = "https://api.stability.ai/v2beta/stable-image/generate/core"

    if not API_KEY:
        raise ValueError("Stability API key not found in environment.")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": prompt,
        "output_format": "png",
        "model": "stable-diffusion-xl-beta" if use_sdxl else "stable-diffusion-v1-5"
    }

    if image_bytes:
        payload["init_image"] = base64.b64encode(image_bytes).decode("utf-8")
        payload["mode"] = "image-to-image"

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        output = response.json()
        return base64.b64decode(output["image"])
    else:
        raise RuntimeError(f"Generation failed: {response.text}")
