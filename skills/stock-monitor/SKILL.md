# Stock Monitor Skill (HK + US)

**Real-time stock monitoring for Hong Kong and US markets**

## 🎯 What It Does

```
┌─────────────────────────────────────────────────────────────┐
│              STOCK MONITOR SYSTEM                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                  DATA SOURCES                       │   │
│  │  🇭🇰 HK: HKEX RSS + yfinance                       │   │
│  │  🇺🇸 US: MarketWatch RSS + yfinance                │   │
│  │  📊 yfinance: Real-time stock data                 │   │
│  └─────────────────────────────────────────────────────┘   │
│                          │                                   │
│                          ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                  PROCESSING                         │   │
│  │  • Fetch latest data                               │   │
│  │  • Calculate metrics (price, change, volume)       │   │
│  │  • Detect alerts (price targets, news)             │   │
│  │  • Store in memory                                 │   │
│  └─────────────────────────────────────────────────────┘   │
│                          │                                   │
│                          ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                  OUTPUT                             │   │
│  │  • Telegram notifications                          │   │
│  │  • Daily reports (09:00, 12:00, 18:30)            │   │
│  │  • Real-time alerts                                │   │
│  │  • Web dashboard (optional)                        │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 📊 Data Sources

### Hong Kong (🇭🇰)
| Source | Type | Update Frequency |
|--------|------|------------------|
| **HKEX RSS** | News, announcements | Real-time |
| **yfinance HK** | Stock prices | 1-min delay |
| **unwire.hk** | Tech news | Hourly |

### United States (🇺🇸)
| Source | Type | Update Frequency |
|--------|------|------------------|
| **MarketWatch RSS** | Market news | Real-time |
| **yfinance US** | Stock prices | 1-min delay |
| **arXiv** | Research papers | Daily |

## 🎯 Key Features

### 1. Real-time Monitoring
- Price tracking for HK + US stocks
- Volume analysis
- Price change detection
- Volume spikes

### 2. News Integration
- HKEX announcements
- MarketWatch news
- unwire.hk tech news
- arXiv papers

### 3. Smart Alerts
- Price target reached
- Volume spike detection
- News sentiment changes
- Market open/close

### 4. Daily Reports
| Time | Report | Content |
|------|--------|---------|
| **09:00** | Morning Brief | Pre-market overview |
| **12:00** | Midday Update | Lunch-time summary |
| **18:30** | End of Day | Full day summary |

## 📈 Monitored Indices

### Hong Kong
| Index | Symbol | Description |
|-------|--------|-------------|
| **HSI** | ^HSI | Hang Seng Index |
| **HSCE** | ^HSCE | H-shares Index |
| **VOO** | VOO | Vanguard S&P 500 ETF |

### United States
| Index | Symbol | Description |
|-------|--------|-------------|
| **S&P 500** | ^GSPC | Standard & Poor's 500 |
| **NASDAQ** | ^IXIC | NASDAQ Composite |
| **DOW** | ^DJI | Dow Jones Industrial |

## 🔧 Installation

```bash
# Install dependencies
pip3 install yfinance pandas requests beautifulsoup4 feedparser

# Make executable
chmod +x /root/clawd/skills/stock-monitor/monitor.py
```

## 🚀 Usage

### Run Stock Monitor

```bash
# Start continuous monitoring
python3 /root/clawd/skills/stock-monitor/monitor.py &

# Or run specific report
python3 /root/clawd/skills/stock-monitor/monitor.py morning
python3 /root/clawd/skills/stock-monitor/monitor.py midday
python3 /root/clawd/skills/stock-monitor/monitor.py evening
```

### Add Stocks to Watchlist

Edit `/root/clawd/skills/stock-monitor/watchlist.json`:
```json
{
  "hk": ["0700.HK", "9988.HK", "3690.HK"],
  "us": ["AAPL", "MSFT", "GOOGL", "VOO"]
}
```

### Configure Alerts

Edit `/root/clawd/skills/stock-monitor/config.json`:
```json
{
  "price_alert_threshold": 0.05,
  "volume_spike_multiplier": 2.0,
  "telegram_token": "YOUR_TOKEN",
  "telegram_chat_id": "YOUR_CHAT_ID"
}
```

## 📁 Files

```
stock-monitor/
├── SKILL.md           # This file
├── monitor.py         # Main monitoring script
├── watchlist.json     # Stocks to watch
├── config.json        # Configuration
├── data_fetcher.py    # Fetch data from sources
├── analyzer.py        # Analyze data
├── notifier.py        # Send notifications
└── reports/           # Generated reports
```

## 🎯 Daily Workflow

```
06:00  → Fetch overnight data
07:00  → Morning weather + calendar
09:00  → Morning stock report
12:00  → Midday update
18:30  → End of day summary
19:00  → Evening news digest
23:45  → Commit + quiet mode
```

## 📊 Example Output

### Morning Report
```
📊 HARRY-001 MORNING STOCK BRIEF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🇭🇰 HONG KONG
📈 HSI: 19,000 (+0.5%)
📊 Volume: 2.1B shares
🔔 Watch: 0700.HK (Tencent)

🇺🇸 UNITED STATES  
📈 S&P 500: 4,500 (+0.3%)
📊 VOO: $420 (+0.25%)
🔔 Watch: AAPL, MSFT

📰 TOP NEWS
• HKEX: New listing announcement
• MarketWatch: Fed meeting notes
```

### Alert Notification
```
🔔 STOCK ALERT

0700.HK (Tencent)
Price: HK$350 (+2.5%)
Volume: 15M (+50% from avg)
Reason: Volume spike detected

9988.HK (Alibaba)
Price: HK$80 (-1.2%)
Reason: Price dropped below support
```

## 🔄 Integration with Harry-001

| Component | Integration |
|-----------|-------------|
| **Brain** | Uses reasoning to analyze trends |
| **Memory** | Stores historical data |
| **Nervous System** | Real-time data flow |
| **Automation** | Cron-based reports |
| **Telegram** | Notification delivery |

## 💰 Cost

| Component | Cost |
|-----------|------|
| **yfinance** | Free |
| **HKEX RSS** | Free |
| **MarketWatch RSS** | Free |
| **Server** | $5-10/month |
| **Total** | **~$5-10/month** |

## 📚 Related Skills

- [x] stock-analysis (yfinance + pandas-ta)
- [x] financial-research (Dexter)
- [x] continuous-learning (RSS feeds)
- [x] hk-tech-rss-feeds (HKEX RSS)

## 🎯 Next Steps

1. [ ] Set up watchlist with desired stocks
2. [ ] Configure Telegram notifications
3. [ ] Test data fetching
4. [ ] Run morning report
5. [ ] Monitor in real-time

---

**Harry-001 Stock Monitor: Your eyes on HK + US markets! 📊🇭🇰🇺🇸**
