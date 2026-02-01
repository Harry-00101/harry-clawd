# Beads Integration

Steve Yegge's AI Agent Memory System.

## What is Beads?

A distributed, git-backed graph issue tracker for AI agents.

From the legendary programmer Steve Yegge (ex-Google, ex-Amazon).

## Key Features

| Feature | Description |
|---------|-------------|
| **Git-backed** | Issues stored as JSONL in .beads/ |
| **Graph-based** | Dependency-aware task tracking |
| **Agent-optimized** | JSON output, auto-ready detection |
| **Zero conflict** | Hash-based IDs (bd-a1b2) |
| **Memory decay** | Auto-summarize old tasks |
| **Long-horizon** | Never lose context |

## Installation

```bash
# Via curl
curl -fsSL https://raw.githubusercontent.com/steveyegge/beads/main/scripts/install.sh | bash

# Via npm
npm install -g @beads/bd

# Via Go
go install github.com/steveyegge/beads/cmd/bd@latest
```

## Essential Commands

```bash
bd ready          # List tasks with no blockers
bd create "Task" -p 0  # Create P0 task
bd dep add <child> <parent>  # Link tasks
bd show <id>      # View task details
bd init --stealth  # Local mode (no git commit)
```

## For Harry-001

Perfect for:
1. **Task Tracking** - Track automation tasks
2. **Dependency Management** - Link related tasks
3. **Long-term Memory** - Persistent across sessions
4. **Project Planning** - Graph-based workflow
5. **Multi-agent Coordination** - Zero conflict IDs

## Integration with Harry-001

```bash
# Install
bd init

# Add to AGENTS.md
echo "Use 'bd' for task tracking" >> AGENTS.md

# Track automation
bd create "Daily VOO Analysis" -p 0
bd create "Market Research" -p 1
bd dep add <market-task> <voo-task>
```

## Steve Yegge

Legendary programmer:
- Ex-Google, ex-Amazon
- Famous blogs: "Rich Programmer Data", "Execution in the Kingdom of Nouns"
- Now building AI agent tools

## References

- https://github.com/steveyegge/beads
- https://github.com/steveyegge/beads/blob/main/AGENT_INSTRUCTIONS.md
- Steve Yegge's blog: https://steve-yegge.blogspot.com
