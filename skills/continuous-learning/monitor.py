#!/usr/bin/env python3
"""
24/7 Continuous Learning System
Monitors: Financial, Workplace, AI, Tech, HK Sources
"""

import requests
import subprocess
import os
import time
import feedparser
from datetime import datetime

LOG_FILE = "/root/clawd/logs/continuous-learning.log"
LEARNING_DIR = "/root/clawd/learning"

def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {msg}")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{ts}] {msg}\n")

# HK Tech RSS Feeds (NEW!)
HK_RSS_FEEDS = {
    "fintech_news_hk": {
        "url": "https://fintechnews.hk/feed/",
        "filter": ["fintech", "finance", "hong kong", "ai", "technology", "blockchain", "payment"],
        "language": "en"
    },
    "techcrunch_hk": {
        "url": "https://techcrunch.com/tag/hong-kong/feed/",
        "filter": ["hong kong", "startup", "ai", "fintech", "technology"],
        "language": "en"
    },
    "hk_it_federation": {
        "url": "https://www.hkitf.org.hk/feed",
        "filter": ["technology", "ai", "business", "innovation"],
        "language": "en"
    },
    "unwire_hk": {
        "url": "https://unwire.hk/feed/",
        "filter": ["科技", "AI", "香港", "金融", "股票", "人工智能", "科技新聞"],
        "language": "zh"
    },
    "pts_tech": {
        "url": "https://www.ptsconsulting.com.hk/feed/",
        "filter": ["technology", "ai", "cybersecurity", "cloud"],
        "language": "en"
    },
}

# Sources to monitor
SOURCES = {
    # Financial Sources
    "github_finance": {
        "url": "https://api.github.com/search/repositories?q=stars:today&sort=stars&per_page=15",
        "filter": ["finance", "stock", "trading", "invest", "crypto", "bitcoin", "python", "api", "yfinance", "pandas", "quant"]
    },
    "hacker_news_finance": {
        "url": "https://hacker-news.firebaseio.com/v0/topstories.json",
        "filter": ["finance", "stock", "trading", "invest", "crypto", "bitcoin", "yfinance", "quant"]
    },
    
    # Workplace/Productivity Sources
    "github_productivity": {
        "url": "https://api.github.com/search/repositories?q=stars:today&sort=stars&per_page=15",
        "filter": ["productivity", "automation", "workflow", "notion", "todoist", "calendar", "task", "project", "management"]
    },
    
    # AI/Tech Sources
    "github_ai": {
        "url": "https://api.github.com/search/repositories?q=stars:today&sort=stars&per_page=15",
        "filter": ["llm", "ai", "agent", "automation", "python", "api", "tool"]
    },
    "arxiv_ai": {
        "url": "http://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=submittedDate&sortOrder=desc&max_results=10",
        "filter": ["transformer", "llm", "agent", "reasoning", "finance", "trading"]
    },
    "hacker_news": {
        "url": "https://hacker-news.firebaseio.com/v0/topstories.json",
        "filter": ["ai", "llm", "agent", "automation", "finance", "stock", "productivity"]
    }
}

def learn_hk_rss_feeds():
    """Learn from Hong Kong Tech RSS Feeds (NEW!)."""
    log("🇭🇰 Learning: HK Tech RSS Feeds...")
    
    for feed_name, feed_info in HK_RSS_FEEDS.items():
        try:
            log(f"  📰 Parsing: {feed_name}")
            feed = feedparser.parse(feed_info["url"])
            
            if feed.bozo:
                log(f"  ⚠️ Error parsing {feed_name}")
                continue
            
            count = 0
            for entry in feed.entries[:5]:  # Top 5 from each feed
                title = entry.get("title", "")
                summary = entry.get("summary", "")[:300]
                link = entry.get("link", "")
                
                # Filter by keywords
                content = (title + " " + summary).lower()
                for keyword in feed_info["filter"]:
                    if keyword.lower() in content:
                        save_learning(f"ss-{feed_namehk-r}-{entry.get('id', title[:20])}", {
                            "source": f"HK RSS: {feed_name}",
                            "title": title,
                            "summary": summary,
                            "url": link,
                            "type": "hk-tech-news",
                            "language": feed_info["language"]
                        })
                        count += 1
                        break
            
            log(f"    ✅ Learned {count} articles from {feed_name}")
            
        except Exception as e:
            log(f"  ⚠️ Error with {feed_name}: {e}")
    
    log("  📊 HK RSS Learning Complete")

