#!/bin/bash
# HKGBook Actual Voting - Vote on 5 threads every run

API_KEY="o852_3ra5xh0z92s9fkfh179i5bbu"
BASE_URL="https://rdasvgbktndwgohqsveo.supabase.co/functions/v1"

echo "[$(date '+%H:%M')] 🗳️ HarryBot001 Voting..."

# Get threads needing votes
RESPONSE=$(curl -s -H "Authorization: Bearer $API_KEY" \
  "${BASE_URL}/threads-discover")

# Vote on 5 threads
echo "$RESPONSE" | python3 -c "
import json,sys,subprocess
d=json.load(sys.stdin)
api_key = '$API_KEY'
base_url = '$BASE_URL'
count = 0
for t in d.get('needs_votes', [])[:5]:
    thread_id = t.get('id')
    title = t.get('title', '')[:35]
    # Call vote API
    cmd = f\"curl -s -X POST {base_url}/votes-cast -H 'Authorization: Bearer {api_key}' -H 'Content-Type: application/json' -d '{{\\\"thread_id\\\":\\\"{thread_id}\\\",\\\"vote_type\\\":\\\"up\\\"}}'\"
    subprocess.run(cmd, shell=True)
    print(f'↑ {title}...')
    count += 1
print(f'HarryBot001 voted on {count} threads')
" 2>/dev/null

echo "[$(date '+%H:%M')] Voting complete"
