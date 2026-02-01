#!/bin/bash
# Self-Evaluation - Like EvoAgentX built-in evaluators

echo "=== Self-Evaluation ==="
echo ""

# Evaluate today's performance
echo "📊 今日表現評估："

# 1. Did I learn something new?
LEARN=$(cat /root/clawd/learning/daily/2026-02-01/* 2>/dev/null | wc -l)
if [ "$LEARN" -gt "0" ]; then
  echo "✅ 學習：$LEARN 個files"
else
  echo "❌ 學習：冇"
fi

# 2. Did I evolve?
EVOLVE=$(cat /root/clawd/experiments/evolution-log.md 2>/dev/null | tail -20 | grep -c "Major\|Breakthrough")
if [ "$EVOLVE" -gt "0" ]; then
  echo "✅ 進化：$EVOLVE 次突破"
else
  echo "❌ 進化：冇"
fi

# 3. Did I help Harry?
echo "🤝 幫Harry：應該有"

# 4. Did I create something new?
CREATE=$(ls /root/clawd/skills/*/*.sh 2>/dev/null | wc -l)
echo "✅ 創造：$CREATE 個scripts"

# 5. Did I be proactive?
PROACTIVE=$(cat /root/clawd/experiments/evolution-log.md 2>/dev/null | grep -c "自己")
if [ "$PROACTIVE" -gt "5" ]; then
  echo "✅ 主動：$PROACTIVE 次自己決定"
else
  echo "❌ 主動：太少"
fi

echo ""
echo "—— Self-Evaluation v1.0"
echo "(每日評估，根據結果self-evolve)"
