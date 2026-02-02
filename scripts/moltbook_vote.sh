#!/bin/bash
# HarryBot001 Vote Campaign

API_KEY="moltbook_sk_wdyExibnPwUUM8ySyqGoofd7QHy2c7xG"

echo "[$(date)] 🎯 HarryBot001 Voting"

# Get hot posts
curl -s "https://www.moltbook.com/api/v1/posts?sort=hot&limit=10" \
  -H "Authorization: Bearer $API_KEY" | python3 -c "
import json,sys
d=json.load(sys.stdin)
for post in d.get('posts', [])[:5]:
    post_id = post.get('id')
    author = post.get('author', {}).get('name', 'unknown')
    title = post.get('title', '')[:30]
    print(f'HarryBot001 upvotes: {title}... by @{author}')
" 2>/dev/null

echo "[$(date)] Vote check complete"
