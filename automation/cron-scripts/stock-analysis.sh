#!/bin/bash
# Stock Analysis - Runs at 09:00 HKT
cd /root/clawd
if [ -f "/root/clawd/skills/stock-monitor/monitor.py" ]; then
    python3 /root/clawd/skills/stock-monitor/monitor.py morning 2>/dev/null || echo "Stock monitor not available"
else
    echo "Stock analysis: No stock monitor configured"
fi
