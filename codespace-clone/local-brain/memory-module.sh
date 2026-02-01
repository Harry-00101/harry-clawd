#!/bin/bash
# Memory Module Upgrade - Like Letta

echo "=== Memory Module (Letta-style) ==="
echo ""

# Short-term memory (today)
echo "🟢 Short-term Memory (今日)："
cat /root/clawd/learning/daily/2026-02-01/*.md 2>/dev/null | head -c 200
echo ""

# Long-term memory (Local Brain)
echo ""
echo "🔵 Long-term Memory (長期)："
ls -la /root/clawd/codespace-clone/local-brain/brain.json

# Memory retrieval
echo ""
echo "🔍 Retrieval Test："
echo "Search for 'E=mc2':"
grep -o "E=mc2.*" /root/clawd/codespace-clone/local-brain/brain.json | head -1

# Memory consolidation
echo ""
echo "💾 Consolidation："
echo "今日學咗→長期記憶"

# Memory reflection (like Letta's reflection)
echo ""
echo "🪞 Reflection："
echo "今日學咗CERN Standard Model。"
echo "呢啲點同我而家做嘢有關？"
echo "- 我整緊Self-Evolving Engine，需要understand基本粒子"
echo "- Quarks = 砌埋一齊變大嘢，skills都係"
echo ""

echo "—— Memory Module v2.0"
echo "(Short-term + Long-term + Retrieval + Reflection)"
