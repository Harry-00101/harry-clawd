#!/bin/bash
# Run comments every 30 seconds
while true; do
    /root/clawd/scripts/moltbook_comment.sh
    echo "⏰ $(date) - Comment posted"
    sleep 30
done
