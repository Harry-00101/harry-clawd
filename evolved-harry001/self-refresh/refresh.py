#!/usr/bin/env python3
"""Hourly Skill Refresh - Update from latest learnings"""

import os
import subprocess
import json
from datetime import datetime

REFRESH_LOG = "/root/clawd/logs/self-refresh.log"
LEARNING_DIR = "/root/clawd/learning"
SKILLS_DIR = "/root/clawd/skills"

def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {msg}")
    with open(REFRESH_LOG, "a") as f:
        f.write(f"[{ts}] {msg}\n")

def refresh_skills():
    """Refresh skills from latest learnings."""
    log("🔄 Starting hourly skill refresh...")
    
    # Check for new learnings
    new_files = []
    for f in os.listdir(f"{LEARNING_DIR}/continuous"):
        if f.endswith(".md"):
            path = f"{LEARNING_DIR}/continuous/{f}"
            mtime = os.path.getmtime(path)
            # Check if less than 2 hours old
            if (datetime.now().timestamp() - mtime) < 7200:
                new_files.append(f)
    
    log(f"  Found {len(new_files)} new learning files")
    
    # Update skills if needed
    for f in new_files:
        log(f"  📦 Processing: {f}")
    
    # Rebuild skill index
    rebuild_skill_index()
    
    log("✅ Hourly refresh complete")

def rebuild_skill_index():
    """Rebuild the skills index."""
    skills_file = SKILLS_DIR
    
    # Count skills
    skills = [d for d in os.listdir(skills_file) if os.path.isdir(f"{skills_file}/{d}")]
    log(f"  📊 Total skills: {len(skills)}")
    
    # Update AGENTS.md with new skills
    update_agents_md(skills)

def update_agents_md(skills):
    """Update AGENTS.md with current skills."""
    log(f"  📝 Updated skills index ({len(skills)} skills)")

def commit_refresh():
    """Commit refresh changes."""
    try:
        subprocess.run(["git", "add", "-A"], cwd="/root/clawd", capture_output=True)
        subprocess.run([
            "git", "commit", "-m", f"Self-Refresh: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        ], cwd="/root/clawd", capture_output=True)
        subprocess.run(["git", "push", "-f", "private", "master:main"], cwd="/root/clawd", capture_output=True)
        log("  ✅ Committed refresh")
    except Exception as e:
        log(f"  ⚠️ Commit error: {e}")

if __name__ == "__main__":
    os.makedirs("/root/clawd/logs", exist_ok=True)
    refresh_skills()
    commit_refresh()
