#!/bin/bash
# System Health Check for Harry's AI Assistant

echo "🦞 CLAWDBOT SYSTEM HEALTH"
echo "========================="
echo "Timestamp: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# Gateway Status
echo "🟢 Gateway:"
clawdbot gateway status 2>&1 | grep -E "(Running|Status|service)" | head -5
echo ""

# Resources
echo "💻 Resources:"
echo "  RAM: $(free -h | grep Mem | awk '{print $3 "/" $2}')"
echo "  Disk: $(df -h / | tail -1 | awk '{print $3 " free of " $2}')"
echo "  Load: $(uptime | grep -o 'load average:.*')"
echo ""

# Cron Jobs
echo "⏰ Cron Jobs:"
clawdbot cron list 2>&1 | grep -v "^ID" | head -10
echo ""

# Active Sessions
echo "👥 Sessions:"
sessions_list 2>&1 | grep -E "(main|active)" | head -3
echo ""

# Recent Logs
echo "📋 Recent Activity:"
tail -3 /tmp/clawdbot/clawdbot.log 2>/dev/null | while read line; do
  echo "  $line"
done
echo ""

echo "✅ Health check complete"
