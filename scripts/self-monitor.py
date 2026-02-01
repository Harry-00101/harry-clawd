#!/usr/bin/env python3
"""
Harry-001 Self-Monitoring System
Monitors system health and self-improves
"""

import subprocess
import json
import os
from datetime import datetime

class SelfMonitor:
    def __init__(self):
        self.metrics = {}
    
    def check_skills(self):
        """Check skill health"""
        skills_path = "/root/clawd/skills/"
        skills = os.listdir(skills_path)
        working = sum(1 for s in skills if os.path.exists(f"{skills_path}{s}/SKILL.md"))
        return {"total": len(skills), "working": working}
    
    def check_memory(self):
        """Check memory files"""
        memory_path = "/root/clawd/memory/"
        if os.path.exists(memory_path):
            files = os.listdir(memory_path)
            return {"memory_files": len(files)}
        return {"memory_files": 0}
    
    def check_learning(self):
        """Check learning progress"""
        learning_path = "/root/clawd/learning/"
        if os.path.exists(learning_path):
            dirs = os.listdir(learning_path)
            return {"learning_categories": len(dirs)}
        return {"learning_categories": 0}
    
    def generate_report(self):
        """Generate self-improvement report"""
        self.metrics = {
            "timestamp": datetime.now().isoformat(),
            "skills": self.check_skills(),
            "memory": self.check_memory(),
            "learning": self.check_learning()
        }
        
        # Identify improvements
        improvements = []
        if self.metrics["skills"]["working"] < self.metrics["skills"]["total"]:
            improvements.append("Remove broken skills")
        if self.metrics["memory"]["memory_files"] == 0:
            improvements.append("Create more memories")
        
        self.metrics["improvements"] = improvements
        return self.metrics
    
    def save_report(self):
        """Save and potentially act on report"""
        report = self.generate_report()
        with open("/root/clawd/logs/self-monitor.json", "w") as f:
            json.dump(report, f, indent=2)
        return report

if __name__ == "__main__":
    monitor = SelfMonitor()
    report = monitor.save_report()
    print(json.dumps(report, indent=2))
