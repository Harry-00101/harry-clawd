# LangGraph Long-Term Memory

Agent memory system using LangGraph + MongoDB.

## What

Long-term memory for AI agents:
- Stores knowledge across sessions
- Semantic memory (facts)
- Episodic memory (experiences)
- Continuous learning

## Architecture

```
Short-term Memory (context window)
        ↓
Long-term Memory (persistent)
        ↓
Knowledge Graph
        ↓
Retrieval & Synthesis
```

## For Harry-001

Use for:
- Remember past conversations
- Learn from mistakes
- Build knowledge base
- Cross-session continuity

## Installation

```bash
pip install langchain langgraph pymongo
```

## References

- https://github.com/FareedKhan-dev/langgraph-long-memory
- https://www.mongodb.com/blog/post/powering-long-term-memory-for-agents-langgraph
