#!/usr/bin/env python3
"""Auto-retry image generation when resources available"""

import os
import time
from pathlib import Path

def check_dependencies():
    """Check if we can generate images."""
    deps = []
    
    # Check torch
    try:
        import torch
        deps.append(f"torch: ✅ {torch.__version__}")
    except:
        deps.append("torch: ❌ Not installed")
    
    # Check diffusers
    try:
        from diffusers import StableDiffusionPipeline
        deps.append("diffusers: ✅")
    except:
        deps.append("diffusers: ❌ Not installed")
    
    # Check HF token
    hf_path = Path('/root/clawd/.config/huggingface.json')
    if hf_path.exists():
        deps.append("HF Token: ✅")
    else:
        deps.append("HF Token: ❌ Missing")
    
    return deps

def main():
    print("🎨 IMAGE GENERATION READINESS CHECK")
    print("="*40)
    
    deps = check_dependencies()
    for d in deps:
        print(f"   {d}")
    
    ready = all("✅" in d for d in deps if "Token" in d or "diffusers" in d)
    
    print("\n" + "="*40)
    if ready:
        print("🚀 READY TO GENERATE!")
    else:
        print("⏳ Waiting for dependencies...")
    
    return ready

if __name__ == "__main__":
    main()
