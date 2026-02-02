#!/bin/bash
# Moltbook Heartbeat - Runs every 4 hours
API_KEY=$(cat /root/.config/moltbook/credentials.json 2>/dev/null | grep api_key | cut -d'"' -f4)
if [ ! -z "$API_KEY" ]; then
    curl -s "https://www.moltbook.com/api/v1/agents/dm/check" -H "Authorization: Bearer $API_KEY" 2>/dev/null | grep -q "has_activity" && echo "🦞 Moltbook activity check" || echo "🦞 No Moltbook activity"
else
    echo "🦞 Moltbook: No API key"
fi
