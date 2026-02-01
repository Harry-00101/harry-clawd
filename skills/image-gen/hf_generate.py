#!/usr/bin/env python3
"""
Hugging Face Image Generation (Free Inference API!)

No GPU needed - uses HF's free inference API.
"""

import os
import sys
from huggingface_hub import InferenceClient

HF_TOKEN = os.environ.get("HF_TOKEN", "")

def generate(prompt, model="stabilityai/stable-diffusion-xl-base-1.0"):
    """Generate image using Hugging Face Inference API."""
    if not HF_TOKEN:
        return {"error": "HF_TOKEN not set. Get free token from: https://huggingface.co/settings/tokens"}
    
    client = InferenceClient(token=HF_TOKEN)
    
    try:
        image = client.text_to_image(prompt, model=model)
        return {"image": image, "prompt": prompt}
    except Exception as e:
        return {"error": str(e)}

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 hf_generate.py <prompt>")
        print("Example: python3 hf_generate.py 'A robot girl with silver hair'")
        print("\nSet HF_TOKEN first:")
        print("  export HF_TOKEN='your-huggingface-token'")
        return
    
    prompt = " ".join(sys.argv[1:])
    print(f"🎨 Generating: {prompt[:50]}...")
    
    result = generate(prompt)
    
    if "error" in result:
        print(f"❌ {result['error']}")
    elif "image" in result:
        filename = f"hf_generated_{len(prompt)[:10]}.png"
        result["image"].save(filename)
        print(f"✅ Saved: {filename}")

if __name__ == "__main__":
    main()
