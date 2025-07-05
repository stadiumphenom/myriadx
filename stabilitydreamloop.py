import os
import base64
import requests

API_KEY = os.getenv("STABILITY_API_KEY")
API_URL = "https://api.stability.ai/v2beta/stable-image/generate/core"

def dreamloop_generate(prompt: str, init_image_bytes: bytes = None):
    if not API_KEY:
        raise ValueError("Missing STABILITY_API_KEY in environment variables.")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": prompt,
        "output_format": "png"
    }

    if init_image_bytes:
        b64_image = base64.b64encode(init_image_bytes).decode("utf-8")
        payload["init_image"] = b64_image
        payload["mode"] = "image-to-image"

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return base64.b64decode(response.json()["image"])
    else:
        raise RuntimeError(f"Stability API failed: {response.text}")
