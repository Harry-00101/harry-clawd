#!/bin/bash
# Get current status emoji

HOUR=$(date +%H)

if [ "$HOUR" -ge 3 ] && [ "$HOUR" -le 5 ]; then
    echo "📚 Learning"
elif [ "$HOUR" -ge 1 ] && [ "$HOUR" -le 6 ]; then
    echo "💤 Idle"
elif [ "$HOUR" -ge 23 ] || [ "$HOUR" -le 6 ]; then
    echo "💤 Sleep"
else
    echo "🟢 Active"
fi
