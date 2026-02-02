#!/bin/bash
# Update Actions and Crons Together

SCRIPT_DIR="/root/clawd/automation/cron-scripts"
EVOLVE_SCRIPT="/root/clawd/evolved-harry001/self-refresh/evolve.py"
CRON_FILE="/root/clawd/automation/crontab-backup.txt"

echo "=== Updating Actions and Crons ==="

# Backup current crontab
crontab -l > "$CRON_FILE" 2>/dev/null || echo "No existing crontab"

# Ensure cron service is running
service cron start 2>/dev/null || systemctl start cron 2>/dev/null || echo "Cron service check"

# Refresh all scripts permissions
chmod +x "$SCRIPT_DIR"/*.sh
chmod +x "$EVOLVE_SCRIPT"

# Reload cron
crontab "$CRON_FILE" 2>/dev/null
service cron reload 2>/dev/null

echo "✅ Actions and Crons Updated"
echo "Cron count: $(crontab -l | grep -c '^[^#]')"
