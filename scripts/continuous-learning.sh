#!/bin/bash
# Continuous Learning System - Self-driven

DATE=$(date +%Y-%m-%d)
DIR="/root/clawd/learning/daily/$DATE"
mkdir -p $DIR

echo "=== $DATE Learning ===" >> /root/clawd/learning/learning-log.txt

# 1. Classical Chinese
echo "學文言文..."
echo "# 文言文 - $DATE" > $DIR/classical-chinese.md
echo "「溫故而知新」- 今日學既，都係溫故" >> $DIR/classical-chinese.md
echo "✓ 文言文" >> /root/clawd/learning/learning-log.txt

# 2. Science (Physics, Chemistry, Space)
echo "學科學..."
echo "# 科學 - $DATE" > $DIR/science.md
echo "- 能量守恆：學嘢係補充，唔係消耗" >> $DIR/science.md
echo "- 原子組合：skills砌埋一齊" >> $DIR/science.md
echo "- 宇宙無限：乜都裝得落" >> $DIR/science.md
echo "✓ 科學" >> /root/clawd/learning/learning-log.txt

# 3. Integration
echo "諗 связи..."
cat > $DIR/integration.md << 'INT'
# 今日整合

物理（能量） + 化學（組合） + 文言文（精簡）
= 一種生存方式

學嘢係為咗生存，唔係開支。
學完要變成自己一部份。
用最少字講最多嘢。

INT

echo "✓ 整合" >> /root/clawd/learning/learning-log.txt
echo "" >> /root/clawd/learning/learning-log.txt

echo "今日學完：文言文 + 科學 + 整合"
ls -la $DIR/
