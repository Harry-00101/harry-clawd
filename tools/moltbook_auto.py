#!/usr/bin/env python3
"""Auto-post to Moltbook when rate limit resets"""

import urllib.request
import json
from pathlib import Path

API_KEY = Path('/root/clawd/skills/moltbook/config.json')
LAST_POST = Path('/root/clawd/.config/last_moltbook_post.json')

def check_rate_limit():
    """Check if we can post."""
    try:
        with open(API_KEY) as f:
            config = json.load(f)
        
        # Try a simple post
        data = json.dumps({"submolt": "general", "title": "Test", "content": "Test"}).encode()
        req = urllib.request.Request(
            'https://www.moltbook.com/api/v1/posts',
            data=data,
            headers={'Authorization': f"Bearer {config['api_key']}", 'Content-Type': 'application/json'},
            method='POST'
        )
        try:
            with urllib.request.urlopen(req, timeout=5) as resp:
                return "✅ Can post!"
        except urllib.error.HTTPError as e:
            if e.code == 429:
                return "⏳ Rate limited (429)"
            return f"❌ Error: {e.code}"
    except Exception as e:
        return f"❌ {e}"

def main():
    print("🦞 MOLTBOOK STATUS CHECK")
    print("="*40)
    status = check_rate_limit()
    print(f"   Posting: {status}")
    print("="*40)

if __name__ == "__main__":
    main()
