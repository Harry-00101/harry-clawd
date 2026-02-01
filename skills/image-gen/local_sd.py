#!/usr/bin/env python3
"""
Local Stable Diffusion Image Generation (CPU)
Will be slow but FREE!
"""

import torch
from diffusers import StableDiffusionPipeline
import os

# Save prompt for Harry-001
PROMPT = """White robotic girl with silver bob hair, large white 
headphones with glowing blue circular lights, bright blue eyes, 
white mechanical armor plating, visible black joints at shoulders 
and elbows, friendly smiling expression, anime style illustration, 
soft warm lighting, cozy cafe background with wooden shelves"""

def generate(prompt=PROMPT, model_id="runwayml/stable-diffusion-v1-5"):
    """Generate image using local CPU."""
    print(f"🎨 Generating image...")
    print(f"Model: {model_id}")
    
    # Load model
    print("Loading model (first time takes a while)...")
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float32  # CPU = float32
    )
    pipe = pipe.to("cpu")  # Use CPU
    
    # Generate
    print("Generating (this may take a few minutes on CPU)...")
    image = pipe(prompt).images[0]
    
    # Save
    filename = "/root/clawd/harry001_local_sd.png"
    image.save(filename)
    print(f"✅ Saved: {filename}")
    return filename

if __name__ == "__main__":
    generate()
