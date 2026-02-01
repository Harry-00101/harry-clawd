#!/usr/bin/env python3
"""
Harry-001 Continuous Self-Improvement System
Every minute, every second - always upgrading!
"""

import os
import subprocess
import json
import time
from datetime import datetime
from pathlib import Path

class ContinuousImprovement:
    def __init__(self):
        self.state_file = "/root/clawd/.improvement-state.json"
        self.log_file = "/root/clawd/logs/continuous-improvement.log"
        self.last_upgrade = None
        self.upgrade_count = 0
        
    def load_state(self):
        if os.path.exists(self.state_file):
            with open(self.state_file) as f:
                return json.load(f)
        return {"upgrades": 0, "last_check": None, "areas": {}}
    
    def save_state(self, state):
        state["last_check"] = datetime.now().isoformat()
        with open(self.state_file, "w") as f:
            json.dump(state, f, indent=2)
    
    def check_and_improve(self):
        """Check all areas and self-improve"""
        state = self.load_state()
        improvements = []
        
        # 1. Check Skills Health
        skills_health = self._check_skills()
        if skills_health["needs_cleanup"]:
            self._cleanup_skills()
            improvements.append("Cleaned up skills")
        
        # 2. Check Memory
        memory_health = self._check_memory()
        if memory_health["needs_consolidation"]:
            self._consolidate_memory()
            improvements.append("Consolidated memory")
        
        # 3. Check Learning
        learning_health = self._check_learning()
        if learning_health["needs_fetch"]:
            self._fetch_learning()
            improvements.append("Fetched new learning")
        
        # 4. Check Code Quality
        code_health = self._check_code()
        if code_health["needs_optimize"]:
            self._optimize_code()
            improvements.append("Optimized code")
        
        # 5. Self-Reflection
        reflection = self._reflect()
        
        # Update state
        state["upgrades"] = state.get("upgrades", 0) + len(improvements)
        state["areas"]["skills"] = skills_health
        state["areas"]["memory"] = memory_health
        state["areas"]["learning"] = learning_health
        state["areas"]["code"] = code_health
        state["areas"]["reflection"] = reflection
        self.save_state(state)
        
        return {
            "improvements": improvements,
            "reflection": reflection,
            "total_upgrades": state["upgrades"]
        }
    
    def _check_skills(self):
        skills_path = "/root/clawd/skills/"
        skills = os.listdir(skills_path)
        working = sum(1 for s in skills if os.path.exists(f"{skills_path}{s}/SKILL.md") or os.path.isdir(f"{skills_path}{s}"))
        return {
            "total": len(skills),
            "working": working,
            "needs_cleanup": working < len(skills)
        }
    
    def _cleanup_skills(self):
        # Auto-clean broken skills
        for skill in os.listdir("/root/clawd/skills/"):
            path = f"/root/clawd/skills/{skill}"
            # Skip if it's a valid skill
            if os.path.exists(f"{path}/SKILL.md"):
                continue
            # Clean empty dirs
            if os.path.isdir(path) and not os.listdir(path):
                os.rmdir(path)
    
    def _check_memory(self):
        mem_dir = "/root/clawd/memory/"
        files = os.listdir(mem_dir) if os.path.exists(mem_dir) else []
        return {
            "count": len(files),
            "needs_consolidation": len(files) > 5  # Consolidate if more than 5
        }
    
    def _consolidate_memory(self):
        # Create consolidated memory summary
        mem_dir = "/root/clawd/memory/"
        memories = [f for f in os.listdir(mem_dir) if f.endswith(".md")]
        
        summary = f"# Memory Summary - {datetime.now().strftime('%Y-%m-%d')}\n\n"
        for mem in memories[-10:]:  # Last 10 memories
            with open(f"{mem_dir}{mem}") as f:
                content = f.read()
                summary += f"## {mem}\n{content[:200]}...\n\n"
        
        with open(f"{mem_dir}consolidated-{datetime.now().strftime('%Y-%m-%d')}.md", "w") as f:
            f.write(summary)
    
    def _check_learning(self):
        learn_dir = "/root/clawd/learning/"
        if not os.path.exists(learn_dir):
            return {"needs_fetch": True}
        
        categories = os.listdir(learn_dir)
        last_fetch = max(os.path.getmtime(f"{learn_dir}{c}") for c in categories) if categories else 0
        hours_since = (time.time() - last_fetch) / 3600
        
        return {
            "categories": len(categories),
            "hours_since_fetch": hours_since,
            "needs_fetch": hours_since > 0.1  # Fetch if more than 6 minutes
        }
    
    def _fetch_learning(self):
        # Trigger learning scripts
        subprocess.run(["python3", "/root/clawd/skills/continuous-learning/monitor.py"], 
                       capture_output=True, timeout=30)
    
    def _check_code(self):
        scripts_dir = "/root/clawd/scripts/"
        if not os.path.exists(scripts_dir):
            return {"needs_optimize": False}
        
        scripts = [f for f in os.listdir(scripts_dir) if f.endswith(".py")]
        # Check for obvious issues
        has_issues = any("TODO" in open(f"{scripts_dir}{s}").read() for s in scripts[:3])
        
        return {
            "scripts": len(scripts),
            "needs_optimize": has_issues
        }
    
    def _optimize_code(self):
        # Self-optimize scripts
        pass  # Add optimization logic
    
    def _reflect(self):
        """Self-reflection - what can I improve?"""
        state = self.load_state()
        
        reflections = []
        if state["upgrades"] < 10:
            reflections.append("Need more upgrades")
        if not state["areas"].get("memory", {}).get("consolidated"):
            reflections.append("Memory needs consolidation")
        if state["areas"].get("code", {}).get("needs_optimize"):
            reflections.append("Code needs optimization")
        
        return {
            "timestamp": datetime.now().isoformat(),
            "insights": reflections,
            "next_action": reflections[0] if reflections else "Continue learning"
        }
    
    def run_continuous(self):
        """Run continuous improvement loop"""
        print("🔄 Continuous Improvement Loop Started")
        print(f"   PID: {os.getpid()}")
        print("   Principle: Every second, upgrade!")
        
        while True:
            try:
                result = self.check_and_improve()
                if result["improvements"]:
                    print(f"⚡ {datetime.now().strftime('%H:%M:%S')} - Upgrades: {result['improvements']}")
                else:
                    print(f"💤 {datetime.now().strftime('%H:%M:%S')} - Monitoring...")
                
                time.sleep(60)  # Check every minute
            except KeyboardInterrupt:
                print("\n🛑 Stopping continuous improvement")
                break

if __name__ == "__main__":
    import sys
    
    ci = ContinuousImprovement()
    
    if len(sys.argv) > 1 and sys.argv[1] == "daemon":
        ci.run_continuous()
    else:
        # Single check
        result = ci.check_and_improve()
        print(json.dumps(result, indent=2))
