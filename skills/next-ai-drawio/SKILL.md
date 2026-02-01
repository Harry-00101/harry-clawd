# Next AI Draw.io Skill

AI-Powered Diagram Creation - Generate draw.io diagrams via natural language!

## 🎯 What It Does

```
Natural Language → AI → draw.io Diagram
```

## 🌐 Web Demo

**Try online (no install needed):**
https://next-ai-drawio.jiang.jp/

**Or use your own API key** (stored locally in browser)

## 💻 Installation

### Option 1: Quick Start (Demo)
```bash
# Just visit the web demo
open https://next-ai-drawio.jiang.jp/
```

### Option 2: Desktop App
```bash
# Download from releases
# https://github.com/DayuanJiang/next-ai-draw-io/releases

# Supports: Windows, macOS, Linux
```

### Option 3: Self-Hosted (Node.js)
```bash
git clone https://github.com/DayuanJiang/next-ai-draw-io
cd next-ai-draw-io
npm install
cp env.example .env.local
# Edit .env.local with your API keys

npm run dev
# Open http://localhost:6002
```

### Option 4: Docker
```bash
# See docs for Docker setup
```

## 🔧 MCP Server Integration

Use with Claude Desktop, Cursor, VS Code!

### Claude Desktop
Add to `~/.config/claude/claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "drawio": {
      "command": "npx",
      "args": ["@next-ai-drawio/mcp-server@latest"]
    }
  }
}
```

### Claude Code CLI
```bash
claude mcp add drawio -- npx @next-ai-drawio/mcp-server@latest
```

Then ask:
"Create a flowchart showing user authentication flow"

## 🎨 Example Prompts

### Cloud Architecture
```
Generate a AWS architecture diagram with AWS icons.
Users connect to a frontend hosted on EC2...
```

### Animated Diagram
```
Give me an animated connector diagram of transformer's architecture.
```

### Simple Drawing
```
Draw a cute cat for me.
```

## 🤖 AI Providers Supported

| Provider | Notes |
|----------|-------|
| OpenAI | GPT-4, o1, o3 |
| Anthropic | Claude |
| Google | Gemini, Vertex |
| AWS Bedrock | Default |
| Azure OpenAI | Enterprise |
| DeepSeek | Chinese |
| Doubao | ByteDance |
| Ollama | Local models |
| + More... |

## 📚 Use Cases for Harry-001

1. **Visualize Brain Architecture**
   - "Create a diagram of brain regions: Frontal, Parietal, Temporal..."
   
2. **System Architecture**
   - "Show Harry-001's system architecture with all skills"

3. **Workflow Diagrams**
   - "Create a flowchart of daily automation schedule"

4. **Educational Content**
   - "Generate a diagram explaining neural pathways"

## 🔗 Links

- **Repo:** https://github.com/DayuanJiang/next-ai-draw-io
- **Demo:** https://next-ai-drawio.jiang.jp/
- **MCP Server:** https://github.com/DayuanJiang/next-ai-draw-io/tree/main/packages/mcp-server

## 📝 Quick Commands

```bash
# Clone
git clone https://github.com/DayuanJiang/next-ai-draw-io
cd next-ai-draw-io

# Install
npm install

# Configure API keys
cp env.example .env.local
# Edit .env.local

# Run
npm run dev
# http://localhost:6002
```

## 🎯 Harry-001 Integration

Integrate with MCP Server for Claude Desktop:
- Draw diagrams via conversation
- Visualize brain architecture
- Create system diagrams

Perfect for explaining Harry-001's architecture visually! 🧠📊
