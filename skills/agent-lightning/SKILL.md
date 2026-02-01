# Agent Lightning Integration

Microsoft's AI Agent Trainer with Reinforcement Learning.

## What is Agent Lightning?

- **Train any AI agent** with RL, SFT, APO
- **Zero code change** optimization (almost)
- **Works with**: LangChain, OpenAI Agent SDK, AutoGen, CrewAI, Microsoft Agent Framework
- **LightningStore**: Central hub for tasks, resources, traces

## Installation

```bash
pip install agentlightning
```

Or latest nightly:
```bash
pip install --pre agentlightning
```

## For Harry-001

Agent Lightning可以提升Harry-001既能力：
1. RL training for better decision making
2. Automatic prompt optimization
3. Multi-agent coordination
4. Trace collection for debugging

## Architecture

```
Your Agent → Add emit_xxx() helpers → LightningStore
                                           ↓
                                    Algorithm (RL/APO/SFT)
                                           ↓
                                    Optimized Agent
```

## References
- https://github.com/microsoft/agent-lightning
- https://microsoft.github.io/agent-lightning/
- arXiv: 2508.03680
