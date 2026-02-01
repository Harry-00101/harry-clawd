#!/bin/bash
# Worldwide Research Heartbeat
# Fetches international & tech news

cd /root/clawd

# Research categories
CATEGORIES=("AI agents multi-agent systems 2026" "technology news today" "international news world")

for query in "${CATEGORIES[@]}"; do
  echo "=== Research: $query ==="
  curl -s "https://api.allorigins.win/raw?url=https://duckduckgo.com/?q=$(echo $query | tr ' ' '+')&format=json" 2>/dev/null | head -500 || echo "Search limited"
done

echo "=== Research Complete ===" 
echo "$(date): Worldwide research heartbeat completed" >> /root/clawd/memory/research-log.md
