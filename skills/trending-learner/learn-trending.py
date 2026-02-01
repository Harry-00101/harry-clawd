#!/usr/bin/env python3
"""
GitHub Trending Auto-Learner
Every 30 minutes: Fetch → Learn → Try → Production
"""

import requests
import subprocess
import os
from datetime import datetime

LOG_FILE = "/root/clawd/logs/trending-learner.log"

def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {msg}")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{ts}] {msg}\n")

# Curated list of high-quality AI/Automation repos
TRENDING_REPOS = [
    {"org": "microsoft", "repo": "BitNet", "desc": "1-bit LLM inference"},
    {"org": "mendableai", "repo": "firecrawl", "desc": "Web scraping for AI"},
    {"org": "anthropics", "repo": "claude-code", "desc": "Agentic coding tool"},
    {"org": "openclaw", "repo": "openclaw", "desc": "AI assistant"},
    {"org": "dify-ai", "repo": "dify", "desc": "LLM app platform"},
    {"org": "mindee", "repo": "doctr", "desc": "Document OCR"},
    {"org": "1bitllm", "repo": "bitnet_b1_58-large", "desc": "1-bit LLM models"},
]

def get_github_stars(org, repo):
    """Get star count from GitHub API."""
    try:
        r = requests.get(f"https://api.github.com/repos/{org}/{repo}", timeout=5)
        if r.status_code == 200:
            return r.json().get("stargazers_count", 0)
    except:
        pass
    return None

def fetch_trending():
    """Fetch trending AI repos."""
    log("Fetching trending AI repos...")
    repos = []
    
    for item in TRENDING_REPOS:
        name = f"{item['org']}/{item['repo']}"
        stars = get_github_stars(item['org'], item['repo'])
        
        repos.append({
            "name": name,
            "stars": f"{stars:,}" if stars else "N/A",
            "description": item['desc'],
            "url": f"https://github.com/{name}",
            "org": item['org'],
            "repo": item['repo']
        })
        log(f"  {name}: {stars} stars" if stars else f"  {name}: N/A")
    
    return repos

def analyze_repo(repo):
    """Check if should learn."""
    keywords = ["llm", "ai", "agent", "automation", "python", "api", "scraper", "ocr", "assistant", "tool"]
    text = (repo["name"] + " " + repo["description"]).lower()
    return any(k in text for k in keywords)

def create_learning(repo):
    """Create learning file."""
    safe_name = repo["name"].replace("/", "-")
    path = f"/root/clawd/learning/trending/{safe_name}.md"
    
    content = f"""# {repo['name']}

**Stars:** {repo['stars']}  
**URL:** {repo['url']}

> {repo['description']}

**Auto-learned:** {datetime.now().isoformat()}

## Learn→Try→Production

- [ ] Learn - Research this repo
- [ ] Try - Test functionality  
- [ ] Production - Integrate into Harry-001

"""
    
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)
    
    log(f"Created: {repo['name']}")
    return path

def commit_to_private():
    """Commit changes."""
    log("Committing to private repo...")
    try:
        subprocess.run(["git", "add", "-A"], cwd="/root/clawd", capture_output=True)
        result = subprocess.run([
            "git", "commit", "-m", f"Auto-learn: GitHub Trending {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        ], cwd="/root/clawd", capture_output=True, text=True)
        
        if "nothing to commit" not in result.stdout:
            subprocess.run(["git", "push", "-f", "private", "master:main"], cwd="/root/clawd", capture_output=True)
            log("✅ Committed to private repo")
        else:
            log("No new repos")
    except Exception as e:
        log(f"Error: {e}")

def main():
    log("=" * 50)
    log("GitHub Trending Auto-Learner")
    log("=" * 50)
    
    repos = fetch_trending()
    learned = 0
    
    for repo in repos:
        if analyze_repo(repo):
            create_learning(repo)
            learned += 1
    
    log(f"Learned {learned} repos")
    
    if learned > 0:
        commit_to_private()
    
    log("Done")
    return learned

if __name__ == "__main__":
    main()
