# mcp/Model Context Protocol

**URL:** https://github.com/mcp

> Model Context Protocol - Standard for AI tool integration from Anthropic

**Added:** 2026-02-01 02:16

## What is MCP?

Model Context Protocol by Anthropic - the standard for connecting AI assistants to external tools.

**75+ MCP servers** available!

## MCP Registry - Available Servers

| Category | Servers |
|----------|---------|
| **File Conversion** | PDF, Word, Excel, images, audio → Markdown |
| **Code & Dev** | GitHub, Chrome DevTools, Next.js, Vite, Unity |
| **Database** | PostgreSQL, MySQL, SQLite, MongoDB, Elasticsearch |
| **Cloud** | Azure, Supabase, Neon, Sentry |
| **Web** | Firecrawl, Tavily, Apify |
| **Productivity** | Notion, Todoist, Monday.com |
| **DevOps** | Azure DevOps, Terraform, SonarQube |
| **Knowledge** | ChromaDB (vector), Microsoft Docs |

## Architecture

```
AI Assistant (Claude, Harry-001)
        ↓
   Model Context Protocol (MCP)
        ↓
   MCP Servers (75+)
        ↓
   External Tools & Data
```

## For Harry-001

MCP servers to integrate:

| Server | Use Case |
|--------|----------|
| **firecrawl-mcp** | Web scraping (already have!) |
| **github-mcp** | Repo management |
| **postgres-mcp** | Data storage |
| **notion-mcp** | Notes sync |
| **tavily-mcp** | Better web search |
| **filesystem-mcp** | File operations |
| **chromadb-mcp** | Vector knowledge base |
| **todoist-mcp** | Task management |

## Installation

```bash
# Via npx
npx -y @modelcontextprotocol/server-github

# Via npm
npm install -g @modelcontextprotocol/server-filesystem

# Via pip
pip install mcp-server-firecrawl
```

## Learn→Try→Production

- [x] Learn - Researched MCP ecosystem
- [ ] Try - Install MCP servers
- [ ] Production - Integrate with Harry-001

## References

- https://github.com/mcp (MCP Registry)
- https://modelcontextprotocol.io (Official docs)
- https://github.com/anthropics (Anthropic)
