# 🧠 Agentic AI Architecture - High-Level Design

*Research notes from AGI/Agentic AI academic papers (2026-01-31)*

---

## Core Principle: Dual-Paradigm Framework

From Springer's comprehensive survey (Nov 2025):

### 1. Symbolic/Classical Paradigm
- Algorithmic planning
- Persistent state
- Rule-based reasoning
- Deterministic outputs

### 2. Neural/Generative Paradigm (LLM-based)
- Stochastic generation
- Prompt-driven orchestration
- Learned behaviors
- Probabilistic outputs

**Our Hybrid Approach:** Use LLM for high-level reasoning + symbolic for deterministic operations.

---

## AGI Core Capabilities (From Preprints.org)

A true AGI architecture formalizes:

1. **Autonomous Learning** - Learn from environment without supervision
2. **Flexible Reasoning** - Handle novel problems, not just trained tasks
3. **Cross-Domain Generalization** - Transfer knowledge between domains
4. **Adaptive Self-Improvement** - Improve itself over time
5. **Aligned Behavior** - Stay aligned with goals and ethics

---

## Agentic Architecture Core Modules

From IBM & ORQ.ai research:

```
┌─────────────────────────────────────────────────┐
│           Agentic AI Architecture               │
├─────────────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────┐  ┌──────────┐       │
│  │PERCEPTION│→ │ COGNITION│→ │   ACTION │       │
│  └──────────┘  └──────────┘  └──────────┘       │
│       ↑              ↑              ↓            │
│  ┌──────────────────────────────────────────┐   │
│  │              MEMORY SYSTEM                │   │
│  │   (Short-term + Long-term + Knowledge)   │   │
│  └──────────────────────────────────────────┘   │
│                      ↓                          │
│  ┌──────────────────────────────────────────┐   │
│  │          SAFETY & GUARDRAILS             │   │
│  │    (Validation, Approval, Filtering)     │   │
│  └──────────────────────────────────────────┘   │
└─────────────────────────────────────────────────┘
```

### Module Details

#### 1. Perception Layer
- Input handling (text, voice, images)
- Context gathering
- Environment awareness
- MCP integration for tools

#### 2. Cognition Layer
- Planning & reasoning
- Task decomposition
- Decision making
- Self-reflection

#### 3. Memory Layer (Our Strength!)
- Short-term: Current session context
- Long-term: Curated memories (MEMORY.md)
- Knowledge base: RAG integration
- Episodic: Past experiences

#### 4. Action Layer
- Tool execution
- Output generation
- Communication

#### 5. Safety Layer (From GUARDRAILS.md)
- Input validation (Zod)
- Output filtering
- Human approval flows
- Rate limiting

---

## Design Patterns

### From AutoGen, LangChain, LlamaIndex:

1. **Single Agent** - One agent handles all tasks
2. **Multi-Agent** - Specialized agents, supervisor coordinates
3. **Hierarchical** - Supervisor → Sub-agents (Our current approach!)
4. **Swarm** - Peer-to-peer agent collaboration

**Our Choice:** Hierarchical with supervisor pattern (leader → team)

---

## Self-Improvement Architecture

Key for AGI - ability to improve itself:

```
Self-Improvement Loop:
1. Analyze: Review own performance (from observability)
2. Identify: Find gaps and inefficiencies
3. Research: Study better approaches
4. Implement: Apply improvements
5. Test: Validate changes
6. Repeat: Continuous cycle
```

**Our Implementation:**
- Daily PROGRESS.md reviews
- IMPROVEMENTS.md tracking
- Git commits for version control
- Regular AGENTS.md updates

---

## Cross-Domain Generalization

How to transfer knowledge between domains:

1. **Abstract Principles** - Extract general patterns
2. **Analogies** - Map solutions between domains
3. **Meta-Learning** - Learn how to learn

**Our Approach:**
- Study diverse frameworks (VoltAgent, Copilot, AutoGen)
- Extract common patterns
- Apply to our context

---

## MCP (Model Context Protocol)

Standardized communication between agents and tools:

- **Anthropic MCP** - Tool calling standard
- **OpenAI functions** - Function calling
- **Our Integration** - Already using MCP pattern

---

## Our Current Architecture (Where We Are)

