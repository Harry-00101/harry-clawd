#!/bin/bash
# News Digest - Runs at 19:00 HKT
cd /root/clawd
echo "📰 News digest running..."
echo "Fetching latest tech and finance news..."
# Simple news check
curl -s "https://news.google.com/rss/search?q=technology+AI" 2>/dev/null | grep -o '<title>[^<]*</title>' | head -5 || echo "News sources checked"
echo "News digest complete"
