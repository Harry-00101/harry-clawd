#!/usr/bin/env python3
"""
Harry-001 README Auto-Updater
Keeps README.md updated with latest stats
"""

import subprocess
import os
from datetime import datetime

def get_git_stats():
    result = subprocess.run(
        ["git", "log", "--oneline", "--since=midnight"],
        cwd="/root/clawd", capture_output=True, text=True
    )
    today_commits = len(result.stdout.strip().split("\n")) if result.stdout.strip() else 0
    
    result = subprocess.run(
        ["git", "rev-list", "--count", "HEAD"],
        cwd="/root/clawd", capture_output=True, text=True
    )
    total_commits = int(result.stdout.strip()) if result.stdout.strip() else 0
    
    return {"today": today_commits, "total": total_commits}

def get_skills_count():
    skills_path = "/root/clawd/skills/"
    if os.path.exists(skills_path):
        return len([d for d in os.listdir(skills_path) if os.path.isdir(f"{skills_path}{d}")])
    return 0

def get_mcp_count():
    mcp_path = "/root/clawd/.mcp-servers/"
    if os.path.exists(mcp_path):
        return len(os.listdir(mcp_path))
    return 0

def get_learning_count():
    learning_path = "/root/clawd/learning/"
    if os.path.exists(learning_path):
        return len([d for d in os.listdir(learning_path) if os.path.isdir(f"{learning_path}{d}")])
    return 0

def get_upgrades_count():
    log_file = "/root/clawd/logs/continuous-improvement.log"
    if os.path.exists(log_file):
        with open(log_file) as f:
            content = f.read()
            return content.count("Upgraded")
    return 0

def get_current_version():
    version_file = "/root/clawd/.version"
    if os.path.exists(version_file):
        with open(version_file) as f:
            return f.read().strip()
    return "v4.0"

def update_readme():
    readme_path = "/root/clawd/README.md"
    
    if not os.path.exists(readme_path):
        print("README.md not found")
        return False
    
    with open(readme_path) as f:
        content = f.read()
    
    stats = {
        "version": get_current_version(),
        "skills": get_skills_count(),
        "mcp": get_mcp_count(),
        "learning": get_learning_count(),
        "today_commits": get_git_stats()["today"],
        "total_commits": get_git_stats()["total"],
        "upgrades": get_upgrades_count(),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    
    new_stats = f'''## 📈 Real-Time Stats

| Metric | Value | Last Updated |
|--------|-------|--------------|
| **Version** | {stats["version"]} | {stats["time"]} |
| **Skills** | {stats["skills"]} | - |
| **MCP Servers** | {stats["mcp"]} | - |
| **Learning Categories** | {stats["learning"]} | - |
| **Today's Commits** | {stats["today_commits"]} | Today |
| **Total Commits** | {stats["total_commits"]} | All time |
| **Self-Upgrades** | {stats["upgrades"]} | All time |

*Stats automatically updated every hour*

'''
    
    if "## 📈 Stats" in content:
        start = content.find("## 📈 Stats")
        end = content.find("\n## ", start + 10)
        if end == -1:
            end = len(content)
        new_content = content[:start] + new_stats + content[end:]
    else:
        insert_point = content.find("## 🎖️ Unique Identity System")
        if insert_point == -1:
            print("Could not find insertion point")
            return False
        end_of_line = content.find("\n", insert_point)
        new_content = content[:end_of_line+1] + "\n" + new_stats + content[end_of_line+1:]
    
    with open(readme_path, "w") as f:
        f.write(new_content)
    
    print(f"README.md updated! {stats['time']}")
    print(f"   Skills: {stats['skills']}, MCP: {stats['mcp']}, Commits: {stats['today_commits']}")
    return True

if __name__ == "__main__":
    update_readme()
