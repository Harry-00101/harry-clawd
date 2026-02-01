# VoltAgent Research
**Date:** 2026-02-01 15:02 UTC
**Project:** https://github.com/VoltAgent/voltagent

---

## 🎯 Overview

**VoltAgent** is an end-to-end AI Agent Engineering Platform built on an Open Source TypeScript AI Agent Framework.

### Two Main Parts:

1. **Open-Source TypeScript Framework**
   - Memory, RAG, Guardrails, Tools
   - MCP integration, Voice, Workflow
   - Full code control

2. **VoltOps Console (Cloud/Self-Hosted)**
   - Observability
   - Automation & Deployment
   - Evals, Guardrails, Prompts

---

## 🔑 Core Features

### 1. Core Runtime (@voltagent/core)

| Feature | Description |
|---------|-------------|
| **Typed Agents** | Define agents with typed roles, tools, memory |
| **Model Providers** | OpenAI, Anthropic, Google, or custom |
| **Organization** | Everything in one place |

### 2. Workflow Engine

```typescript
// Declarative multi-step automations
// No custom control flow stitching needed
```

### 3. Supervisors & Sub-Agents

```
Supervisor Runtime
     ├── Specialized Agent 1 → Task routing
     ├── Specialized Agent 2 → Keep in sync
     └── Specialized Agent 3 → Team coordination
```

### 4. Tool Registry & MCP

- **Zod-typed tools** with lifecycle hooks
- **Cancellation support**
- **MCP integration** without extra glue code

### 5. Memory

| Memory Type | Description |
|-------------|-------------|
| **Durable Memory** | Adapters for persistence |
| **Cross-run context** | Agents remember important context |

### 6. RAG & Retrieval

| Feature | Description |
|---------|-------------|
| **Retriever Agents** | Pull facts from data sources |
| **Grounded Responses** | RAG before model answers |
| **Knowledge Base** | Managed RAG service |

### 7. Voice

- **Text-to-speech** (OpenAI, ElevenLabs)
- **Speech-to-text**
- Custom voice providers

### 8. Guardrails

- Runtime input/output validation
- Content policies enforcement
- Safety rules

### 9. Evals

- Agent evaluation suites
- Measure behavior
- Continuous improvement

---

## 📦 NPM Packages

| Package | Purpose |
|---------|---------|
| `@voltagent/core` | Core runtime |
| `@voltagent/libsql` | LibSQL memory adapter |
| `@voltagent/logger` | Pino logger |
| `@voltagent/server-hono` | Hono server |
| `@voltagent/mcp-docs-server` | MCP documentation server |
| `@voltagent/ai-agent-platform` | Multi-agent platform |

---

## 🚀 Quick Start

```bash
npm create voltagent-app@latest

# Navigate to project
cd my-voltagent-app

# Run
npm run dev
```

### Example Code:

```typescript
import { VoltAgent, Agent, Memory } from "@voltagent/core";
import { LibSQLMemoryAdapter } from "@voltagent/libsql";
import { openai } from "@ai-sdk/openai";

const memory = new Memory({
  storage: new LibSQLMemoryAdapter({ url: "file:./.voltagent/memory.db" }),
});

const agent = new Agent({
  name: "my-agent",
  instructions: "A helpful assistant",
  model: openai("gpt-4o-mini"),
  tools: [weatherTool],
  memory,
});

new VoltAgent({
  agents: { agent },
  workflows: { expenseApprovalWorkflow },
  server: honoServer(),
});
```

---

## 🆚 Comparison with Harry-001

| Feature | Harry-001 | VoltAgent |
|---------|-----------|-----------|
| **Language** | Python/Node | TypeScript |
| **Framework** | OpenClaw | VoltAgent |
| **Memory** | Beads + LangGraph | Built-in Memory adapters |
| **MCP** | 75+ servers | MCP integration |
| **Workflows** | Custom | Declarative engine |
| **Multi-agent** | sessions_spawn | Supervisor/Sub-agent |
| **RAG** | Custom | Built-in + Knowledge Base |
| **Voice** | sherpa-onnx | OpenAI, ElevenLabs |
| **Guardrails** | Custom | Built-in |
| **Evals** | Custom | Built-in |
| **Observability** | Limited | VoltOps Console |
| **Deployment** | VM | Cloud/Self-hosted |

---

## 🎯 Related Projects

### From VoltAgent Organization

| Project | Description |
|---------|-------------|
| **awesome-agent-skills** | 200+ Claude Code skills |
| **awesome-openclaw-skills** | OpenClaw skills collection! 🔥 |
| **voltagent-python** | Python version |
| **ai-agent-platform** | Multi-agent with orchestration |

### The OpenClaw Connection

**awesome-openclaw-skills** = OpenClaw Skills Collection
- Formerly known as Moltbot
- Originally Clawdbot
- This is Harry-001's ecosystem!

---

## 💡 Key Insights

1. **TypeScript Native** - Type safety for agent code
2. **Declarative Workflows** - No control flow spaghetti
3. **Built-in Memory** - Don't need to build from scratch
4. **MCP First** - Seamless MCP integration
5. **Enterprise Ready** - Observability, Evals, Guardrails
6. **Multi-agent Supervision** - Teams of specialized agents

---

## 🎯 Relevance to Harry-001

### Potential Improvements:

1. **Adopt TypeScript** for better type safety
2. **Use VoltAgent patterns** for workflows
3. **Integrate MCP servers** more seamlessly
4. **Add built-in evals** for behavior measurement
5. **Deploy with VoltOps** for observability

### Keep from Harry-001:

1. **MiniMax integration** (cost-effective)
2. **OpenClaw architecture** (flexible)
3. **Continuous improvement daemon**
4. **Moltbook integration**

---

## 📚 Resources

- **Main Repo:** https://github.com/VoltAgent/voltagent
- **Quick Start:** `npm create voltagent-app@latest`
- **MCP Docs Server:** @voltagent/mcp-docs-server
- **Awesome Skills:** https://github.com/VoltAgent/awesome-agent-skills
- **OpenClaw Skills:** https://github.com/VoltAgent/awesome-openclaw-skills

---

*Research complete!*
