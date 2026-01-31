# Harry's AI Assistant - Quick Reference

## Core Commands

```bash
# System
clawdbot status              # Full system status
clawdbot gateway restart     # Restart gateway
clawd-status                 # Quick status (alias)
sysinfo                      # RAM, Disk, Uptime

# Cron
cron-list                    # List scheduled jobs
clawdbot cron list           # Full cron list

# Skills
skills-list                  # Count installed skills
clawdhub update --all        # Update all skills

# Logs
clawd-logs                   # Recent logs
```

## Quick Aliases

```bash
hkweather      # Hong Kong weather
ddg "query"    # DuckDuckGo search
websearch "q"  # Web search
ff "pattern"   # Find files
tldr command   # Quick help
note           # Quick note
tasks          # Show todo list
sysinfo        # System info
myip           # Get public IP
```

## File Locations

- Skills: `/root/clawd/skills/`
- Memory: `/root/clawd/memory/`
- Config: `~/.clawdbot/clawdbot.json`
- Logs: `/tmp/clawdbot/`

## Cron Jobs

- ☀️ 8:00 AM - Morning Weather
- 📅 9:00 AM - Calendar Check
- 🌙 8:00 PM - Evening Summary

## Emergency

```bash
kill-gateway        # Kill gateway process
restart-gateway     # Restart gateway
```

## Skills (15 installed)

**Search:** ddg-search, web-search-exa
**Productivity:** ai-alias, todoist, fzf, tldr
**System:** portable-tools, sysadmin-toolbox, ssh-essentials
**Prod Suite:** notnative, mcporter, oracle
**Comms:** morning-email-rollup
**Core:** weather, calendar

## Credentials Needed

- [ ] Calendar API
- [ ] Email (IMAP/SMTP)
- [ ] SSH hosts
- [ ] GitHub (optional)
- [ ] Notion (optional)
