#!/usr/bin/env python3
import os, subprocess
from datetime import datetime

LOG_FILE = "/root/clawd/logs/evolve.log"
MEMORY_DIR = "/root/clawd/memory"
SKILLS_DIR = "/usr/lib/node_modules/clawdbot/skills"

def run():
    # Skills
    s = len(os.listdir(SKILLS_DIR)) if os.path.exists(SKILLS_DIR) else 0
    # Memory  
    m = len([f for f in os.listdir(MEMORY_DIR) if f.endswith('.md')])
    # Git auto-commit
    subprocess.run("git add -A && git commit -m 'Evolve' 2>/dev/null", shell=True)
    # Learning
    subprocess.run("python3 /root/clawd/skills/continuous-learning/monitor.py 2>/dev/null", shell=True)
    # Write log
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now().strftime('%H:%M:%S')}] Skills:{s} Memory:{m}\n")

if __name__ == "__main__":
    run()