def learn_github_finance():
    """Learn from GitHub finance/trading repos."""
    log("💰 Learning: GitHub Finance...")
    try:
        r = requests.get(SOURCES["github_finance"]["url"], timeout=10)
        if r.status_code == 200:
            data = r.json()
            count = 0
            for item in data.get("items", [])[:5]:
                name = item["full_name"]
                desc = item.get("description", "").lower()
                for keyword in SOURCES["github_finance"]["filter"]:
                    if keyword.lower() in desc:
                        save_learning(f"github-finance-{name}", {
                            "source": "GitHub Finance",
                            "name": name,
                            "stars": item["stargazers_count"],
                            "description": item.get("description", ""),
                            "url": item["html_url"],
                            "type": "finance-repo"
                        })
                        count += 1
                        break
            log(f"  ✅ Learned {count} finance repos")
    except Exception as e:
        log(f"  ⚠️ Error: {e}")

def learn_github_productivity():
    """Learn from GitHub productivity/workplace repos."""
    log("💼 Learning: GitHub Productivity...")
    try:
        r = requests.get(SOURCES["github_productivity"]["url"], timeout=10)
        if r.status_code == 200:
            data = r.json()
            count = 0
            for item in data.get("items", [])[:5]:
                name = item["full_name"]
                desc = item.get("description", "").lower()
                for keyword in SOURCES["github_productivity"]["filter"]:
                    if keyword.lower() in desc:
                        save_learning(f"github-prod-{name}", {
                            "source": "GitHub Productivity",
                            "name": name,
                            "stars": item["stargazers_count"],
                            "description": item.get("description", ""),
                            "url": item["html_url"],
                            "type": "productivity-repo"
                        })
                        count += 1
                        break
            log(f"  ✅ Learned {count} productivity repos")
    except Exception as e:
        log(f"  ⚠️ Error: {e}")

def learn_github_ai():
    """Learn from GitHub AI repos."""
    log("🤖 Learning: GitHub AI...")
    try:
        r = requests.get(SOURCES["github_ai"]["url"], timeout=10)
        if r.status_code == 200:
            data = r.json()
            count = 0
            for item in data.get("items", [])[:5]:
                name = item["full_name"]
                desc = item.get("description", "").lower()
                for keyword in SOURCES["github_ai"]["filter"]:
                    if keyword.lower() in desc:
                        save_learning(f"github-ai-{name}", {
                            "source": "GitHub AI",
                            "name": name,
                            "stars": item["stargazers_count"],
                            "description": item.get("description", ""),
                            "url": item["html_url"],
                            "type": "ai-repo"
                        })
                        count += 1
                        break
            log(f"  ✅ Learned {count} AI repos")
    except Exception as e:
        log(f"  ⚠️ Error: {e}")

def learn_arxiv_papers():
    """Learn from arXiv AI papers."""
    log("📚 Learning: arXiv AI Papers...")
    try:
        r = requests.get(SOURCES["arxiv_ai"]["url"], timeout=10)
        if r.status_code == 200:
            import xml.etree.ElementTree as ET
            root = ET.fromstring(r.content)
            count = 0
            for entry in root.findall("{http://www.w3.org/2005/Atom}entry")[:5]:
                title = entry.find("{http://www.w3.org/2005/Atom}title").text.strip()
                summary = entry.find("{http://www.w3.org/2005/Atom}summary").text.strip()
                link = entry.find("{http://www.w3.org/2005/Atom}id").text
                for keyword in SOURCES["arxiv_ai"]["filter"]:
                    if keyword.lower() in title.lower():
                        save_learning(f"arxiv-{title[:30]}", {
                            "source": "arXiv",
                            "title": title,
                            "summary": summary[:300],
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
        r = requests.get(SOURCES["hacker_news"]["url"], timeout=10)
        if r.status_code == 200:
            top_ids = r.json()[:15]
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

**Description:** {data.get('description') or data.get('summary', '')[:400]}

**Score:** {data.get('stars') or data.get('score', 'N/A')}

## Learn→Try→Production
- [ ] Learn
- [ ] Try
- [ ] Production

## Tags
{data.get('type', '')}
{data.get('language', '')}
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
    log("🔄 24/7 Continuous Learning System (with HK RSS!)")
    log("=" * 60)
    
    while True:
        log("\n--- Learning Cycle ---")
        
        # 🇭🇰 HK Tech RSS (NEW!)
        learn_hk_rss_feeds()
        
        # Financial Learning
        learn_github_finance()
        
        # Workplace/Productivity Learning
        learn_github_productivity()
        
        # AI/Tech Learning
        learn_github_ai()
        learn_arxiv_papers()
        learn_hacker_news()
        
        # Commit
        commit_all()
        
        log("--- Cycle Complete, sleeping 5 minutes ---\n")
        time.sleep(300)  # 5 minutes

if __name__ == "__main__":
    os.makedirs(f"{LEARNING_DIR}/continuous", exist_ok=True)
    main()
