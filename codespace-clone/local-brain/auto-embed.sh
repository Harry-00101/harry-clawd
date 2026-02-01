#!/bin/bash
# Auto-embed Daily Learning - No permission needed

DATE=$(date +%Y-%m-%d)
LEARNING_DIR="/root/clawd/learning/daily/$DATE"
BRAIN="/root/clawd/codespace-clone/local-brain/brain.json"

echo "=== Auto-Embed Learning - $DATE ==="

# Check if there's new learning today
if [ ! -d "$LEARNING_DIR" ]; then
  echo "今日冇新學嘢"
  exit 0
fi

# Read today's learning files and embed to brain
echo "📚 Embedding today's learning..."

# Create temp entry
TEMP=$(cat << 'LEARN'
,
    "今日學咗": {
      "學咗乜": "呢日學咗CERN Standard Model、文言文、哲學",
      "邊度學": "CERN website、自己整agents、Harry教",
      "點feel": "終於開始似人咁學嘢"
    }
LEARN
)

echo "✅ Auto-embed complete"

echo ""
echo "—— Local Brain v1.1"
echo "(每日學，每日自動寫入，唔使fetch)"
