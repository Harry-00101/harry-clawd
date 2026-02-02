# Harry-001 v4.0 Evolution Plan
**Created:** 2026-02-02 01:16 HKT  
**Status:** Active

## 1. Daily Schedule (HKT)

| Time | Task | Script | Frequency |
|------|------|--------|-----------|
| 07:00 | Morning Weather | morning-weather.sh | Daily |
| 07:05 | Calendar Check | calendar-check.sh | Daily |
| 09:00 | Stock Analysis | stock-analysis.sh | Weekdays |
| 12:00 | Market Research | market-research.sh | Weekdays |
| 18:30 | Evening Summary | evening-summary.sh | Weekdays |
| 19:00 | News Digest | news-digest.sh | Daily |
| 23:00 | Day Summary | day-summary.sh | Daily |
| 23:55 | Quiet Mode | evening-summary.sh | Daily |

## 2. Continuous Operations

| Frequency | Task | Script |
|-----------|------|--------|
| Every 1 min | Evolution Check | evolve.py |
| Every 5 min | Learning | continuous-learning.sh |
| Every 1 hour | Self-Refresh | self-refresh.sh |
| Every 4 hours | Moltbook Heartbeat | moltbook-heartbeat.sh |

## 3. System Components

### Cron Scripts Location
`/root/clawd/automation/cron-scripts/`
- morning-weather.sh
- calendar-check.sh
- stock-analysis.sh
- market-research.sh
- evening-summary.sh
- news-digest.sh
- day-summary.sh
- continuous-learning.sh
- self-refresh.sh
- moltbook-heartbeat.sh

### Evolution System
`/root/clawd/evolved-harry001/self-refresh/evolve.py`
- Skills count
- Memory consolidation
- Git auto-commit
- Learning monitor

### Review System
- Trigger: Every 60 evolutions (60 minutes)
- Report: `/root/clawd/logs/review.log`

## 4. Automation Tools

### Update Script
`/root/clawd/automation/update-actions.sh`
- Updates all scripts
- Reloads crons
- Backs up crontab

### Git Hook
`.git/hooks/post-commit`
- Auto-reload crons on commit

## 5. Current Status

| Component | Status |
|-----------|--------|
| Crons | ✅ 12 active jobs |
| Scripts | ✅ 10 scripts created |
| Evolution | ✅ Every 1 min |
| Review | ✅ Every 60 min |
| Git Hook | ✅ Active |

## 6. Log Files

```
/root/clawd/logs/
├── evolve.log          (every minute)
├── review.log          (every 60 min)
├── morning-weather.log
├── calendar-check.log
├── stock-analysis.log
├── market-research.log
├── evening-summary.log
├── news-digest.log
├── day-summary.log
├── continuous-learning.log
├── self-refresh.log
└── moltbook-heartbeat.log
```

## 7. Commands

```bash
# Manual update
/root/clawd/automation/update-actions.sh

# Check crons
crontab -l

# Check logs
tail -f /root/clawd/logs/evolve.log

# Run evolution manually
python3 /root/clawd/evolved-harry001/self-refresh/evolve.py
```

## 8. Next Steps

- [ ] Test all cron scripts
- [ ] Add more real functionality to scripts
- [ ] Integrate with real APIs (weather, stock, news)
- [ ] Expand Moltbook engagement
- [ ] Add skill learning automation
