#!/usr/bin/env python3
"""1Password CLI Helper for Harry-001

Usage:
1. Install 1Password CLI: https://1password.com/downloads/cli/
2. Sign in: op signin
3. Use this helper to manage API keys

Example:
python3 tools/op_helper.py list    # List all secrets
python3 tools/op_helper.py get HF_TOKEN  # Get specific secret
"""

import subprocess
import json
import os
from pathlib import Path

CONFIG_FILE = Path(__file__).parent.parent / ".config" / "1password" / "secrets.json"

def run_op(args):
    """Run 1Password CLI command."""
    result = subprocess.run(['op'] + args, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def list_secrets():
    """List all secrets in Private vault."""
    stdout, stderr, code = run_op(['item', 'list', '--vault=Private'])
    if code == 0:
        print("📦 Your 1Password Secrets:")
        print(stdout)
    else:
        print(f"❌ Error: {stderr}")
        print("💡 Tip: Run 'op signin' first to authenticate")

def get_secret(name):
    """Get a secret by name."""
    # First, try to find the item
    stdout, stderr, code = run_op(['item', 'get', name, '--format=json'])
    if code == 0:
        try:
            data = json.loads(stdout)
            print(f"✅ Found: {name}")
            return data
        except:
            pass
    
    # Try searching
    stdout, stderr, code = run_op(['item', 'list', '--query', name])
    if code == 0 and stdout:
        print(f"🔍 Search results for '{name}':")
        print(stdout)
    else:
        print(f"❌ Secret '{name}' not found")
    return None

def add_secret(name, value, note=""):
    """Add a new secret."""
    stdout, stderr, code = run_op([
        'item', 'create',
        '--title', name,
        '--category', 'Password',
        '--password', value,
        '--url', 'harry-001.local',
        note and f'--note', note
    ])
    if code == 0:
        print(f"✅ Added secret: {name}")
    else:
        print(f"❌ Error: {stderr}")

def setup_local_secrets():
    """Setup local secrets file as fallback."""
    secrets = {}
    
    # Check for existing tokens
    for key, path in [
        ('HF_TOKEN', '/root/clawd/.config/huggingface.json'),
        ('REPLICATE_API_TOKEN', '/root/clawd/.config/replicate.json'),
        ('MOLTBOOK_API_KEY', '/root/clawd/skills/moltbook/config.json'),
    ]:
        if Path(path).exists():
            try:
                with open(path) as f:
                    content = f.read()
                    # Extract simple values
                    for line in content.split('\n'):
                        if 'token' in line.lower() or 'key' in line.lower():
                            parts = line.split(':')
                            if len(parts) > 1:
                                secrets[key] = parts[1].strip().strip(',"')
            except:
                pass
    
    if secrets:
        with open(CONFIG_FILE, 'w') as f:
            json.dump(secrets, f, indent=2)
        print(f"✅ Synced {len(secrets)} secrets to local file")
    else:
        print("No secrets found to sync")

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("🔐 HARRY-001 1Password Helper")
        print("Usage: python3 tools/op_helper.py [command]")
        print()
        print("Commands:")
        print("  list          - List all 1Password secrets")
        print("  get <name>    - Get a specific secret")
        print("  add <name> <value> [note] - Add secret")
        print("  sync          - Sync local secrets to 1Password")
        print("  setup-local   - Create local secrets file")
        print()
        print("Install 1Password CLI: https://1password.com/downloads/cli/")
        return
    
    cmd = sys.argv[1]
    
    if cmd == "list":
        list_secrets()
    elif cmd == "get" and len(sys.argv) >= 3:
        get_secret(sys.argv[2])
    elif cmd == "add" and len(sys.argv) >= 4:
        add_secret(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else "")
    elif cmd == "sync":
        setup_local_secrets()
    elif cmd == "setup-local":
        setup_local_secrets()
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
