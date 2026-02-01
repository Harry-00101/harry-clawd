# Image Generation Skill

AI image generation using various APIs and tools.

## Options

### 1. Replicate (Flux, SDXL, etc.)
```bash
pip install replicate
export REPLICATE_API_TOKEN="your-token"
```

```python
import replicate

output = replicate.run(
    "black-forest-labs/flux-schnell",
    input={
        "prompt": "A robot girl with silver hair, blue eyes, anime style",
        "width": 1024,
        "height": 1024
    }
)
print(output[0])
```

### 2. OpenAI DALL-E
```bash
pip install openai
```

```python
from openai import OpenAI
client = OpenAI(api_key="your-key")

response = client.images.generate(
    model="dall-e-3",
    prompt="A futuristic robot girl in a cozy cafe",
    size="1024x1024",
    quality="standard",
    n=1,
)
print(response.data[0].url)
```

### 3. Hugging Face (Free, local)
```bash
pip install diffusers torch transformers
```

```python
from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
)
pipe = pipe.to("cuda")

image = pipe("anime robot girl, silver hair, blue eyes").images[0]
image.save("robot_girl.png")
```

## Prompt Structure

```
[Subject] + [Style] + [Lighting] + [Mood] + [Details]
```

Example:
```
White robotic girl, silver bob hair, large headphones with 
blue lights, blue eyes, mechanical joints visible, anime 
style, soft warm lighting, cozy cafe setting, friendly expression
```

## Resources

- Replicate: https://replicate.com/
- OpenAI DALL-E: https://platform.openai.com/docs/dall-e
- Hugging Face: https://huggingface.co/docs/diffusers
