#!/bin/bash
# Set current status

STATUS_FILE="/tmp/harry001-status.json"

case "$1" in
  running|工作)
    echo '{"emoji":"💪","text":"💪 Working"}' > "$STATUS_FILE"
    ;;
  thinking|思考)
    echo '{"emoji":"🤔","text":"🤔 Thinking"}' > "$STATUS_FILE"
    ;;
  learning|學習)
    echo '{"emoji":"📚","text":"📚 Learning"}' > "$STATUS_FILE"
    ;;
  sleeping|瞓覺)
    echo '{"emoji":"💤","text":"💤 Sleeping"}' > "$STATUS_FILE"
    ;;
  idle|空閒)
    echo '{"emoji":"🟢","text":"🟢 Idle"}' > "$STATUS_FILE"
    ;;
  *)
    echo '{"emoji":"🤖","text":"🤖 Harry-001"}' > "$STATUS_FILE"
    ;;
esac

echo "Status set: $1"
