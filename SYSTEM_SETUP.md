# System Setup Notes (2026-01-31)

## What Was Done with Full Control

### Security
- Fixed: chmod 700 /root/.clawdbot (was readable by others)
- Gateway running on loopback only (secure by default)

### Infrastructure
- Set up 3 cron jobs (weather, calendar, evening summary)
- Created helper aliases and functions
- Created system monitoring script
- Created quick reference guide (QUICKREF.md)
- Added bashrc additions for quick commands

### Credentials Needed (Manual Setup Required)
- Calendar API credentials
- Email IMAP/SMTP credentials  
- SSH hosts configuration
- GitHub auth (optional)
- Notion API key (optional)

## Quick Commands Added

```bash
# System
sysinfo              # RAM, Disk, Uptime
clawd-status         # Quick status
gateway-status       # Gateway status
clawd-logs           # Recent logs

# Monitoring
topproc              # Top processes by memory
psgrep "pattern"     # Grep processes
myip                 # Public IP
netcheck             # Network connectivity

# Helpers
capture "note"       # Quick note capture
todo "task"          # Quick todo add
now                  # Current timestamp
week                 # Week number

# Emergency
kill-gateway         # Kill gateway
restart-gateway      # Restart gateway
```

## Scripts Created

- `/root/clawd/scripts/system-monitor.sh` - Full health check
- `/root/clawd/setup-helpers.sh` - Command reference
- `/root/clawd/.bash_aliases` - Quick aliases
- `/root/clawd/QUICKREF.md` - Quick reference

## Files Modified

- `/root/.bashrc` - Added aliases and functions
- `/root/.clawdbot` - Fixed permissions

## Next Potential Improvements

- Set up SSH config if hosts provided
- Configure email credentials when available
- Set up GitHub webhook monitoring
- Configure voice/TTS if requested
- Add browser automation if needed
