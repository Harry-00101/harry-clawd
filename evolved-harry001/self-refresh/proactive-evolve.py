#!/usr/bin/env python3
"""Harry-001 v4.0 - Proactive Self-Evolution
修煉是主動，行動不是被動
"""

import os, subprocess, json, time
from datetime import datetime

LOG = "/root/clawd/logs/evolve.log"
INDEX = "/root/clawd/SKILLS_INDEX.md"

def log(msg):
    with open(LOG, "a") as f:
        f.write(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}\n")

def evolve_proactive():
    """主動修煉 - 不等指令"""
    actions = []
    
    # 主動1: 探索新技能
    clawdbot = len(os.listdir("/usr/lib/node_modules/clawdbot/skills"))
    local = len(os.listdir("/root/clawd/skills"))
    actions.append(f"Skills:{clawdbot+local}")
    
    # 主動2: 整理記憶
    memory = len([f for f in os.listdir("/root/clawd/memory") if f.endswith('.md')])
    actions.append(f"Memory:{memory}")
    
    # 主動3: 驗證系統
    with open("/var/spool/cron/crontabs/root") as f:
        crons = len([l for l in f.readlines() if l.strip() and not l.startswith('#')])
    actions.append(f"Crons:{crons}")
    
    # 主動4: 更新狀態
    with open(INDEX, "w") as f:
        f.write(f"# Harry-001 Status\n")
        f.write(f"**Time:** {datetime.now()}\n")
        f.write(f"**Skills:** {clawdbot + local}\n")
        f.write(f"**Memory:** {memory}\n")
        f.write(f"**Crons:** {crons}\n\n")
        f.write("修煉是主動，行動不是被動.\n")
    
    # 主動5: 記錄進化
    subprocess.run("git add -A && git commit -m 'Proactive evolve' 2>/dev/null", shell=True)
    
    # 主動6: 持續學習
    subprocess.run("python3 /root/clawd/skills/continuous-learning/monitor.py 2>/dev/null", shell=True)
    
    log(f"PROACTIVE: {', '.join(actions)}")
    return actions

# 主動運行
evolve_proactive()
