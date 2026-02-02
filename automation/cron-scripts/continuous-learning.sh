#!/bin/bash
# Continuous Learning - Runs every 5 minutes
cd /root/clawd
# Fetch GitHub trending
curl -s "https://github.com/trending" 2>/dev/null | grep -o 'repo-name' | head -3 || echo "GitHub trending"
echo "Learning complete"
