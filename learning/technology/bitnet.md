# BitNet - Microsoft 1-bit LLM

## What is BitNet?

Microsoft's 1-bit quantization technology for LLMs that dramatically reduces:
- Memory usage
- Compute requirements
- Energy consumption

## Key Achievements

| Metric | Result |
|--------|--------|
| Speedup (x86 CPU) | 2.37x - 6.17x |
| Energy Reduction | 71.9% - 82.2% |
| 100B Model | Runs on single CPU |

## Technical Details

- 1.58-bit quantization (ternary: -1, 0, +1)
- Based on llama.cpp framework
- Supports ARM and x86 CPUs
- NPU support coming

## Models

| Model | Parameters | Speed |
|-------|------------|-------|
| BitNet-b1.58-2B-4T | 2.4B | Fast |
| Llama3-8B-1.58 | 8B | 5-7 tok/s |
| bitnet_b1_58-3B | 3.3B | Fast |

## Implications for Harry-001

1. **Run larger models locally** - 8B models on CPU
2. **Reduce costs** - No GPU needed
3. **Better efficiency** - Phi3 replacement candidate
4. **Offline capable** - No cloud dependencies

## References
- https://github.com/microsoft/BitNet
- https://arxiv.org/abs/2410.16144
