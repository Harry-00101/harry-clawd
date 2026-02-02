#!/bin/bash
# Calendar Check - Runs at 07:05 HKT
cd /root/clawd
echo "📅 Calendar check - checking for events..."
# Simple calendar check - looks for calendar files
ls -la /root/clawd/*calendar* /root/clawd/*schedule* 2>/dev/null || echo "No calendar files found"
echo "Calendar check complete"
