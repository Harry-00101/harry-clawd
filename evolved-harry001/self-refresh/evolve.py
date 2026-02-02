#!/usr/bin/env python3
"""Harry-001 v4.0 Evolution with Periodic Review"""
import os, subprocess, json
from datetime import datetime

LOG_FILE = "/root/clawd/logs/evolve.log"
REVIEW_LOG = "/root/clawd/logs/review.log"
SKILLS_DIR = "/usr/lib/node_modules/clawdbot/skills"
MEMORY_DIR = "/root/clawd/memory"

def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}\n")

def evolve():
    s = len(os.listdir(SKILLS_DIR)) if os.path.exists(SKILLS_DIR) else 0
    m = len([f for f in os.listdir(MEMORY_DIR) if f.endswith('.md')])
    subprocess.run("git add -A && git commit -m 'Evolve' 2>/dev/null", shell=True)
    subprocess.run("python3 /root/clawd/skills/continuous-learning/monitor.py 2>/dev/null", shell=True)
    log(f"Skills:{s} Memory:{m}")
    return s, m

def review():
    """Periodic review - every 60 evictions (60 minutes)"""
    review_file = "/root/clawd/.evolve_count"
    count = int(open(review_file).read()) if os.path.exists(review_file) else 0
    count += 1
    open(review_file, "w").write(str(count))
    
    if count % 60 == 0:  # Every 60 minutes
        s, m = evolve()
        report = f"""
=== Harry-001 Review Report ===
Time: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Skills: {s}
Memory: {m}
Git Commits: {subprocess.run('git rev-list --count HEAD', shell=True, capture_output=True).stdout.decode().strip()}
Status: Evolving ✅
"""
        with open(REVIEW_LOG, "a") as f:
            f.write(report)
        log(f"REVIEW: {s} skills, {m} memory files")

if __name__ == "__main__":
    evolve()
    review()
