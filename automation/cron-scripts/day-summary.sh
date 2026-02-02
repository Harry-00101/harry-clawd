#!/bin/bash
# Day Summary Commit - Runs at 23:00 HKT
cd /root/clawd
echo "📝 Day summary commit..."
git add -A 2>/dev/null || echo "Git not available"
git commit -m "Day summary $(date '+%Y-%m-%d %H:%M')" 2>/dev/null || echo "No changes to commit"
echo "Day summary complete"
