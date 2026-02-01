# Image Generation Skill

AI image generation using various tools.

## 1. Hugging Face Inference API (FREE!)

**No GPU needed** - Uses HF's free inference API.

```bash
pip install huggingface_hub
export HF_TOKEN="your-huggingface-token"
```

```python
from huggingface_hub import InferenceClient

client = InferenceClient(token="your-token")
image = client.text_to_image("A robot girl with silver hair")
image.save("robot.png")
```

**Get free token:** https://huggingface.co/settings/tokens

## 2. Replicate (Paid, GPU)

```bash
pip install replicate
export REPLICATE_API_TOKEN="your-token"
```

```python
import replicate
output = replicate.run("black-forest-labs/flux-schnell", input={"prompt": "..."})
```

## 3. Local Diffusers (FREE, needs GPU)

```bash
pip install diffusers torch transformers
```

```python
from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe = pipe.to("cuda")
image = pipe("A robot girl").images[0]
image.save("robot.png")
```

## Prompt Structure

```
[Subject] + [Style] + [Lighting] + [Mood] + [Details]
```

Example:
```
White robotic girl, silver bob hair, large headphones with 
blue lights, blue eyes, anime style, soft lighting, cafe background
```

## Usage

```bash
# Hugging Face (free)
export HF_TOKEN="hf_xxxxx"
python3 skills/image-gen/hf_generate.py "A robot girl"

# Replicate (paid)
export REPLICATE_API_TOKEN="r8_xxxxx"
python3 skills/image-gen/generate.py "A robot girl"
```

## Resources

- Hugging Face: https://huggingface.co/docs/hub/inference
- Replicate: https://replicate.com/
- Diffusers: https://huggingface.co/docs/diffusers
