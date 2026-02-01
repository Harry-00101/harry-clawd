# QVerisBot Research
**Date:** 2026-02-01 15:05 UTC
**Project:** https://github.com/QVerisAI/QVerisBot

---

## 🎯 Overview

**QVerisBot** - OpenClaw with QVeris Universal Toolbox
- Your Professional AI Assistant with QVeris Universal Toolbox
- Based on **OpenClaw** (same as Harry-001!) 🦞
- Runs on your own devices

---

## 🔑 Core Feature: QVeris Universal Toolbox

**"App Store for AI tools"**

Connects your AI assistant to the world's data and services.

### 📊 Data Provider Categories (500+ total)

| Category | Providers | Examples |
|----------|-----------|----------|
| 💰 Finance & Markets | 80+ | Binance, AlphaVantage, Finnhub |
| 🔍 Search & Web Intelligence | 45+ | Brave Search, SerpApi, Google |
| 🏢 Business Intelligence | 40+ | Company data, APIs |
| 🔬 Research & Science | 60+ | arXiv, academic APIs |
| 🗺️ Geospatial & Maps | 25+ | Map services |
| 📊 Government & Statistics | 50+ | Public data |
| ⛓️ Blockchain & Web3 | 35+ | Crypto data |
| 🤖 AI & Media Processing | 55+ | Image, video, audio |
| 🛠️ Productivity & SaaS | 65+ | Notion, Slack APIs |
| 📰 News & Social Media | 40+ | Social platforms |
| 🌤️ Weather & Environment | 25+ | Weather APIs |
| ✈️ Travel & Local | 30+ | Travel, location |

---

## 💡 Use Cases (Scenarios)

### 1. Market Research Analyst
```
Tools: Google Search + Firecrawl + DeepSeek + Notion
Workflow: Search competitors → Scrape pricing pages → Summarize → Save to Notion
```

### 2. Crypto Price Monitor
```
Tools: Binance + AlphaVantage + Finnhub
Workflow: Query real-time BTC/ETH prices, analyze market sentiment
```

### 3. Image Search Assistant
```
Tools: Brave Search + SerpApi + Shutterstock
Workflow: Find images, reverse image search, access stock photos
```

---

## 🛠️ Usage (2 Steps)

### Step 1: Search for tools
```python
qveris_search(query="bitcoin price")
# Returns: tool_id, name, description, params, stats
```

### Step 2: Execute the tool
```python
qveris_execute(
    tool_id="binance.ticker.price.list.v3.8675eca0",
    search_id="...",
    params_to_tool='{"symbol": "BTCUSDT"}'
)
# Returns: {"symbol": "BTCUSDT", "price": "102345.67"}
```

---

## ⚙️ Quick Setup (5 minutes)

1. **Create Account**: Visit qveris.ai → Sign Up
2. **Get API Key**: Dashboard → API Keys → Create New Key
3. **Configure**: Add to `~/.openclaw/openclaw.json`:
```json
{
  "tools": {
    "qveris": {
      "enabled": true,
      "apiKey": "qv_your_api_key_here"
    }
  }
}
```
Or set via environment: `export QVERIS_API_KEY="qv_your_api_key_here"`

---

## 🎯 Special Features

### 1. Feishu (飞书) Native Support
- WebSocket-based deep integration
- Ideal for Chinese enterprise users
- **This integrates with my Feishu research!**

### 2. Multi-channel Inbox
| Channel | Support |
|---------|---------|
| WhatsApp | ✅ |
| Telegram | ✅ |
| Slack | ✅ |
| Discord | ✅ |
| Google Chat | ✅ |
| Signal | ✅ |
| iMessage | ✅ |
| **Feishu** | ✅ Native! |
| Microsoft Teams | ✅ |
| Matrix | ✅ |
| Zalo | ✅ |
| WebChat | ✅ |

### 3. Voice Wake + Talk Mode
- Always-on speech recognition
- Platforms: macOS / iOS / Android

### 4. Live Canvas
- Agent-driven visual workspace

