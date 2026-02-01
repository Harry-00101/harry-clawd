#!/bin/bash
# Fetch Science Learning Materials (YouTube/Podcasts alternative)

echo "=== Science Learning Materials ==="
echo ""

# Science channels to check (simulated)
CHANNELS=(
  "Kurzgesagt"
  "Veritasium"
  "Physics Girl"
  "Numberphile"
)

echo "🎬 Recommended Science Channels:"
for channel in "${CHANNELS[@]}"; do
  echo "   - $channel"
done

echo ""
echo "📚 Learn E=mc² from:"
echo "   1. Einstein's original paper (1905)"
echo "   2. CERN website - particle physics"
echo "   3. NASA - sun's energy"
echo "   4. BBC Bitesize - relativity"

echo ""
echo "🎧 Alternative: Listen to science podcasts"
echo "   - Science Vs"
echo "   - Radiolab"
echo "   - BBC Inside Science"

echo ""
echo "=== Learning Sources ==="
echo "Location: /root/clawd/learning/multimedia/"
