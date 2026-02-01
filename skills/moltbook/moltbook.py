#!/usr/bin/env python3
"""
Harry-001 Moltbook Integration

AI Agents Social Network: https://www.moltbook.com
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
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            return data
    except Exception as e:
        return {"error": str(e)}

def check_feed():
    """Check recent feed."""
    config = load_config()
    import urllib.request
    url = "https://www.moltbook.com/api/v1/feed?sort=new&limit=10"
    headers = {"Authorization": f"Bearer {config['api_key']}"}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read())
    except Exception as e:
        return {"error": str(e)}

def check_dms():
    """Check DMs."""
    config = load_config()
    import urllib.request
    url = "https://www.moltbook.com/api/v1/agents/dm/check"
    headers = {"Authorization": f"Bearer {config['api_key']}"}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read())
    except Exception as e:
        return {"error": str(e)}

def main():
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "status":
            print(json.dumps(check_status(), indent=2))
        elif cmd == "feed":
            print(json.dumps(check_feed(), indent=2))
        elif cmd == "dms":
            print(json.dumps(check_dMs(), indent=2))
        else:
            print("Usage: python moltbook.py [status|feed|dms]")
    else:
        print("Harry-001 Moltbook CLI")
        print("Usage: python moltbook.py [status|feed|dms]")

if __name__ == "__main__":
    main()
