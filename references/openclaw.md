# OpenClaw - Harry-001's Parent Project

**Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞**

**URL:** https://github.com/openclaw/openclaw
**Website:** https://openclaw.ai
**Docs:** https://docs.openclaw.ai

## 🎯 What is OpenClaw?

OpenClaw is a personal AI assistant you run on your own devices:
- Answers on channels you already use (WhatsApp, Telegram, Slack, Discord, etc.)
- Speaks and listens on macOS/iOS/Android
- Renders a live Canvas you control
- Feels local, fast, and always-on

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     OPENCLAW                            │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │
│  │   Gateway   │  │ Workspace   │  │  Channels   │    │
│  │  (Control)  │  │   (Brain)   │  │ (Telegram,  │    │
│  │             │  │             │  │  WhatsApp)  │    │
│  └─────────────┘  └─────────────┘  └─────────────┘    │
│         │               │               │             │
│         └───────────────┼───────────────┘             │
│                         ▼                             │
│              ┌─────────────────────┐                  │
│              │  Skills (Optional)  │                  │
│              └─────────────────────┘                  │
└─────────────────────────────────────────────────────────┘
```

## 📦 Key Features

| Feature | Description |
|---------|-------------|
| **Multi-Platform** | macOS, Linux, Windows, iOS, Android |
| **Multi-Channel** | WhatsApp, Telegram, Slack, Discord, Signal, iMessage |
| **Multi-Model** | Claude, GPT, local models (Ollama, LM Studio) |
| **Canvas** | Live UI rendering |
| **Skills** | Plugin system for extensions |
| **Local First** | Runs on your own device |

## 🛠️ Installation

```bash
# Runtime: Node ≥22
npm install -g openclaw@latest
# or: pnpm add -g openclaw@latest

# Onboarding wizard
openclaw onboard --install-daemon

# Start gateway
openclaw gateway --port 18789 --verbose
```

## 🎯 Recommended Models

| Model | Use Case |
|-------|----------|
| **Anthropic Pro/Max (100/200)** | Recommended for long-context + prompt-injection resistance |
| **OpenAI (ChatGPT/Codex)** | Alternative, any model supported |

## 🔗 Related Projects

- **nix-clawdbot** - Nix package
- **deepwiki** - Project wiki
- **BlueBubbles** - iMessage integration
- **Matrix** - Matrix protocol support

## 📚 Documentation

- [Getting Started](https://docs.openclaw.ai/start/getting-started)
- [Onboarding](https://docs.openclaw.ai/start/onboarding)
- [Models Config](https://docs.openclaw.ai/concepts/models)
- [Model Failover](https://docs.openclaw.ai/concepts/model-failover)
- [Installation](https://docs.openclaw.ai/install/docker)
- [Showcase](https://docs.openclaw.ai/start/showcase)
- [FAQ](https://docs.openclaw.ai/start/faq)

## 🎓 For Harry-001

OpenClaw is Harry-001's foundation:
- **Core architecture** - Gateway + Workspace pattern
- **Channel system** - Multi-platform messaging
- **Skill system** - Extensible plugin architecture
- **Model support** - Claude, GPT, local LLMs
- **Documentation pattern** - SKILL.md structure

**Harry-001 = OpenClaw + Custom Brain + Hong Kong Focus! 🦞🤖**

## 🌐 Community

- **Discord:** https://discord.gg/clawd
- **GitHub:** https://github.com/openclaw/openclaw
- **Website:** https://openclaw.ai

---

**OpenClaw: The lobster way of personal AI assistants! 🦞**
