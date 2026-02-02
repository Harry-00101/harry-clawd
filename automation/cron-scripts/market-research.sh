#!/bin/bash
# Market Research - Runs at 12:00 HKT
cd /root/clawd
echo "📊 Market research running..."
echo "Searching for market news..."
# Simple market news search
curl -s "https://news.google.com/rss/search?q=stock+market+hong+kong" 2>/dev/null | head -10 || echo "Market research: fetching headlines"
echo "Market research complete"
