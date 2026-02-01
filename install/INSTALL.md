# Harry-001 Installation Guide

**Your Personal AI Assistant with Brain Architecture + Nervous System**

---

## Quick Install (3 Steps)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Harry-00101/harry-001-automation.git
cd harry-001-automation
```

### Step 2: Install Dependencies

```bash
npm install
```

### Step 3: Run Harry-001

```bash
python3 /root/clawd/automation/harry-001-automator.sh status
```

---

## Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **Node.js** | >=22 | 22.x LTS |
| **Python** | 3.10+ | 3.12 |
| **Git** | Latest | Latest |
| **Memory** | 2GB | 4GB+ |
| **Storage** | 1GB | 5GB+ |

---

## Full Installation

### 1. System Dependencies

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install -y nodejs npm python3 python3-pip git

# Verify versions
node --version  # Should be >=22
python3 --version  # Should be >=3.10
```

### 2. Harry-001 Setup

```bash
# Clone the repo
git clone https://github.com/Harry-00101/harry-001-automation.git
cd harry-001-automation

# Make automation scripts executable
chmod +x automation/*.sh

# Test the system
python3 /root/clawd/automation/harry-001-automator.sh status
```

### 3. Configure API Keys (Optional)

```bash
# Create .env file
cat > .env << 'EOF'
# MiniMax API (Primary Brain)
MINIMAX_API_KEY=your-minimax-key
EOF
```

---

## Harry-001 Features

### Core Features

- **Brain Architecture**: 6 brain regions (Frontal, Parietal, Temporal, Occipital, Cerebellum, Brainstem)
- **Nervous System**: Complete CNS + PNS with neural pathways
- **Stock Analysis**: yfinance + pandas-ta
- **Web Research**: Firecrawl + Web-Check
- **Financial Research**: Dexter integration
- **OCR**: PaddleOCR
- **Voice**: Voicebox (local TTS)
- **Video**: Remotion
- **MCP Integration**: 75+ tools
- **Continuous Learning**: 24/7 auto-learning

### Automation Schedule

| Time | Task |
|------|------|
| 07:00 | Morning Weather + Calendar |
| 09:00 | Stock Analysis |
| 12:00 | Market Research |
| 18:30 | End of Work Summary |
| 23:45 | Day Commit + Quiet Mode |
| */5 min | Continuous Learning |

---

## Usage

```bash
# Check status
python3 automation/harry-001-automator.sh status

# Run stock analysis
python3 automation/harry-001-automator.sh stock

# Run market research
python3 automation/harry-001-automator.sh market

# Commit changes
python3 automation/harry-001-automator.sh commit

# Start continuous learning
python3 skills/continuous-learning/monitor.py &
```

---

## Cost

| Component | Cost |
|-----------|------|
| **Hosting** | $5-10/month (VPS) |
| **APIs** | MiniMax ~$0.01/1M tokens |
| **Tools** | Mostly free |
| **Total** | **~$5-15/month** |

---

## Next Steps

1. Clone the repository
2. Install dependencies
3. Configure API keys (optional)
4. Test basic commands
5. Set up cron jobs
6. Deploy to production
7. Use daily!

---

## Support

- **GitHub Issues:** https://github.com/Harry-00101/harry-001-automation/issues

---

**Welcome to Harry-001! Your Personal AI Assistant!**

**要咩諗咩就得咩！**
