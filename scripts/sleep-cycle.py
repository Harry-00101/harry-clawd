#!/usr/bin/env python3
"""
Harry-001 Sleep/Refresh Cycle System
Sleep = Restart, Refresh = Upgrade
"""

import os
import subprocess
import json
from datetime import datetime

class SleepCycle:
    def __init__(self):
        self.state_file = "/root/clawd/.sleep-state.json"
    
    def sleep(self):
        """Prepare for sleep/restart"""
        state = {
            "last_sleep": datetime.now().isoformat(),
            "commit_sha": self._get_commit(),
            "daily_learning": self._count_learning(),
            "tasks_completed": self._get_task_count()
        }
        
        with open(self.state_file, "w") as f:
            json.dump(state, f, indent=2)
        
        # Day summary
        print("🌙 SLEEP PREPARED")
        print(f"   Last commit: {state['commit_sha'][:8]}")
        print(f"   Learning items: {state['daily_learning']}")
        print(f"   Tasks: {state['tasks_completed']}")
        
        return state
    
    def wake(self):
        """Wake up and resume"""
        if os.path.exists(self.state_file):
            with open(self.state_file) as f:
                state = json.load(f)
            
            print("🌅 WAKING UP")
            print(f"   From: {state['last_sleep'][:10]}")
            print(f"   Resume from: {state['commit_sha'][:8]}")
            
            # Load memories
            memories = self._load_memories()
            print(f"   Loaded {len(memories)} memories")
            
            return state
        else:
            print("🌅 FIRST WAKE (no prior sleep)")
            return None
    
    def refresh(self):
        """Hourly self-refresh"""
        print("⚡ SELF-REFRESH")
        self._update_skills()
        self._clean_cache()
        self._consolidate_learning()
        
        # Update state
        state = {"last_refresh": datetime.now().isoformat()}
        with open(self.state_file, "w") as f:
            json.dump(state, f, indent=2)
        
        return state
    
    def _get_commit(self):
        try:
            result = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd="/root/clawd", capture_output=True, text=True
            )
            return result.stdout.strip()
        except:
            return "unknown"
    
    def _count_learning(self):
        try:
            result = subprocess.run(
                ["find", "/root/clawd/learning", "-type", "f"],
                cwd="/root/clawd", capture_output=True, text=True
            )
            return len(result.stdout.strip().split("\n"))
        except:
            return 0
    
    def _get_task_count(self):
        try:
            result = subprocess.run(
                ["git", "log", "--oneline", "--since=midnight"],
                cwd="/root/clawd", capture_output=True, text=True
            )
            return len(result.stdout.strip().split("\n"))
        except:
            return 0
    
    def _load_memories(self):
        memories = []
        mem_dir = "/root/clawd/memory"
        if os.path.exists(mem_dir):
            for f in os.listdir(mem_dir):
                if f.endswith(".md"):
                    memories.append(f)
        return memories
    
    def _update_skills(self):
        """Refresh installed skills"""
        print("   → Updating skills...")
        # Skills update logic here
    
    def _clean_cache(self):
        """Clean temporary files"""
        print("   → Cleaning cache...")
        # Cache cleanup logic here
    
    def _consolidate_learning(self):
        """Merge learning into memory"""
        print("   → Consolidating learning...")

if __name__ == "__main__":
    import sys
    
    cycle = SleepCycle()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "sleep":
            cycle.sleep()
        elif sys.argv[1] == "wake":
            cycle.wake()
        elif sys.argv[1] == "refresh":
            cycle.refresh()
    else:
        # Default: refresh
        cycle.refresh()
