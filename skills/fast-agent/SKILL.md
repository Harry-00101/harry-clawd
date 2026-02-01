# Fast-Agent Integration

MCP-enabled Agent Framework - Define, Prompt and Test Agents.

## What is Fast-Agent?

Framework for creating sophisticated MCP agents and workflows:
- **Complete MCP support** - Sampling, Elicitations, Streamable HTTP
- **CLI-first** - Terminal-based interaction
- **Declarative syntax** - Simple prompt/MCP composition
- **Multi-model** - Anthropic, OpenAI, Google, Azure, Ollama, Deepseek
- **Agent Skills** - Uses SKILL.md files (like Harry-001!)

## Key Features

| Feature | Description |
|---------|-------------|
| **MCP Sampling** | Server-initiated sampling |
| **Elicitations** | Human input requests |
| **Streamable HTTP** | Reliable transport inspection |
| **Structured Outputs** | JSON/Pydantic support |
| **Vision/PDF** | Multi-modal support |
| **Passthrough/Playback** | Development & testing |

## Architecture

```
fast-agent CLI
    ↓
Prompt Config (YAML)
    ↓
MCP Servers (75+)
    ↓
LLM (Anthropic/OpenAI/Ollama/etc.)
    ↓
Agent Output
```

## For Harry-001

Perfect alignment:
1. **SKILL.md system** - Same as Harry-001!
2. **MCP integration** - Our MCP skills use similar pattern
3. **Declarative config** - Could use for Harry-001 tasks
4. **Multi-model support** - Similar to our delegation

## Installation

```bash
# Via pip
pip install fast-agent-mcp

# Or from source
git clone --recurse-submodules https://github.com/evalstate/fast-agent.git
cd fast-agent
pip install -e .
```

## Usage

```bash
# Create agent config
fast-agent new my-agent

# Edit prompts.yaml
fast-agent edit my-agent

# Run agent
fast-agent run my-agent

# Interactive mode
fast-agent chat my-agent
```

## Example Agent Config

```yaml
# prompts.yaml
agent:
  name: "Stock Analyst"
  model: "claude-sonnet-4-20250514"
  system: "You are a stock market analyst..."
  
mcp_servers:
  - name: "yfinance"
    command: "uvx"
    args: ["mcp-server-yfinance"]
  
  - name: "firecrawl"
    command: "npx"
    args: ["-y", "firecrawl-mcp"]

skills:
  - path: ./skills/voo-analysis/SKILL.md
  - path: ./skills/pandas-ta/SKILL.md
```

## References

- https://github.com/evalstate/fast-agent
- https://pypi.org/project/fast-agent-mcp/
- MCP Protocol: https://modelcontextprotocol.io
- Building Effective Agents: https://www.anthropic.com/research/building-effective-agents
