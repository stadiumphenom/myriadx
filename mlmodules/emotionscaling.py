# emotionscaling.py
# Normalize and scale inferred emotional signals for sim input

def scale_emotion_features(raw_data):
    """
    Convert raw ML inference data into usable simulation weights.
    """
    return {
        "entropy": round(min(max(raw_data.get("entropy", 0.1), 0.0), 1.0), 2),
        "ghost": round(raw_data.get("ghost", 0.0) * 1.5, 2),
        "intensity": round(0.6 + raw_data.get("glow", 0.0), 2),
        "keywords": ["echo pulse", "fluid light", "residual motion"]
    }

