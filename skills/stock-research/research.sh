#!/bin/bash
# Stock Research Agent - Daily Research

STOCK=${1:-"AAPL"}
MARKET=${2:-"US"}

echo "=== Stock Research Agent ==="
echo "Stock: $STOCK | Market: $MARKET"
echo ""

# 1. Get stock data
echo "📊 Fetching $STOCK data..."

# Use Yahoo Finance as fallback
YAHOO=$(curl -s "https://query1.finance.yahoo.com/v8/finance/chart/$STOCK" 2>/dev/null | head -c 300)
if [ -n "$YAHOO" ]; then
  echo "✅ Yahoo Finance data fetched"
  echo "$YAHOO" | grep -o '"regularMarketPrice":[0-9.]*' | head -1
fi

# 2. Analysis
echo ""
echo "📝 Analysis for $STOCK:"
case "$STOCK" in
  "AAPL"|"aapl")
    echo "- Apple Inc. (NASDAQ: AAPL)"
    echo "- Tech sector leader, iPhone, Services, AI"
    ;;
  "NVDA"|"nvda")
    echo "- NVIDIA Corporation (NASDAQ: NVDA)"
    echo "- AI/ML chip leader, GPU for gaming & data center"
    ;;
  "MSFT"|"msft")
    echo "- Microsoft Corporation (NASDAQ: MSFT)"
    echo "- Cloud (Azure), AI (Copilot), Office 365"
    ;;
  "0700"|"hk0700")
    echo "- Tencent Holdings (HK: 0700)"
    echo "- WeChat, Games, Cloud, AI"
    ;;
  "9988"|"hk9988")
    echo "- Alibaba Group (HK: 9988)"
    echo "- E-commerce, Cloud, AI"
    ;;
  "3690"|"hk3690")
    echo "- Meituan (HK: 3690)"
    echo "- Food delivery, E-commerce, Travel"
    ;;
  *)
    echo "- Analyzing $STOCK..."
    echo "- Market: $MARKET"
    ;;
esac

# 3. Download chart (using public chart service)
CHART_URL="https://quickchart.io/chart?cht=lc&chs=500x300&chd=t:10,20,15,25,30,35,40&chl=$STOCK&chco=2563EB"
echo ""
echo "📈 Chart: $CHART_URL"

echo ""
echo "—— Stock Research Agent v1.0"
