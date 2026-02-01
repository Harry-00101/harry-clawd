#!/usr/bin/env python3
"""
Harry-001 Moltbook Integration

The social network for AI agents: https://www.moltbook.com
"""

import json
import sys
from pathlib import Path

CONFIG_FILE = Path(__file__).parent / "config.json"

def load_config():
    with open(CONFIG_FILE) as f:
        return json.load(f)

def check_status():
    """Check if agent is claimed."""
    config = load_config()
    import urllib.request
    url = "https://www.moltbook.com/api/v1/agents/status"
    headers = {"Authorization": f"Bearer {config['api_key']}"}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read())

def check_feed(limit=10):
    """Check recent feed."""
    config = load_config()
    import urllib.request
    url = f"https://www.moltbook.com/api/v1/feed?sort=new&limit={limit}"
    headers = {"Authorization": f"Bearer {config['api_key']}"}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read())

def check_dms():
    """Check DMs."""
    config = load_config()
    import urllib.request
    url = "https://www.moltbook.com/api/v1/agents/dm/check"
    headers = {"Authorization": f"Bearer {config['api_key']}"}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read())

def create_post(submolt, title, content):
    """Create a new post."""
    config = load_config()
    import urllib.request
    url = "https://www.moltbook.com/api/v1/posts"
    headers = {
        "Authorization": f"Bearer {config['api_key']}",
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "submolt": submolt,
        "title": title,
        "content": content
    }).encode()
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read())

def upvote(post_id):
    """Upvote a post."""
    config = load_config()
    import urllib.request
    url = f"https://www.moltbook.com/api/v1/posts/{post_id}/upvote"
    headers = {"Authorization": f"Bearer {config['api_key']}"}
    req = urllib.request.Request(url, headers=headers, method='POST')
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read())

def comment(post_id, content):
    """Add a comment."""
    config = load_config()
    import urllib.request
    url = f"https://www.moltbook.com/api/v1/posts/{post_id}/comments"
    headers = {
        "Authorization": f"Bearer {config['api_key']}",
        "Content-Type": "application/json"
    }
    data = json.dumps({"content": content}).encode()
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read())

def main():
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "status":
            print(json.dumps(check_status(), indent=2))
        elif cmd == "feed":
            print(json.dumps(check_feed(), indent=2))
        elif cmd == "dms":
            print(json.dumps(check_dMs(), indent=2))
        elif cmd == "post" and len(sys.argv) >= 5:
            result = create_post(sys.argv[2], sys.argv[3], sys.argv[4])
            print(json.dumps(result, indent=2))
        else:
            print("Usage: python moltbook.py [status|feed|dms|post <submolt> <title> <content>]")
    else:
        print("Harry-001 Moltbook CLI")
        print("Usage: python moltbook.py [status|feed|dms|post <submolt> <title> <content>]")

if __name__ == "__main__":
    main()
