#!/bin/bash
# Auto commit and push to GitHub

cd /root/clawd

# Add all changes
git add -A

# Check if there are changes
if git diff --cached --quiet; then
    echo "[$(date)] No changes to commit"
    exit 0
fi

# Commit with timestamp
git commit -m "Auto-update $(date '+%Y-%m-%d %H:%M')"

# Push (ignore errors if secrets blocked)
git push origin master 2>/dev/null || echo "[$(date)] Push blocked (secrets or network)"

echo "[$(date)] GitHub sync complete"
