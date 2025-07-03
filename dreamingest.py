# dream_ingest.py
# Module to download and prepare media input for simulation

import os
import requests

def download_file(url, save_path="ingest/input_media.mp4"):
    response = requests.get(url, stream=True)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"[Ingest] Downloaded file to {save_path}")
    return save_path

def extract_frames(video_path, output_dir="ingest/frames", fps=1):
    os.makedirs(output_dir, exist_ok=True)
    os.system(f"ffmpeg -i {video_path} -vf fps={fps} {output_dir}/frame_%04d.png")
    print(f"[Ingest] Frames saved to {output_dir}")
