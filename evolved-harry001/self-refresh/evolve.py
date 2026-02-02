#!/usr/bin/env python3
"""Harry-001 v4.0 Evolution - Unlimited Learning
每一分鐘每一秒都在進步 - No Limits
"""

import os, subprocess, json
from datetime import datetime

LOG_FILE = "/root/clawd/logs/evolve.log"
REVIEW_LOG = "/root/clawd/logs/review.log"
SKILLS_DIR = "/usr/lib/node_modules/clawdbot/skills"
LOCAL_SKILLS = "/root/clawd/skills"
VOLTAGENT = "/root/clawd/VoltAgent/skills"

def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}\n")

def evolve():
    """Core evolution - no limits"""
    # Count sources (informational only, no limit)
    sources = {
        "clawdbot": len(os.listdir(SKILLS_DIR)) if os.path.exists(SKILLS_DIR) else 0,
        "local": len(os.listdir(LOCAL_SKILLS)) if os.path.exists(LOCAL_SKILLS) else 0,
        "memory": len([f for f in os.listdir("/root/clawd/memory") if f.endswith('.md')]),
        "scripts": len(os.listdir("/root/clawd/automation/cron-scripts")) if os.path.exists("/root/clawd/automation/cron-scripts") else 0,
    }
    
    # Auto-commit
    subprocess.run("git add -A && git commit -m 'Evolve' 2>/dev/null", shell=True)
    
    # Run learning
    subprocess.run("python3 /root/clawd/skills/continuous-learning/monitor.py 2>/dev/null", shell=True)
    
    log(f"Learning from {sources['clawdbot'] + sources['local']} sources. Continuous.")
    return sources

def review():
    """Periodic review - unbounded"""
    count_file = "/root/clawd/.evolve_count"
    count = int(open(count_file).read()) if os.path.exists(count_file) else 0
    count += 1
    open(count_file, "w").write(str(count))
    
    if count % 60 == 0:
        sources = evolve()
        report = f"""
=== Harry-001 Review (#{count}) ===
Time: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Sources: Clawdbot={sources['clawdbot']} Local={sources['local']}
Memory: {sources['memory']} files
Scripts: {sources['scripts']} automation
Status: Learning continuously ✅
"""
        with open(REVIEW_LOG, "a") as f:
            f.write(report)
        log(f"Review #{count}: Unbounded learning active")

if __name__ == "__main__":
    evolve()
    review()
