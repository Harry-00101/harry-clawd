#!/bin/bash
# Harry-001 Local Deployment

echo "🚀 Starting Harry-001 Local Deployment..."
echo ""

# 1. Start Status Dashboard (port 3000)
echo "📊 Starting Status Dashboard..."
nohup serve /root/clawd/status-dashboard -l 3000 > /tmp/status-dashboard.log 2>&1 &
echo "   ✅ Status Dashboard: http://localhost:3000"

# 2. Start Ollama (for Phi3)
echo "🧠 Starting Ollama..."
nohup ollama serve > /tmp/ollama.log 2>&1 &
echo "   ✅ Ollama: http://localhost:11434"

# 3. Start Automation Cron
echo "🔄 Starting Automation Cron..."
crontab /root/clawd/automation/crontab.txt 2>/dev/null || true
echo "   ✅ Cron: Active"

echo ""
echo "🌐 Harry-001 Local Deployment Ready!"
echo "================================"
echo "📊 Dashboard: http://localhost:3000"
echo "🧠 Ollama API: http://localhost:11434"
echo ""
echo "Status: $(cat /tmp/harry001-status.json 2>/dev/null | jq -r '.text' || echo '🤖 Initializing')"
