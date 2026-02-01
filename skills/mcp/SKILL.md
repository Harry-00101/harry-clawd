# MCP Integration

Model Context Protocol - Standard for AI tool integration.

## What is MCP?

From Anthropic - the protocol that connects AI assistants to external tools.

75+ MCP servers available for:
- File conversion (PDF, Word, Excel, images, audio)
- GitHub integration
- Browser automation
- Database connections
- Cloud services (Azure, Supabase, MongoDB, etc.)
- Documentation lookup
- Web search (Tavily, Firecrawl)
- Code tools (Chrome DevTools, Next.js, Vite)
- And more!

## Architecture

```
AI Assistant (Claude, Harry-001, etc.)
        ↓
   MCP Protocol
        ↓
   MCP Servers (75+)
        ↓
   External Tools & Data
```

## MCP Servers We Can Use

| Server | Purpose | For Harry-001 |
|--------|---------|---------------|
| firecrawl | Web scraping | ✅ Already have |
| github | Repo management | Research |
| postgres | Database | Data storage |
| notion | Notes integration | Memory |
| tavily | Web search | Research |
| sse | Terminal | Automation |
| chrome | Browser automation | Testing |
| todoist | Task management | Productivity |
| filesystem | File operations | Automation |
| chromadb | Vector storage | Knowledge base |

## Installation

```bash
# MCP servers are typically installed via npm/pip
npm install -g @modelcontextprotocol/server-github
pip install mcp-server-firecrawl

# Or use via Claude Desktop config
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"]
    }
  }
}
```

## For Harry-001

Integrate MCP servers to extend capabilities:
1. **Firecrawl** - Web scraping (already integrated)
2. **GitHub** - Repo management, issues
3. **PostgreSQL** - Data storage
4. **Notion** - Notes sync
5. **Tavily** - Better web search
6. **ChromaDB** - Vector knowledge base
7. **Todoist** - Task management

## MCP Registry

Full list: https://github.com/mcp

Popular servers:
- @modelcontextprotocol/server-github
- @modelcontextprotocol/server-filesystem
- @modelcontextprotocol/server-postgres
- @modelcontextprotocol/server-notion
- firecrawl-mcp

## References

- https://github.com/mcp (MCP Registry)
- https://modelcontextprotocol.io (Official docs)
- MCP Protocol specification
