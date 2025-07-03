# sd_to_myriad1.py
# Analyze image and convert to emotional simulation input

from PIL import Image
import random

def analyze_image(image_path):
    try:
        img = Image.open(image_path).convert("RGB")
        width, height = img.size
        entropy = (width * height) / 1000000.0
    except Exception as e:
        print(f"[Analyze] Failed to load image: {e}")
        entropy = 0.1

    emotions = ["ego-loss", "chaos", "structured", "ghost-calm"]
    inferred_emotion = random.choice(emotions)

    return {
        "emotion": inferred_emotion,
        "entropy": round(min(entropy, 1.0), 2),
        "keywords": ["flow", "fracture", "echo", "light ripple"],
        "intensity": round(random.uniform(0.5, 1.0), 2)
    }
