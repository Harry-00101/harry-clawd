# steveyegge/beads

**URL:** https://github.com/steveyegge/beads

> A memory upgrade for your coding agent - Distributed, git-backed graph issue tracker.

**Added:** 2026-02-01 02:15

## What is Beads?

Steve Yegge's AI Agent Memory System:
- **Distributed, git-backed** issue tracker
- **Graph-based** task management
- **Long-horizon memory** for agents
- Never lose context

## Key Features

| Feature | Description |
|---------|-------------|
| Git-backed | JSONL in .beads/, versioned like code |
| Graph-based | Dependency-aware, hierarchical |
| Zero conflict | Hash-based IDs (bd-a1b2) |
| Memory decay | Auto-summarize old tasks |
| Stealth mode | Local only, no git commit |

## Commands

```bash
bd ready              # Tasks ready to work on
bd create "Task" -p 0  # Create P0 task
bd dep add <child> <parent>  # Link tasks
bd show <id>          # View details
bd init --stealth     # Local mode
```

## For Harry-001

Use cases:
1. **Task Tracking** - Track automation tasks
2. **Memory System** - Persistent across sessions
3. **Project Planning** - Graph workflow
4. **Multi-agent** - Zero conflict coordination

## Steve Yegge

Legendary programmer:
- Ex-Google, ex-Amazon engineer
- Famous blogs: "Rich Programmer Data", "Execution in the Kingdom of Nouns"
- Now building AI agent infrastructure

## Learn→Try→Production

- [x] Learn - Researched features
- [ ] Try - Installation pending
- [ ] Production - Integrate as Harry-001 memory

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/steveyegge/beads/main/scripts/install.sh | bash
npm install -g @beads/bd
go install github.com/steveyegge/beads/cmd/bd@latest
```

## References

- https://github.com/steveyegge/beads
- https://steve-yegge.blogspot.com (famous blog!)
