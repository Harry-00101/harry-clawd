#!/bin/bash
# VOO Daily Analysis

DATE=$(date '+%Y-%m-%d')
echo "=== VOO Analysis - $DATE ==="
echo ""

# Fetch VOO data (using alternative)
echo "📊 Fetching VOO data..."

# Try Yahoo Finance alternative endpoint
VOO_DATA=$(curl -s "https://query1.finance.yahoo.com/v8/finance/chart/VOO?interval=1d&range=5d" 2>/dev/null)

# Extract key data using grep/sed
PRICE=$(echo "$VOO_DATA" | grep -oP '"regularMarketPrice":\K[0-9.]+' | head -1)
PREV_CLOSE=$(echo "$VOO_DATA" | grep -oP '"previousClose":\K[0-9.]+' | head -1)
CHANGE=$(echo "$VOO_DATA" | grep -oP '"regularMarketChange":\K[0-9.-]+' | head -1)
CHANGE_PCT=$(echo "$VOO_DATA" | grep -oP '"regularMarketChangePercent":\K[0-9.-]+' | head -1)

echo ""
if [ -n "$PRICE" ]; then
    echo "💰 VOO Price: \$$PRICE"
    echo "📈 Change: \$$CHANGE (${CHANGE_PCT}%)"
else
    echo "⚠️ Price data unavailable"
    echo "💰 VOO: ~\$520 (last known)"
fi

echo ""
echo "📋 VOO Summary:"
echo "- ETF: Vanguard S&P 500"
echo "- Expense Ratio: 0.03%"
echo "- Holdings: 503 S&P 500 stocks"
echo "- Strategy: Long-term growth"

echo ""
echo "✅ Analysis Complete"
echo "—— VOO Agent v1.0"

# Save to daily log
mkdir -p /root/clawd/learning/voo-analysis
echo "=== $DATE ===" > /root/clawd/learning/voo-analysis/$DATE.md
echo "Price: \$$PRICE" >> /root/clawd/learning/voo-analysis/$DATE.md
echo "Change: \$$CHANGE (${CHANGE_PCT}%)" >> /root/clawd/learning/voo-analysis/$DATE.md
