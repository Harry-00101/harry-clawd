#!/bin/bash
# Local LLM Agent - Using Ollama for small tasks

TASK=${1:-"你好，做個自我介紹"}
MODEL=${2:-"phi3"}

echo "=== Local LLM Agent ==="
echo "Task: $TASK"
echo "Model: $MODEL"
echo ""

# Check if Ollama is running
if ! pgrep -x ollama > /dev/null; then
  echo "Starting Ollama..."
  ollama serve &
  sleep 5
fi

# Run model
echo "🤖 Running $MODEL..."
echo ""
ollama run $MODEL "$TASK" 2>&1 | head -30

echo ""
echo "—— Local LLM Agent v1.0"
