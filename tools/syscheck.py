#!/usr/bin/env python3
"""Harry-001 System Health Checker"""

import os
import subprocess
from pathlib import Path

def check_process(name):
    """Check if process is running."""
    result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
    return any(name in line and 'grep' not in line for line in result.stdout.split('\n'))

def check_log(path):
    """Get last line of log file."""
    if Path(path).exists():
        with open(path) as f:
            lines = f.readlines()
            return lines[-1].strip() if lines else "Empty"
    return "Not found"

def main():
    print("🔧 HARRY-001 SYSTEM STATUS")
    print("="*40)
    
    # Check processes
    print("\n📦 Installing Packages:")
    for name, log_path in [
        ('torch', '/root/clawd/logs/torch_install.log'),
        ('whisper', '/root/clawd/logs/whisper_install.log'),
    ]:
        status = check_log(log_path)
        print(f"   {name}: {status[:50]}")
    
    print("\n🔄 Background Processes:")
    for name in ['torch', 'whisper', 'sd']:
        if check_process(name):
            print(f"   {name}: ✅ Running")
        else:
            print(f"   {name}: ❌ Not running")
    
    print("\n💾 Disk Usage:")
    result = subprocess.run(['df', '-h', '/'], capture_output=True, text=True)
    print(f"   {result.stdout.splitlines()[-1]}")
    
    print("\n🧠 Memory:")
    result = subprocess.run(['free', '-h'], capture_output=True, text=True)
    print(result.stdout.splitlines()[1])
    
    print("\n" + "="*40)
    print("💪 Harry-001 Self-Monitoring Active!")

if __name__ == "__main__":
    main()
