# kafroc/LOFMonitor

**LOF基金溢价监控系统 (LOF Fund Premium/Discount Monitoring System)**

**URL:** https://github.com/kafroc/LOFMonitor
**Stars:** 1 ⭐
**Language:** Python (Chinese)

**Added:** 2026-02-01 03:43

## 🎯 What It Does

Real-time monitoring tool for LOF基金 (Listed Open-Ended Funds):
- **Premium/Discount Monitoring**: Tracks price vs NAV (Net Asset Value)
- **Dual Data Sources**: On-exchange (Sina/AkShare) + Off-exchange (EastMoney)
- **Smart Alerts**: DingTalk notifications with daily deduplication
- **Dual Modes**: GUI (tkinter) + CLI (async streaming)

## ✨ Features

### Core Features
| Feature | Description |
|---------|-------------|
| **Real-time Monitoring** | Sync on-exchange prices + off-exchange NAV |
| **Precision Calculation** | Calculate premium/discount rates |
| **Smart Alerts** | DingTalk bot notifications |
| **Deduplication** | One alert per fund per day |
| **Status Detection** | Detect suspended trading/creation/redemption |

### User Experience
| Mode | Description |
|------|-------------|
| **GUI Mode** | Dark theme, dynamic sorting, search filtering |
| **CLI Mode** | Async streaming output, real-time display |

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  LOFMonitor Architecture                │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │
│  │   Data      │  │  Calculator │  │  Notifier   │    │
│  │  Fetcher    │  │             │  │             │    │
│  │(AkShare/    │  │ Premium/    │  │ DingTalk    │    │
│  │ Beautiful   │  │ Discount    │  │ Alerts      │    │
│  │  Soup)      │  │ Calc        │  │             │    │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘    │
│         │                │                │            │
│         └────────────────┼────────────────┘            │
│                          ▼                              │
│                 ┌─────────────────┐                    │
│                 │   Config/Log    │                    │
│                 │   (JSON)        │                    │
│                 └────────┬────────┘                    │
│                          │                              │
│         ┌────────────────┼────────────────┐            │
│         ▼                ▼                ▼            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐   │
│  │     UI      │  │     CLI     │  │  Logger     │   │
│  │  (tkinter)  │  │  (Async)    │  │  (File)     │   │
│  └─────────────┘  └─────────────┘  └─────────────┘   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## 📁 Key Files

| File | Purpose |
|------|---------|
| `data_fetcher.py` | Fetch data from AkShare + EastMoney |
| `calculator.py` | Calculate premium/discount rates |
| `notifier.py` | DingTalk alert system |
| `ui.py` | GUI (tkinter) |
| `cli.py` | Terminal mode |
| `config.py` | Configuration management |
| `main.py` | Entry point |

## 🔧 Tech Stack

| Component | Technology |
|-----------|-----------|
| **Data** | AkShare, requests, BeautifulSoup |
| **GUI** | tkinter (dark theme) |
| **CLI** | asyncio, async streaming |
| **Notifications** | DingTalk bot |
| **Config** | JSON |
| **Logging** | Python logging |

## 🎯 For Harry-001

### Integration Possibilities
1. **Stock Analysis**: Similar premium/discount calculation for Hong Kong stocks
2. **Data Fetching**: AkShare for Chinese market data
3. **Alert System**: Integrate DingTalk/other notification channels
4. **CLI Mode**: Reference for async streaming output
5. **UI Design**: Dark theme patterns for Harry-001 Canvas

### Key Learnings
- **Modular Architecture**: Data → Calc → Notify → UI
- **Async Streaming**: Real-time CLI output without waiting
- **Smart Deduplication**: One alert per day per fund
- **Status Detection**: Parse complex trading states

## 📊 Comparison with Harry-001

| Aspect | LOFMonitor | Harry-001 |
|--------|-----------|-----------|
| **Focus** | Chinese LOF funds | Hong Kong stocks |
| **Data** | AkShare + EastMoney | yfinance + HKEX RSS |
| **Alerts** | DingTalk | Telegram |
| **UI** | tkinter | Canvas + CLI |
| **Mode** | GUI + CLI | Multi-channel |

## 🚀 Learn→Try→Production

- [x] Learn - Researched the repo
- [ ] Try - Test AkShare data fetching
- [ ] Production - Integrate LOF monitoring into Harry-001

## 📚 Related Skills

- [x] stock-analysis skill
- [x] financial research (Dexter)
- [x] continuous learning (HK RSS feeds)

## 🌐 Resources

- **AkShare:** https://akshare.xyz/ (Chinese financial data)
- **EastMoney:** https://www.eastmoney.com/ (Chinese financial portal)
- **DingTalk:** https://www.dingtalk.com/ (Alibaba's communication app)

---

**LOFMonitor: Reference for Chinese financial monitoring + async CLI + smart alerts! 📊🇨🇳**
