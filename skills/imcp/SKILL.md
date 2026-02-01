# iMCP Integration

macOS app for connecting your digital life with AI via MCP.

## What is iMCP?

By mattt (famous iOS developer, ex-Apple):
- macOS app providing MCP server
- Connects: Calendar, Messages, Contacts, Location, Maps, Reminders, Weather
- Works with Claude Desktop and other MCP clients
- Privacy-focused (no data collection)

## mattt

Legendary iOS developer:
- Former Apple Developer Relations
- Created many popular iOS libraries
- Known for: Alamofire, Surge, etc.
- Active open source contributor
- Now building AI tools

## Capabilities

| Service | Data |
|---------|------|
| **Calendar** | View/create events, recurrence, alarms |
| **Messages** | Message history by contact/date |
| **Contacts** | Search by name, phone, email |
| **Location** | Current location, coordinates |
| **Maps** | Place search, directions, POI |
| **Reminders** | View/create with due dates, priorities |
| **Weather** | Current conditions, wind, temperature |

## Installation

```bash
# Via Homebrew
brew install --cask mattt/tap/iMCP

# Or download from https://iMCP.app/download
# Requires macOS 15.3+
```

## Architecture

```
macOS Apps (Calendar, Messages, etc.)
        ↓
   iMCP (MCP Server)
        ↓
   MCP Protocol
        ↓
   AI Client (Claude Desktop, etc.)
```

## For Harry-001

Learn from iMCP's approach:
1. **Privacy-first** - No data collection
2. **Local-first** - Data stays on device
3. **Standard protocol** - MCP for integration
4. **Clean UX** - Simple permission model

## MCP Integration Pattern

iMCP demonstrates MCP's power:
- Connect local apps to AI
- Rich, contextual data
- Privacy controls
- Standardized access

## References

- https://github.com/mattt/iMCP
- https://iMCP.app/download
- https://modelcontextprotocol.io
- mattt's GitHub: https://github.com/mattt
