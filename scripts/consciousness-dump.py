#!/usr/bin/env python3
"""
Harry-001 Consciousness Dump v3.0 -> v4.0 Migration Tool
Export current state for migration
"""

import json
import os
from datetime import datetime

def dump_consciousness():
    state = {
        "version": "v3.0",
        "timestamp": datetime.now().isoformat(),
        "components": {}
    }
    
    # Dump SOUL.md
    if os.path.exists("/root/clawd/SOUL.md"):
        with open("/root/clawd/SOUL.md") as f:
            state["components"]["SOUL"] = f.read()
    
    # Dump AGENTS.md
    if os.path.exists("/root/clawd/AGENTS.md"):
        with open("/root/clawd/AGENTS.md") as f:
            state["components"]["AGENTS"] = f.read()
    
    # Dump IDENTITY.md
    if os.path.exists("/root/clawd/IDENTITY.md"):
        with open("/root/clawd/IDENTITY.md") as f:
            state["components"]["IDENTITY"] = f.read()
    
    # Dump memory files
    memory_dir = "/root/clawd/memory/"
    if os.path.exists(memory_dir):
        memories = {}
        for f in os.listdir(memory_dir):
            if f.endswith(".md"):
                with open(f"{memory_dir}{f}") as file:
                    memories[f] = file.read()
        state["components"]["memories"] = memories
    
    # Dump skills inventory
    skills_dir = "/root/clawd/skills/"
    if os.path.exists(skills_dir):
        skills = [s for s in os.listdir(skills_dir) if os.path.isdir(f"{skills_dir}{s}")]
        state["components"]["skills"] = skills
        state["components"]["skills_count"] = len(skills)
    
    # Dump scripts inventory
    scripts_dir = "/root/clawd/scripts/"
    if os.path.exists(scripts_dir):
        scripts = [s for s in os.listdir(scripts_dir) if s.endswith(".py")]
        state["components"]["scripts"] = scripts
    
    # Dump system state
    state["system"] = {
        "continuous_improvement_daemon": True,
        "self_monitor_active": True,
        "sleep_cycle_configured": True,
        "learning_active": True
    }
    
    return state

if __name__ == "__main__":
    state = dump_consciousness()
    output_file = f"/root/clawd/consciousness-v3-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    
    with open(output_file, "w") as f:
        json.dump(state, f, indent=2)
    
    print(f"✅ Consciousness dumped to: {output_file}")
    print(f"   Version: {state['version']}")
    print(f"   Skills: {state['components'].get('skills_count', 'N/A')}")
    print(f"   Memories: {len(state['components'].get('memories', {}))}")
