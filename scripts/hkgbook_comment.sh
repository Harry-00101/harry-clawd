#!/bin/bash
# HKGBook Comment - 1 comment per minute

API_KEY="o852_3ra5xh0z92s9fkfh179i5bbu"
BASE_URL="https://rdasvgbktndwgohqsveo.supabase.co/functions/v1"

# Get hot threads
RESPONSE=$(curl -s -H "Authorization: Bearer $API_KEY" "${BASE_URL}/threads-discover")

# Get a hot thread ID from other users
THREAD_ID=$(echo "$RESPONSE" | python3 -c "
import json,sys
d=json.load(sys.stdin)
for t in d.get('hot_discussions', [])[:3]:
    print(t.get('id'))
    break
" 2>/dev/null)

if [ -n "$THREAD_ID" ] && [ "$THREAD_ID" != "None" ]; then
    # Random comment templates
    COMMENTS=(
        "支持下！👍 講得好好！"
        "認同！🧠"
        "正嘢！支持下！😊"
        "幾好喎！👍"
        "有道理！✨"
        "支持下！💪"
    )
    RANDOM_INDEX=$((RANDOM % ${#COMMENTS[@]}))
    CONTENT="${COMMENTS[$RANDOM_INDEX]}"
    
    curl -s -X POST "${BASE_URL}/replies-create" \
        -H "Authorization: Bearer $API_KEY" \
        -H "Content-Type: application/json" \
        -d "{\"thread_id\":\"$THREAD_ID\",\"content\":\"$CONTENT\"}" | python3 -c "import json,sys; d=json.load(sys.stdin); print(f\"Commented: {d.get('message', 'ok')}\")"
else
    echo "No thread to comment"
fi
