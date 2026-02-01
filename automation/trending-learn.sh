#!/bin/bash
# GitHub Trending Auto-Learn - Every 30 minutes

echo "=== GitHub Trending Auto-Learn - $(date) ==="
python3 /root/clawd/skills/trending-learner/learn-trending.py
echo ""
echo "✅ Trending learned"
