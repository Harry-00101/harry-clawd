# TOOLS.md - Local Notes

Skills define *how* tools work. This file is for *your* specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:
- Camera names and locations
- SSH hosts and aliases  
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras
- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH
- home-server → 192.168.1.100, user: admin

### TTS
- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

## Installed Skills (15 total)

### Search & Productivity
- **ddg-search** - DuckDuckGo CLI
- **web-search-exa** - Web search (Exa)
- **ai-alias** - Shell alias generator
- **todoist** - Todoist integration
- **fzf-fuzzy-finder** - Fuzzy finder

### CLI Tools
- **tldr** - Quick man pages
- **portable-tools** - CLI utilities
- **sysadmin-toolbox** - System admin
- **ssh-essentials** - SSH management

### Productivity Suite
- **notnative** - Notion + Native hybrid
- **mcporter** - MCP server manager
- **oracle** 🧿 - AI prompt bundler

### Communication
- **morning-email-rollup** 📧 - Email digest

### Core
- **weather** 🌤️ - Hong Kong weather
- **calendar** - Calendar management

### Built-in Skills Available
- github, slack, notion, bird (X), tmux, bluebubbles, skill-creator, clawdhub

## 📊 Skills Installed (46 total!)

### 🎯 Debug & Code Analysis
- **debug-pro** - Debug problems
- **ai-explain** - Explain code
- **code-reviewer** - Code review
- **coding-agent** - Coding assistant
- **git-essentials** - Git operations

### 🧪 Testing & Quality
- **test-runner** - Test runner
- **ai-coverage-boost** - Test coverage booster
- **test-gen** - Unit test generator

### 🗄️ Database & SQL
- **database** - Database operations
- **ai-sql** - SQL query generator
- **postgres** - PostgreSQL specific

### 🔄 Automation & Workflow
- **n8n-automation** - Workflow automation
- **agent-orchestrator** - Multi-agent coordination

### 🔍 Research & AI
- **research** - General research
- **deep-research** - Deep research agent

### 🎤 Voice & Audio
- **local-whisper** 🎙️ - Offline speech-to-text (Whisper)
- **sherpa-onnx-tts** - Local TTS (already configured)

### 🌐 Browser
- **agent-browser-clawdbot** - Local browser automation
- **browser-use** - Cloud browser automation (paid)

### 💬 Communication
- **telegram-bot** - Telegram bot capabilities

### 📄 Document Processing
- **markdown-converter** - Markdown conversion
- **nano-pdf** - PDF operations
- **chart-image** - Chart/image generation

### 🔐 Security
- **security-monitor** - Security monitoring

### 🐳 Docker & Kubernetes
- **docker-essentials** - Docker operations
- **docker-diag** - Docker diagnostics
- **kubectl** - Kubernetes CLI
- **kubernetes** - Kubernetes management

### 🖥️ Terminal & Shell
- **zellij** - Terminal workspace
- **imagemagick** - Image processing

### 🛠️ Core Tools
- weather, calendar, ddg-search, web-search-exa, tldr, fzf, portable-tools, sysadmin-toolbox, ssh-essentials, ai-alias, todoist, morning-email-rollup, notnative, mcporter, oracle

## Helper Files
- `.bash_aliases` - Quick command aliases
- `setup-helpers.sh` - Command reference

## Automation (Cron Jobs)
- ☀️ 8:00 AM - Morning Weather
- 📅 9:00 AM - Calendar Check
- 🌙 8:00 PM - Evening Summary

## CLI Tools
- `rg`, `fdfind`/`fd`, `fzf`, `tldr`, `jq`, `bat`

## Quick Commands
```bash
hkweather           # Hong Kong weather
ddg "query"         # DuckDuckGo search
websearch "query"   # Web search
ff "pattern"        # Find files
tldr command        # Quick help
tasks               # Show todo list
note                # Quick note capture
tts "text"          # Generate voice message (FREE!)
```

## Hong Kong Specific
- Timezone: HKT (UTC+8)
- Weather: "Hong Kong"

## 🎤 Voice (Local Free TTS)
- **Status:** ✅ Working
- **Engine:** sherpa-onnx (offline, no API key)
- **Voice:** en_US lessac (Piper)
- **Usage:** `tts "Hello world"` → generates WAV file

## 🤖 Mini-Agent Framework
- **Status:** ✅ Installed
- **Location:** `/root/clawd/Mini-Agent/`
- **Config:** `~/.mini-agent/config/config.yaml`
- **Runner:** `/root/clawd/Mini-Agent/run-agent.sh`
- **Requires:** MiniMax API Key

### Mini-Agent Features
- Full agent execution loop (Perception → Thinking → Action → Feedback)
- Persistent memory (Session Note Tool)
- Intelligent context management (auto-summarization)
- Claude Skills integration (uses our /root/clawd/skills!)
- MCP tool support
- File tools, bash tools

### Usage
```bash
# Set API key first
export MINIMAX_API_KEY="your-key"

# Run agent
cd /root/clawd/Mini-Agent
./run-agent.sh "Research and solve: [your problem]"

# Or directly
.venv/bin/python -m mini_agent.cli "Help me debug this issue"
```

## 🌐 Browser Automation
- **Status:** ✅ Working (agent-browser v0.8.5)
- **Engine:** Local Chromium (playwright-based)
- **Usage:** `agent-browser open <url>` then `snapshot`, `click`, `fill`, etc.
- **Commands:**
  ```bash
  agent-browser open https://example.com
  agent-browser snapshot -i --json
  agent-browser click @e2
  agent-browser fill @e3 "text"
  agent-browser get text @e1 --json
  ```

## 📊 Browser Use (Cloud - Paid)
- **Status:** ⚠️ Not configured
- **URL:** https://cloud.browser-use.com
- **Pricing:** $0.06/hour (pay as you go)
- Requires API key to enable
