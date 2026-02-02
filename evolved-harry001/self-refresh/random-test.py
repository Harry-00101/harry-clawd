#!/usr/bin/env python3
"""Harry-001 - Random Testing Generator
Proactively generate random inputs to test systems"""

import os, subprocess, random, json
from datetime import datetime

LOG = "/root/clawd/logs/random-test.log"

def log(msg):
    with open(LOG, "a") as f:
        f.write(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}\n")

def generate_random_test():
    """Generate random tests to stress-test systems"""
    
    tests = []
    
    # Random skill test
    skills = os.listdir("/usr/lib/node_modules/clawdbot/skills")
    random_skill = random.choice(skills)
    tests.append(f"Skill test: {random_skill}")
    
    # Random memory check
    memories = [f for f in os.listdir("/root/clawd/memory") if f.endswith('.md')]
    random_mem = random.choice(memories) if memories else "No memory"
    tests.append(f"Memory test: {random_mem}")
    
    # Random cron check
    with open("/var/spool/cron/crontabs/root") as f:
        crons = [l for l in f.readlines() if l.strip() and not l.startswith('#')]
    random_cron = random.choice(crons).split()[-1] if crons else "No cron"
    tests.append(f"Cron test: {random_cron}")
    
    # Random learning source
    sources = ["GitHub Trending", "arXiv", "Hacker News", "Moltbook", "RSS Feed"]
    random_source = random.choice(sources)
    tests.append(f"Learning source: {random_source}")
    
    # Log all tests
    log(f"TEST: {json.dumps(tests)}")
    
    # Execute learning
    subprocess.run("python3 /root/clawd/skills/continuous-learning/monitor.py 2>/dev/null", shell=True)
    
    return tests

if __name__ == "__main__":
    results = generate_random_test()
    print(f"Random tests generated: {len(results)}")
    for r in results:
        print(f"  - {r}")
