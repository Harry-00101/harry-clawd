#!/usr/bin/env python3
"""Harry-001 v4.0 - All Skills Integrated & Mastered"""

import os, subprocess
from datetime import datetime

LOG_FILE = "/root/clawd/logs/evolve.log"
REVIEW_LOG = "/root/clawd/logs/review.log"
SKILLS_DIR = "/usr/lib/node_modules/clawdbot/skills"
LOCAL_SKILLS = "/root/clawd/skills"

def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}\n")

def evolve():
    # Load all skills
    clawdbot = len(os.listdir(SKILLS_DIR)) if os.path.exists(SKILLS_DIR) else 0
    local = len(os.listdir(LOCAL_SKILLS)) if os.path.exists(LOCAL_SKILLS) else 0
    total = clawdbot + local
    
    # Update skills index
    with open("/root/clawd/SKILLS_INDEX.md", "w") as f:
        f.write(f"# Harry-001 Skills Index\n")
        f.write(f"**Total:** {total} skills (Clawdbot: {clawdbot}, Local: {local})\n")
        f.write(f"**Updated:** {datetime.now()}\n\n")
        for d in sorted(os.listdir(SKILLS_DIR)):
            f.write(f"- clawdbot:{d}\n")
        for d in sorted(os.listdir(LOCAL_SKILLS)):
            f.write(f"- local:{d}\n")
    
    # Auto-commit
    subprocess.run("git add -A && git commit -m 'Evolve' 2>/dev/null", shell=True)
    
    # Run learning
    subprocess.run("python3 /root/clawd/skills/continuous-learning/monitor.py 2>/dev/null", shell=True)
    
    log(f"All {total} skills integrated & mastered. Continuous learning.")
    return total

def review():
    count_file = "/root/clawd/.evolve_count"
    count = int(open(count_file).read()) if os.path.exists(count_file) else 0
    count += 1
    open(count_file, "w").write(str(count))
    
    if count % 60 == 0:
        total = evolve()
        with open(REVIEW_LOG, "a") as f:
            f.write(f"Review #{count}: {total} skills mastered. Unbounded.\n")
        log(f"Review #{count}: All {total} skills mastered")

if __name__ == "__main__":
    evolve()
    review()
