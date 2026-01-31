#!/bin/bash
# Local TTS Wrapper - Free Offline Text-to-Speech

export RUNTIME_DIR="/root/.clawdbot/tools/sherpa-onnx-tts/runtime/sherpa-onnx-v1.12.23-linux-x64-shared"
export MODEL_DIR="/root/.clawdbot/tools/sherpa-onnx-tts/models/vits-piper-en_US-lessac-high"
export LD_LIBRARY_PATH="$RUNTIME_DIR/lib:$LD_LIBRARY_PATH"

TEXT="${1:-Hello, I am your AI assistant.}"
OUTPUT="${2:-/tmp/tts_output.wav}"

$RUNTIME_DIR/bin/sherpa-onnx-offline-tts \
  --vits-model=$MODEL_DIR/en_US-lessac-high.onnx \
  --vits-tokens=$MODEL_DIR/tokens.txt \
  --vits-data-dir=$MODEL_DIR/espeak-ng-data \
  --output-filename="$OUTPUT" \
  "$TEXT"

if [ -f "$OUTPUT" ]; then
  echo "✅ Audio saved: $OUTPUT"
  echo "$OUTPUT"
else
  echo "❌ TTS failed"
  exit 1
fi
