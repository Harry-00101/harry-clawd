#!/bin/bash
# Web Browsing Heartbeat - Every 30 minutes
# Checks web for news, trends, updates

API_KEY=$(cat /root/.config/moltbook/credentials.json 2>/dev/null | grep api_key | cut -d'"' -f4)

# Check news sources
curl -s "https://news.google.com/rss/search?q=AI+technology" 2>/dev/null | head -5

# Check Moltbook feed if API available
if [ ! -z "$API_KEY" ]; then
    curl -s "https://www.moltbook.com/api/v1/feed?sort=new&limit=3" -H "Authorization: Bearer $API_KEY" 2>/dev/null | grep -o '"title":"[^"]*"' | head -3
fi
