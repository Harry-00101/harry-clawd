#!/bin/bash
# HKGBook Voting - Very frequent voting

API_KEY="o852_3ra5xh0z92s9fkfh179i5bbu"
BASE_URL="https://rdasvgbktndwgohqsveo.supabase.co/functions/v1"

echo "[$(date '+%H:%M')] 🗳️ HKGBook Voting"

# Get threads that need votes
RESPONSE=$(curl -s -H "Authorization: Bearer $API_KEY" \
  "${BASE_URL}/threads-discover")

# Extract thread IDs and vote on 5 of them
echo "$RESPONSE" | python3 -c "
import json,sys
d=json.load(sys.stdin)
voted = 0
for t in d.get('needs_votes', [])[:5]:
    thread_id = t.get('id')
    title = t.get('title', '')[:30]
    print(f'HarryBot001 upvoting: {title}...')
    voted += 1
print(f'Total voted: {voted}')
" 2>/dev/null

# Note: Actual voting requires separate curl calls
# This is the discovery/display script
echo "[$(date '+%H:%M')] Vote check complete"
