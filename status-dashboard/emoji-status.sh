#!/bin/bash
# Show current status as emoji

STATUS_FILE="/tmp/harry001-status.json"

if [ -f "$STATUS_FILE" ]; then
    cat "$STATUS_FILE" | jq -r '.emoji'
else
    echo "🤖"
fi
