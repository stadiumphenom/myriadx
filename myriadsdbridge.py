# myriad_sd_bridge.py
# Convert Myriad sim output → Stable Diffusion prompt and export

import os
import json

def build_sd_prompt(sim_data, emotion="ego-loss"):
    keywords = sim_data.get("keywords", [])
    intensity = sim_data.get("intensity", 1.0)
    entropy = sim_data.get("entropy", 0.1)

    base = f"{emotion} dream, ethereal concept art, surrealist textures"
    keyword_str = ", ".join(keywords)
    prompt = f"{base}, {keyword_str}, entropy level {entropy:.2f}, emotional charge {intensity:.2f}"
    return prompt

def export_to_sd(prompt, output_dir="sd_prompts", tag="frame"):
    os.makedirs(output_dir, exist_ok=True)
    index = len(os.listdir(output_dir)) + 1
    out_path = os.path.join(output_dir, f"{tag}_{str(index).zfill(3)}.json")

    with open(out_path, "w") as f:
        json.dump({"prompt": prompt}, f, indent=2)

    print(f"[Export] Prompt saved to {out_path}")
