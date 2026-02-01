# Voicebox Integration

Open-source voice synthesis studio by Jamie Pine.

## What is Voicebox?

"Think of it as the Ollama for voice"
- Local-first voice cloning
- Professional DAW-like features
- Qwen3-TTS powered
- Privacy-focused (data stays local)

## Features

| Feature | Description |
|---------|-------------|
| **Voice Cloning** | Clone from few seconds of audio |
| **Multi-track Editor** | DAW-like timeline |
| **Qwen3-TTS** | Alibaba's breakthrough TTS model |
| **MLX Backend** | 4-5x faster on Apple Silicon |
| **API-first** | Desktop app or integrate projects |
| **Privacy** | All local, no cloud |

## Jamie Pine

Creator of:
- **Linear** (famous project management tool)
- Various AI tools
- Product-focused developer

## For Harry-001

Add voice capabilities:
1. **Voice Notifications** - Hear stock alerts
2. **TTS Reports** - Listen to analysis
3. **Voice Cloning** - Custom voice output
4. **Multi-voice** - Different voices for different tasks

## Installation

```bash
# Download from https://github.com/jamiepine/voicebox/releases
# Or via CLI
curl -fsSL https://voicebox.sh/install.sh | bash
```

## API Usage

```python
# Voice synthesis API
import requests

# Generate speech
response = requests.post("http://localhost:5000/tts", json={
    "text": "VOO is up 2.3% today",
    "voice": "my-voice-profile",
    "model": "qwen3-tts"
})

with open("voo-alert.wav", "wb") as f:
    f.write(response.content)
```

## Integration with Harry-001

```
Harry-001
    ↓
Voicebox API
    ↓
Voice Output (TTS)
    ↓
Audio Notifications / Reports
```

## References

- https://github.com/jamiepine/voicebox
- https://voicebox.sh
- Qwen3-TTS: https://github.com/Qwen/Qwen3-TTS