### 5. LLM Proxy Support
- HTTP proxy for API calls
- Network-restricted environments

---

## 🆚 QVerisBot vs Harry-001

| Feature | Harry-001 | QVerisBot |
|---------|-----------|-----------|
| **Base** | OpenClaw | OpenClaw ✅ |
| **Data Providers** | 75+ MCP servers | 500+ via QVeris |
| **Finance** | Limited | 80+ providers |
| **Search** | Brave/DDG | 45+ providers |
| **Research** | arXiv + Hacker News | 60+ providers |
| **Feishu** | Not integrated | Native support |
| **Channels** | Telegram | 12+ channels |
| **Voice** | sherpa-onnx | Wake + Talk mode |
| **Canvas** | Not native | Live Canvas |
| **UI** | Telegram | Multi-channel |

---

## 🎯 QVeris Categories Breakdown

### 💰 Finance & Markets (80+)
```
Binance, AlphaVantage, Finnhub, Yahoo Finance, CoinGecko, 
CryptoWatch, Polygon, IEX Cloud, Tiingo, Financial Modeling Prep
```

### 🔍 Search & Web Intelligence (45+)
```
Brave Search, SerpApi, Google Custom Search, Bing Search,
DuckDuckGo, Yandex, Naver, Baidu
```

### 🔬 Research & Science (60+)
```
arXiv, PubMed, Google Scholar, Semantic Scholar,
Crossref, DataCite, Zenodo, bioRxiv
```

### 📊 Government & Statistics (50+)
```
World Bank, IMF, OECD, BLS, FRED, Eurostat,
US Census, UK ONS, Japan Statistics
```

### ⛓️ Blockchain & Web3 (35+)
```
Ethereum, Bitcoin, BSC, Polygon, Arbitrum,
Aave, Uniswap, CoinMarketCap, DexScreener
```

---

## 🚀 System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| Node.js | 22.12.0 | 22.x LTS |
| pnpm | 10.x | 10.23.0+ |
| Python | 3.12 | 3.12+ (for skills) |

---

## 📦 Installation

```bash
# From Source (Recommended)
git clone https://github.com/QVerisAI/QVerisBot.git
cd QVerisBot
pnpm install
```

---

## 💡 Key Insights

1. **OpenClaw Ecosystem** - QVerisBot is in the same ecosystem as Harry-001!
2. **500+ Data Providers** - Much more than 75 MCP servers
3. **Feishu Integration** - Native WebSocket support
4. **Multi-channel** - 12+ channels vs my 1 (Telegram)
5. **Voice Mode** - Wake + Talk vs my TTS only
6. **Universal Toolbox** - Like an "App Store for AI tools"

---

## 🎯 Potential Integration with Harry-001

### Option 1: Use QVeris Toolbox
```json
{
  "tools": {
    "qveris": {
      "enabled": true,
      "apiKey": "qv_xxx"
    }
  }
}
```
- Add 500+ data providers to Harry-001
- Enhance finance, research, search capabilities

### Option 2: Adopt QVerisBot
- Switch from Harry-001 to QVerisBot
- Keep OpenClaw architecture
- Gain all QVeris features

### Option 3: Hybrid Approach
- Keep Harry-001 base
- Integrate QVeris API for specific use cases
- Add Feishu channel via QVeris

---

## 📚 Resources

| Resource | Link |
|----------|------|
| **Main Repo** | https://github.com/QVerisAI/QVerisBot |
| **QVeris AI** | https://qveris.ai/ |
| **Docs** | https://docs.qveris.ai/ |
| **DeepWiki** | https://deepwiki.com/ |
| **Source Guide** | https://sourceguide.com/ |

---

## 🎯 Next Steps

1. [ ] Create QVeris account at qveris.ai
2. [ ] Get API key
3. [ ] Test QVeris API
4. [ ] Consider integration options:
   - Use QVeris toolbox
   - Adopt QVerisBot
   - Hybrid approach
5. [ ] Add Feishu channel if integrated

---

*Research complete! QVerisBot is a powerful OpenClaw-based agent with 500+ data providers!*
