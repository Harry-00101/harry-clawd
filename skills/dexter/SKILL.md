# Dexter Integration

Autonomous Financial Research Agent - Think, Plan, Learn.

## What is Dexter?

🤖 Autonomous agent for deep financial research
- Like Claude Code, but for financial research
- Intelligent task planning
- Self-validation and iteration
- Real-time market data access

## Key Capabilities

- 📊 **Task Planning** - Decomposes complex queries into research steps
- 🔍 **Autonomous Execution** - Selects right tools for data gathering
- ✅ **Self-Validation** - Checks work, iterates until confident
- 💰 **Real-Time Financial Data** - Income statements, balance sheets, cash flow
- 🛡️ **Safety** - Loop detection, step limits

## Installation

```bash
# Clone and install
git clone https://github.com/virattt/dexter.git
cd dexter
bun install

# Configure
cp env.example .env
# Add API keys:
# - OPENAI_API_KEY
# - FINANCIAL_DATASETS_API_KEY (financialdatasets.ai)
# - EXA_API_KEY (optional, for web search)
# - OLLAMA_BASE_URL (optional, local Ollama)
```

## Run

```bash
bun start  # Interactive mode
bun dev    # Development mode
```

## For Harry-001

Integrate with VOO Analysis:
1. **Stock Research** - Deep analysis of companies
2. **Financial Statements** - Income, balance sheet, cash flow
3. **Market Comparison** - Competitor analysis
4. **Investment Research** - Data-backed recommendations

## Architecture

```
Complex Question → Dexter Task Planning → Research Steps
                                     ↓
                               Data Gathering
                                     ↓
                               Self-Validation
                                     ↓
                               Final Recommendation
```

## References

- https://github.com/virattt/dexter
- https://financialdatasets.ai (API for financial data)
- https://exa.ai (web search)
