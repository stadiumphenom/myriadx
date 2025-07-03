# dreamloopbuilder.py
# Full Myriad ⇄ Stable Diffusion recursive loop generator

import os
import time
from sdtomyriad import analyze_image
from myriadsdbridge import buildsdprompt, exporttosd
from engines import engineego, engineecho, enginedrift, engineform
from myriadsdmock import simulate_sd_render

ENGINE_MAP = {
    "ego-loss": engine_ego.MyriadEgoEngine,
    "ghost-calm": engine_echo.MyriadEchoEngine,
    "chaos": engine_drift.MyriadDriftEngine,
    "structured": engine_form.MyriadFormEngine
}

def run_sim(params, sim_count=10000):
    emotion_key = params.get("emotion", "ego-loss")
    drift = params.get("entropy", 0.1)
    EngineClass = ENGINE_MAP.get(emotion_key, engine_ego.MyriadEgoEngine)
    engine = EngineClass(emotion=emotion_key, sim_count=sim_count, drift_factor=drift)
    return engine.generate_frame_data()

def loop_once(input_image_path, loop_id="001"):
    print(f"[Loop {loop_id}] Starting from image: {input_image_path}")
    inferred = analyze_image(input_image_path)
    sim_data = run_sim(inferred)
    prompt = build_sd_prompt(sim_data, emotion=inferred["emotion"])
    simulate_sd_render(prompt, output_path=f"outputs/frame_{loop_id}.png")
    print(f"[Loop {loop_id}] Complete.")
    return prompt

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Dream Loop Builder")
    parser.add_argument("--image", type=str, required=True, help="Initial image")
    parser.add_argument("--cycles", type=int, default=1, help="Number of dream loops")
    args = parser.parse_args()

    image = args.image
    for i in range(args.cycles):
        print(f"\n🌀 Dream Cycle {i+1}/{args.cycles}")
        prompt = loop_once(image, loop_id=str(i+1).zfill(3))
        time.sleep(1)
