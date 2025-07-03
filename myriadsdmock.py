# myriadsdmock.py
# Simulated Stable Diffusion output generator (mock)

import os
from PIL import Image, ImageDraw, ImageFont
import random

def simulate_sd_render(prompt, output_path="outputs/frame_mock.png"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    img = Image.new("RGB", (512, 512), color=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()
    
    wrapped_text = "\n".join(prompt[i:i+40] for i in range(0, len(prompt), 40))
    draw.text((10, 10), wrapped_text, font=font, fill=(255, 255, 255))
    img.save(output_path)
    print(f"[MockSD] Image saved to {output_path}")
