# Mini-Agent Framework Integration

## What is Mini-Agent?

Mini-Agent is MiniMax's open-source AI Agent framework. It's a **minimalist yet professional** agent development framework that demonstrates best practices for building intelligent agents.

**Key Philosophy:** Lightweight, Simple, Extensible

## Core Architecture

### Agent Loop: Perception → Thinking → Action → Feedback

```
1. Perception:   Receive user input / Check message history
2. Thinking:     Call LLM (MiniMax-M2.1) for decisions
3. Action:       Execute tool calls (if needed)
4. Feedback:     Add results to message history
5. Repeat:       Until task complete (up to max_steps)
```

### Three Core Components

#### 1. LLM (Brain)
- Model: MiniMax-M2.1
- Handles understanding and decision-making
- Supports tool calling

#### 2. Tools (Hands & Feet)
- **File Tools:** Read, write, edit files
- **Bash Tool:** Execute shell commands
- **Note Tool:** Persistent session memory
- **Skills:** Claude Skills integration (we have 33 skills!)
- **MCP Tools:** Extended capabilities

#### 3. Memory
- Conversation history management
- Auto-summarization for long contexts
- Session persistence

## Integration with Our System

### Skills Directory
```
Mini-Agent → Uses → /root/clawd/skills/ (33 skills!)
```

### Configuration
- **Config:** `~/.mini-agent/config/config.yaml`
- **System Prompt:** `~/.mini-agent/config/system_prompt.md`
- **MCP Config:** `~/.mini-agent/config/mcp.json`

### Available Tools
- All our skills are available to Mini-Agent
- Browser automation (agent-browser)
- Voice I/O (local-whisper, sherpa-onnx-tts)
- Search (ddg-search, web-search-exa)
- Database (database, ai-sql, postgres)
- Git (git-essentials)
- Debug (debug-pro)
- Code analysis (ai-explain, code-reviewer)
- Research (research, deep-research)

## Usage Examples

### Basic Task
```bash
cd /root/clawd/Mini-Agent
./run-agent.sh "Research the best practices for Python async programming"
```

### Debug Problem
```bash
./run-agent.sh "Debug why my Docker container is not starting. Check logs in /var/log/"
```

### Database Query
```bash
./run-agent.sh "Create a SQL query to find all users who logged in the last 7 days"
```

### Code Review
```bash
./run-agent.sh "Review the code in /root/clawd/project/ and suggest improvements"
```

### Research & Solve
```bash
./run-agent.sh "Research: How to optimize PostgreSQL queries? Then apply suggestions to my queries."
```

## Files Created

```
/root/clawd/Mini-Agent/
├── README.md                    # Original documentation
├── run-agent.sh                 # Easy runner script
├── .venv/                       # Python virtual environment
├── workspace/                   # Agent working directory
└── mini_agent/                  # Source code

~/.mini-agent/config/
├── config.yaml                  # Main configuration
├── system_prompt.md             # Custom system prompt
└── mcp.json                     # MCP server config
```

## Setup Required

1. **Set MiniMax API Key:**
   ```bash
   export MINIMAX_API_KEY="your-api-key"
   ```

   Or create file:
   ```bash
   echo "your-api-key" > ~/.clawdbot/.minimax_api_key
   ```

2. **Run Agent:**
   ```bash
   cd /root/clawd/Mini-Agent
   ./run-agent.sh "Your task here"
   ```

## Benefits for Harry

✅ **Research:** Deep research on any topic
✅ **Debug:** Analyze and solve problems
✅ **Code:** Generate, review, and fix code
✅ **Automate:** Create workflows
✅ **Voice:** Voice-in, voice-out conversation
✅ **Browser:** Automated web tasks
✅ **Database:** Query and manage data

## Skills Available to Agent (33 total!)

**Debug & Code:** debug-pro, ai-explain, code-reviewer, coding-agent, git-essentials
**Database:** database, ai-sql, postgres
**Automation:** n8n-automation, agent-orchestrator
**Research:** research, deep-research
**Voice:** local-whisper, sherpa-onnx-tts
**Browser:** agent-browser, browser-use
**Communication:** telegram-bot
**Core:** weather, calendar, ddg-search, web-search-exa, tldr, fzf, portable-tools, sysadmin-toolbox, ssh-essentials, ai-alias, todoist, morning-email-rollup, notnative, mcporter, oracle

---

*Mini-Agent: The essence of an Agent is a decision loop.*
