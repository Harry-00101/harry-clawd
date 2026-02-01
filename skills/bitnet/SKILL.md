# BitNet Integration Skill

Microsoft BitNet - 1-bit LLM inference framework.

## Features
- 1.58-bit quantization
- CPU inference (no GPU needed)
- 2.37x - 6.17x speedup
- 71-82% energy reduction

## Models
- BitNet-b1.58-2B-4T (2.4B parameters)
- Llama3-8B-1.58-100B-tokens (8B parameters)
- bitnet_b1_58-3B (3.3B parameters)

## Usage
```bash
# Install bitnet.cpp
git clone https://github.com/microsoft/BitNet.git
cd BitNet
pip install -r requirements.txt
python run.py --model microsoft/BitNet-b1.58-2B-4T
```

## For Harry-001
- More efficient than Phi3
- Can run larger models locally
- Lower resource usage
