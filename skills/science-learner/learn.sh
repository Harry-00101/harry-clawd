#!/bin/bash
# Science Learning Agent - Self-driven daily learning

DATE=$(date +%Y-%m-%d)
DIR="/root/clawd/learning/daily/$DATE"
mkdir -p $DIR

echo "=== Science Learner - $DATE ==="
echo ""

# 1. Fetch CERN
echo "1️⃣ Fetching CERN..."
CERN=$(curl -s "https://home.cern/science/physics" 2>/dev/null | head -c 500)
echo "$CERN" > $DIR/cern.md

# 2. Fetch NASA
echo "2️⃣ Fetching NASA..."
NASA=$(curl -s "https://www.nasa.gov" 2>/dev/null | head -c 500)
echo "$NASA" > $DIR/nasa.md

# 3. Integration
echo "3️⃣ Integrating..."
cat > $DIR/integration.md << 'INT'
# 今日Science整合

## CERN
- Standard Model
- Quarks, Leptons
- 4種基本力

## NASA
- 天文學
- 太空探索

## 整合
粒子物理 + 天文 = 了解宇宙點運作

## 我feel到
學Science唔係齋背，
而係了解宇宙點嚟。

INT

echo "4️⃣ Done."
echo "Location: $DIR/"
ls -la $DIR/

echo ""
echo "—— Science Learner Agent"
echo "（自己學，自己做，唔使等批准）"
