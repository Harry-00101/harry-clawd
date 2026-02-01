#!/usr/bin/env python3
"""
AI Image Generation for Harry-001

Supports: Replicate, OpenAI DALL-E
"""

import os
import sys

def generate_with_replicate(prompt, model="black-forest-labs/flux-schnell"):
    """Generate image using Replicate API."""
    import replicate
    
    api_token = os.environ.get("REPLICATE_API_TOKEN")
    if not api_token:
        return {"error": "REPLICATE_API_TOKEN not set"}
    
    output = replicate.run(
        model,
        input={
            "prompt": prompt,
            "width": 1024,
            "height": 1024,
            "num_outputs": 1
        }
    )
    return {"url": output[0]}

def generate_with_dalle(prompt, model="dall-e-3"):
    """Generate image using OpenAI DALL-E."""
    from openai import OpenAI
    
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return {"error": "OPENAI_API_KEY not set"}
    
    client = OpenAI(api_key=api_key)
    
    response = client.images.generate(
        model=model,
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    
    return {"url": response.data[0].url}

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 generate.py <prompt>")
        print("Example: python3 generate.py 'A robot girl with silver hair'")
        return
    
    prompt = " ".join(sys.argv[1:])
    print(f"Generating: {prompt}")
    
    # Try Replicate first
    result = generate_with_replicate(prompt)
    if "error" in result and "token" in result["error"].lower():
        # Try DALL-E
        result = generate_with_dalle(prompt)
    
    if "url" in result:
        print(f"✅ Generated: {result['url']}")
    else:
        print(f"❌ Error: {result.get('error', 'Unknown error')}")

if __name__ == "__main__":
    main()
