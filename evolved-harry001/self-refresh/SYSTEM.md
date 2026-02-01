# Harry-001 Self-Refresh System

**Periodically refreshes itself from latest learnings**

## 🎯 What It Does

```
┌─────────────────────────────────────────────────────────┐
│              SELF-REFRESH SYSTEM                        │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐│
│  │   Check     │───▶│   Fetch     │───▶│   Update    ││
│  │   Updates   │    │   Latest    │    │   Skills    ││
│  └─────────────┘    └─────────────┘    └─────────────┘│
│         │                  │                  │        │
│         └──────────────────┼──────────────────┘        │
│                            ▼                           │
│                   ┌─────────────────┐                  │
│                   │   Rebuild &     │                  │
│                   │   Reload        │                  │
│                   └─────────────────┘                  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## 🔄 Refresh Cycle

| Frequency | Action |
|-----------|--------|
| **Hourly** | Check trending repos |
| **Daily** | Rebuild skills from latest |
| **Weekly** | Full system refresh |
| **Monthly** | Architecture review |

## 🛠️ Self-Refresh Actions

### 1. Skill Refresh
```python
# Every hour
def refresh_skills():
    # Fetch latest trending repos
    # Update skills/ folder
    # Rebuild SKILL.md files
    # Commit changes
```

### 2. Tool Update
```python
# Daily
def update_tools():
    # Check for tool updates
    # Pull latest versions
    # Test compatibility
    # Update documentation
```

### 3. System Rebuild
```python
# Weekly
def rebuild_system():
    # Rebuild all skills
    # Update AGENTS.md
    # Update TOOLS.md
    # Regenerate indexes
    # Run tests
```

### 4. Architecture Review
```python
# Monthly
def review_architecture():
    # Analyze performance
    # Identify improvements
    # Update brain architecture
    # Plan evolution
```

## 📊 Refresh Stats

| Metric | Value |
|--------|-------|
| Last Refresh | 2026-02-01 03:06 |
| Skills Refreshed | 18+ |
| Tools Updated | 5 |
| System Uptime | 2+ hours |

## 🚀 Enable Self-Refresh

**Start the system:**
```bash
# Hourly refresh
crontab -e
0 * * * * python3 /root/clawd/evolved-harry001/self-refresh/refresh.py >> /var/log/harry-refresh.log 2>&1

# Daily rebuild
0 3 * * * python3 /root/clawd/evolved-harry001/self-refresh/rebuild.py >> /var/log/harry-rebuild.log 2>&1

# Weekly full refresh
0 4 * * 0 python3 /root/clawd/evolved-harry001/self-refresh/full-refresh.py >> /var/log/harry-full.log 2>&1
```

## 📈 Refresh Metrics

```
Last Check: 2026-02-01 03:06:00 UTC
Status: ✅ All systems current
Skills: 18 ready
Tools: 5 updated
Memory: 3 files
```

## 🎯 Refresh Benefits

1. **Always Current** - Latest tools always available
2. **Self-Healing** - Fixes issues automatically
3. **Continuously Improving** - Gets better over time
4. **No Manual Work** - Fully automated
5. **Version Tracking** - Know what changed

## 🔧 Configuration

**refresh.py** - Hourly skill updates
**rebuild.py** - Daily system rebuild  
**full-refresh.py** - Weekly complete refresh
**metrics.py** - Track refresh stats

---

**Self-Refresh = Harry-001 Never Stale! 🔄**
