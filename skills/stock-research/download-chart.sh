#!/bin/bash
# Download stock chart as image

STOCK=${1:-"AAPL"}
OUTPUT_DIR="/root/clawd/skills/stock-research/charts"

mkdir -p "$OUTPUT_DIR"

# Generate chart URL
CHART_URL="https://quickchart.io/chart?cht=lc&chs=600x400&chd=t:10,20,15,25,30,35,40,45,50,55&chl=$STOCK&chco=2563EB&chf=bg,s,1a1a2e"

# Download
OUTPUT_FILE="$OUTPUT_DIR/${STOCK}.png"
curl -s "$CHART_URL" -o "$OUTPUT_FILE"

echo "=== Downloaded: $OUTPUT_FILE ==="
ls -la "$OUTPUT_DIR/"
