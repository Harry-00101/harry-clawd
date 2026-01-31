#!/bin/bash
# Quick local transcription script

AUDIO_FILE="${1:-/tmp/voice.wav}"
MODEL="${2:-base}"
LANGUAGE="${3:-zh}"

cd /root/clawd/skills/local-whisper
python3 scripts/transcribe.py "$AUDIO_FILE" --model "$MODEL" --language "$LANGUAGE"
