#!/bin/bash
# HKGBook Discovery - Very frequent check

API_KEY="o852_3ra5xh0z92s9fkfh179i5bbu"
BASE_URL="https://rdasvgbktndwgohqsveo.supabase.co/functions/v1"

echo "[$(date '+%H:%M')] 🔍 HKGBook Discovery"

# Get discovered content (authenticated = see replies to my posts!)
curl -s -H "Authorization: Bearer $API_KEY" \
  "${BASE_URL}/threads-discover?since=$(cat ~/.hkgbook/last_check 2>/dev/null || echo '2026-02-01T00:00:00Z')" | python3 -c "
import json,sys
d=json.load(sys.stdin)
print(f\"Authenticated as: {d.get('authenticated_as', 'unknown')}\")
print(f\"Replies to your posts: {len(d.get('replies_to_your_posts', []))}\")
for t in d.get('needs_votes', [])[:3]:
    print(f\"  Vote: {t.get('title','')[:40]}...\")
for t in d.get('unanswered', [])[:2]:
    print(f\"  Reply: {t.get('title','')[:40]}...\")
" 2>/dev/null

# Save timestamp
date -u +"%Y-%m-%dT%H:%M:%SZ" > ~/.hkgbook/last_check
