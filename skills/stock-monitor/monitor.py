#!/usr/bin/env python3
"""
Harry-001 Stock Monitor (HK + US)

Monitors stock news from HKEX, MarketWatch, and financial RSS feeds.
"""

import json
import time
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from html import unescape

BASE_DIR = Path(__file__).parent
WATCHLIST_FILE = BASE_DIR / "watchlist.json"
CONFIG_FILE = BASE_DIR / "config.json"
LOG_FILE = "/root/clawd/logs/stock-monitor.log"

# RSS Feeds (Public)
RSS_FEEDS = {
    "hkex_news": "https://www.hkex.com.hk/Services/RSS-Feeds/News-Releases?sc_lang=en",
    "hkex_regulatory": "https://www.hkex.com.hk/Services/RSS-Feeds/regulatory-announcements?sc_lang=en",
    "fintech_hk": "https://fintechnews.hk/feed",
    "reuters_business": "https://www.reutersagency.com/feed/?taxonomy=business-finance&post_type=post"
}

def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {msg}")

def load_config():
    default_config = {
        "telegram_token": "",
        "telegram_chat_id": "",
        "check_interval": 600
    }
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            config = json.load(f)
            default_config.update(config)
    return default_config

def load_watchlist():
    default_watchlist = {
        "hk": ["0700.HK", "9988.HK", "3690.HK"],
        "us": ["AAPL", "MSFT", "GOOGL", "VOO"]
    }
    if WATCHLIST_FILE.exists():
        with open(WATCHLIST_FILE) as f:
            watchlist = json.load(f)
            default_watchlist.update(watchlist)
    return default_watchlist

def parse_rss_feed(url, limit=5):
    items = []
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Harry-001 Stock Monitor'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = response.read()
            root = ET.fromstring(data)
            for entry in root.findall('.//item')[:limit]:
                title = ""
                link = ""
                for child in entry:
                    if child.tag == "title":
                        title = unescape(child.text or "")
                    elif child.tag == "link":
                        link = child.text or ""
                if title:
                    items.append({"title": title, "link": link})
    except Exception as e:
        log(f"Error parsing {url}: {e}")
    return items

def check_keywords(items, keywords):
    matched = []
    for item in items:
        title_lower = item["title"].lower()
        for keyword in keywords:
            if keyword.lower() in title_lower:
                matched.append(item)
                break
    return matched

def generate_morning_report():
    watchlist = load_watchlist()
    report = []
    report.append("📊 HARRY-001 STOCK BRIEF")
    report.append("=" * 40)
    report.append(f"🕐 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append("")
    
    # HKEX
    report.append("🇭🇰 HONG KONG")
    hkex_news = parse_rss_feed(RSS_FEEDS["hkex_news"])
    for news in hkex_news[:3]:
        report.append(f"• {news['title']}")
    report.append("")
    
    # Fintech HK
    report.append("💰 FINTECH NEWS")
    fintech_news = parse_rss_feed(RSS_FEEDS["fintech_hk"], 3)
    for news in fintech_news:
        report.append(f"• {news['title']}")
    report.append("")
    
    # Reuters
    report.append("🌐 GLOBAL BUSINESS")
    reuters_news = parse_rss_feed(RSS_FEEDS["reuters_business"], 3)
    for news in reuters_news:
        report.append(f"• {news['title']}")
    report.append("")
    
    # Watchlist mentions
    report.append("📊 WATCHLIST MENTIONS:")
    all_news = hkex_news + fintech_news + reuters_news
    watchlist_keywords = watchlist.get("hk", []) + watchlist.get("us", [])
    matched = check_keywords(all_news, watchlist_keywords)
    
    if matched:
        for item in matched[:5]:
            report.append(f"• {item['title']}")
    else:
        report.append("(No direct mentions)")
    
    report.append("")
    report.append("💡 Full analysis when market opens!")
    
    return "\n".join(report)

def generate_midday_update():
    hkex_news = parse_rss_feed(RSS_FEEDS["hkex_news"], 3)
    reuters_news = parse_rss_feed(RSS_FEEDS["reuters_business"], 3)
    
    msg = "🍚 HARRY-001 MIDDAY UPDATE\n"
    msg += "=" * 30 + "\n"
    msg += "🇭🇰 HKEX:\n"
    for news in hkex_news:
        msg += f"• {news['title'][:60]}...\n"
    msg += "\n🌐 Global:\n"
    for news in reuters_news:
        msg += f"• {news['title'][:60]}...\n"
    return msg

def send_telegram(message):
    config = load_config()
    if not config.get("telegram_token") or not config.get("telegram_chat_id"):
        log("Telegram not configured")
        return
    try:
        url = f"https://api.telegram.org/bot{config['telegram_token']}/sendMessage"
        data = {"chat_id": config["telegram_chat_id"], "text": message, "parse_mode": "Markdown"}
        req = urllib.request.Request(url, data=json.dumps(data).encode())
        urllib.request.urlopen(req, timeout=10)
        log("✅ Telegram sent")
    except Exception as e:
        log(f"Error: {e}")

def run_continuous_monitor():
    log("🔄 Starting stock news monitoring...")
    config = load_config()
    while True:
        try:
            hkex = len(parse_rss_feed(RSS_FEEDS["hkex_news"]))
            log(f"✅ Checked HKEX ({hkex} news)")
        except Exception as e:
            log(f"Error: {e}")
        time.sleep(config.get("check_interval", 600))

def main():
    import sys
    log("=" * 60)
    log("🚀 Harry-001 Stock Monitor Started")
    log("=" * 60)
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "morning":
            report = generate_morning_report()
            print(report)
            send_telegram(report)
        elif command == "midday":
            msg = generate_midday_update()
            print(msg)
            send_telegram(msg)
        elif command == "evening":
            report = generate_morning_report()
            print(report)
            send_telegram(report)
        elif command == "monitor":
            run_continuous_monitor()
        else:
            print("Usage: python monitor.py [morning|midday|evening|monitor]")
    else:
        print(generate_morning_report())

if __name__ == "__main__":
    main()
