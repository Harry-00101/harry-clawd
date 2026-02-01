#!/usr/bin/env python3
"""
24/7 Continuous Learning System
Watches multiple sources, learns continuously.
"""

import requests
import subprocess
import os
import time
from datetime import datetime

LOG_FILE = "/root/clawd/logs/continuous-learning.log"
LEARNING_DIR = "/root/clawd/learning"

def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {msg}")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{ts}] {msg}\n")

# Sources to monitor
SOURCES = {
    "github_trending": {
        "url": "https://api.github.com/search/repositories?q=stars:today&sort=stars&per_page=10",
        "filter": ["llm", "ai", "agent", "automation", "python", "api", "tool"]
    },
    "arxiv_cs_ai": {
        "url": "http://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=submittedDate&sortOrder=desc&max_results=10",
        "filter": ["transformer", "llm", "agent", "reasoning"]
    },
    "hacker_news": {
        "url": "https://hacker-news.firebaseio.com/v0/topstories.json",
        "filter": ["ai", "llm", "agent", "automation"]
    }
}

def learn_github_trending():
    """Learn from GitHub trending."""
    log("📡 Learning: GitHub Trending...")
    try:
        r = requests.get(SOURCES["github_trending"]["url"], timeout=10)
        if r.status_code == 200:
            data = r.json()
            for item in data.get("items", [])[:5]:
                name = item["full_name"]
                desc = item.get("description", "")
                url = item["html_url"]
                stars = item["stargazers_count"]
                
                save_learning(f"github-{name}", {
                    "source": "GitHub Trending",
                    "name": name,
                    "stars": stars,
                    "description": desc,
                    "url": url,
                    "type": "repository"
                })
            log(f"  ✅ Learned {len(data.get('items', []))} repos")
    except Exception as e:
        log(f"  ⚠️ Error: {e}")

def learn_arxiv_papers():
    """Learn from arXiv AI papers."""
    log("📚 Learning: arXiv AI Papers...")
    try:
        r = requests.get(SOURCES["arxiv_cs_ai"]["url"], timeout=10)
        if r.status_code == 200:
            # Parse RSS feed
            import xml.etree.ElementTree as ET
            root = ET.fromstring(r.content)
            
            count = 0
            for entry in root.findall("{http://www.w3.org/2005/Atom}entry")[:5]:
                title = entry.find("{http://www.w3.org/2005/Atom}title").text.strip()
                summary = entry.find("{http://www.w3.org/2005/Atom}summary").text.strip()
                link = entry.find("{http://www.w3.org/2005/Atom}id").text
                
                # Filter relevant papers
                for keyword in SOURCES["arxiv_cs_ai"]["filter"]:
                    if keyword.lower() in title.lower():
                        save_learning(f"arxiv-{title[:30]}", {
                            "source": "arXiv",
                            "title": title,
                            "summary": summary[:200],
                            "url": link,
                            "type": "paper"
                        })
                        count += 1
                        break
            
            log(f"  ✅ Learned {count} papers")
    except Exception as e:
        log(f"  ⚠️ Error: {e}")

def learn_hacker_news():
    """Learn from Hacker News."""
    log("📰 Learning: Hacker News...")
    try:
        # Get top stories
        r = requests.get(SOURCES["hacker_news"]["url"], timeout=10)
        if r.status_code == 200:
            top_ids = r.json()[:10]
            
            count = 0
            for story_id in top_ids:
                story_r = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json", timeout=5)
                if story_r.status_code == 200:
                    story = story_r.json()
                    title = story.get("title", "").lower()
                    
                    for keyword in SOURCES["hacker_news"]["filter"]:
                        if keyword in title:
                            save_learning(f"hn-{story_id}", {
                                "source": "Hacker News",
                                "title": story.get("title"),
                                "url": story.get("url", f"https://news.ycombinator.com/item?id={story_id}"),
                                "score": story.get("score"),
                                "type": "news"
                            })
                            count += 1
                            break
            
            log(f"  ✅ Learned {count} HN stories")
    except Exception as e:
        log(f"  ⚠️ Error: {e}")

def save_learning(key, data):
    """Save learning to file."""
    safe_key = key.replace("/", "-").replace(" ", "-")[:50]
    path = f"{LEARNING_DIR}/continuous/{safe_key}.md"
    
    content = f"""# {data.get('name') or data.get('title')}

**Source:** {data['source']}  
**Type:** {data['type']}  
**URL:** {data['url']}
**Added:** {datetime.now().isoformat()}

**Description:** {data.get('description') or data.get('summary', '')[:300]}

**Score:** {data.get('stars') or data.get('score', 'N/A')}

## Learn→Try→Production

- [ ] Learn
- [ ] Try
- [ ] Production

"""
    
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

def commit_all():
    """Commit all learnings."""
    log("💾 Committing to private repo...")
    try:
        subprocess.run(["git", "add", "-A"], cwd="/root/clawd", capture_output=True)
        subprocess.run([
            "git", "commit", "-m", f"Continuous Learning: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        ], cwd="/root/clawd", capture_output=True)
        subprocess.run(["git", "push", "-f", "private", "master:main"], cwd="/root/clawd", capture_output=True)
        log("✅ Committed")
    except Exception as e:
        log(f"⚠️ Commit error: {e}")

def main():
    """Main continuous learning loop."""
    log("=" * 60)
    log("🔄 24/7 Continuous Learning System Started")
    log("=" * 60)
    
    while True:
        log("\n--- Learning Cycle ---")
        
        # Learn from all sources
        learn_github_trending()
        learn_arxiv_papers()
        learn_hacker_news()
        
        # Commit
        commit_all()
        
        log("--- Cycle Complete, sleeping 5 minutes ---\n")
        time.sleep(300)  # 5 minutes

if __name__ == "__main__":
    os.makedirs(f"{LEARNING_DIR}/continuous", exist_ok=True)
    main()
