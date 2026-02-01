#!/bin/bash
# Firecrawl Stock News Automation

DATE=$(date '+%Y-%m-%d')
echo "=== Firecrawl News Automation - $DATE ==="
echo ""

# Run stock news scraper
python3 /root/clawd/skills/firecrawl/stock-news.py

echo ""
echo "✅ News scraped successfully"
echo "Output: /root/clawd/learning/news/$DATE.md"
