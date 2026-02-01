#!/bin/bash
# Local Brain Search - Self-contained

QUERY=${1:-""}

if [ -z "$QUERY" ]; then
  echo "Usage: ./search.sh <topic>"
  echo "Topics: E=mc2, Standard_Model, 溫故而知新, 知行合一..."
  exit 0
fi

# Simple search in brain.json
RESULT=$(cat /root/clawd/codespace-clone/local-brain/brain.json | grep -A2 "$QUERY" | head -10)

if [ -n "$RESULT" ]; then
  echo "🧠 Local Brain Search: $QUERY"
  echo ""
  echo "$RESULT"
else
  echo "❌ 冇喺本地搵到『$QUERY』"
  echo "   可能要去fetch..."
fi