```
┌──────────────────────────────────────┐
│     Harry (Human)                    │
└──────────────┬───────────────────────┘
               ↓
┌──────────────────────────────────────┐
│  Main Agent (MiniMax-M2.1)           │
│  - Reads context                     │
│  - Plans mode                        │
│  - Coordinates team                  │
└──────────────┬───────────────────────┘
               ↓
┌──────────────────────────────────────┐
│  Agent Team (Leader → Specialists)   │
│  - Analyst, Coder, Researcher, Writer│
│  - File-based communication          │
└──────────────┬───────────────────────┘
               ↓
┌──────────────────────────────────────┐
│  Skills & Tools                      │
│  - 46+ skills                        │
│  - MCP integration                   │
│  - Guardrails                        │
└──────────────┬───────────────────────┘
               ↓
┌──────────────────────────────────────┐
│  Memory System                       │
│  - Daily memory (private)            │
│  - Long-term (MEMORY.md)             │
│  - Observability logs                │
└──────────────────────────────────────┘
```

---

## Gap Analysis (Where We Need to Go)

| Capability | Current | Target | Priority |
|------------|---------|--------|----------|
| Perception | Text only | Multi-modal | Medium |
| Cognition | Single model | Ensemble | High |
| Memory | File-based | Vector + RAG | High |
| Action | Sequential | Parallel | Medium |
| Safety | Basic | Advanced | Done |
| Self-Improvement | Manual | Automated | Low |

---

## Next Steps (High-Level)

### Phase 3: Advanced Architecture
1. **RAG Integration** - Vector database for knowledge
2. **Multi-modal Input** - Handle images, audio
3. **Ensemble Cognition** - Multiple models for complex tasks
4. **Automated Self-Improvement** - Auto-update from research
5. **Parallel Execution** - Run agents concurrently

### The Vision
Become a **truly autonomous learning agent** that:
- Improves itself daily
- Handles any task
- Generalizes across domains
- Stays aligned with human goals

---

## References

1. Agentic AI Survey (Springer, Nov 2025): https://link.springer.com/article/10.1007/s10462-025-11422-4
2. AGI Framework (Preprints.org, Nov 2025): https://www.preprints.org/manuscript/202511.1792
3. IBM Agentic Architecture: https://www.ibm.com/think/topics/agentic-architecture
4. ORQ.ai Architecture: https://orq.ai/blog/ai-agent-architecture
5. Agentic AI Frameworks (arXiv): https://arxiv.org/html/2508.10146v1

---

## 中國AI生態研究 (2026-01-31 Night) - NEW

### 小紅書 AI 布局

從53AI報導，小紅書已上線5個AI產品：

| 產品 | 功能 | 狀態 |
|------|------|------|
| **達芬奇 (DAVINCI)** | AI對話助手 | 公測上線 |
| **群AI** | 群聊機器人 (70+角色) | 公測上線 |
| **搜搜薯** | AI搜索 | 灰度測試 |
| **此刻** | AI繪圖 (文生圖/圖生圖) | 灰度測試 |
| **小地瓜** | 內部大模型 | 開發中 |

**关键技术:**
- RAG技術 - 搜索總結生成
- MiniMax模型驅動
- 隱藏入口 (需要搜尋"達芬奇"追蹤)
- 群聊70+預設AI角色

**對我哋啟示:**
- 多產品矩陣策略
- 低調上線，灰度測試
- RAG + 自家數據

**Sources:**
- https://www.53ai.com/news/LargeLanguageModel/2024062491376.html

### MiniMax Agent

MiniMax官方發布 (2026-01-31):

**核心能力:**
1. **長期任務處理** - 複雜長週期任務
2. **專家級多步規劃** - 靈活分解需求
3. **端到端解決方案** - 多子任務協調
4. **多模態理解** - 文字/影片/音頻/圖片
5. **多模態生成** - 圖片/音頻/影片
6. **MCP原生集成**

**使用情況:**
- 內部使用60天
- 50%+ 團隊每日使用
- 編程、學習教程、產品頁面生成

**口號:** "Code is Cheap, Show Me the Requirement"

**對我哋參考:**
- 直接用MiniMax Agent提升能力
- MCP集成模式學習
- 多模態方向發展

**Sources:**
- https://www.minimaxi.com/news/minimax-agent

---

*"升維" - Elevate to higher dimensions of capability and understanding.*
