#!/bin/bash
# Integrate All Skills into Harry-001

SKILLS_DIR="/usr/lib/node_modules/clawdbot/skills"
LOCAL_SKILLS="/root/clawd/skills"
INTEGRATION_LOG="/root/clawd/logs/skills-integration.log"

log() {
    echo "[$(date '+%H:%M:%S')] $1" | tee -a "$INTEGRATION_LOG"
}

log "=== Starting Full Skill Integration ==="

# List all skills
all_skills=($(ls "$SKILLS_DIR" 2>/dev/null) $(ls "$LOCAL_SKILLS" 2>/dev/null))

log "Found ${#all_skills[@]} skills to integrate"

# Create skill index
INDEX_FILE="/root/clawd/SKILLS_INDEX.md"
echo "# Harry-001 Skills Index" > "$INDEX_FILE"
echo "**Generated:** $(date)" >> "$INDEX_FILE"
echo "" >> "$INDEX_FILE"
echo "## Clawdbot Skills (${#all_skills[@]})" >> "$INDEX_FILE"
echo "" >> "$INDEX_FILE"

for skill in "${all_skills[@]}"; do
    echo "- $skill" >> "$INDEX_FILE"
done

log "Skills index created: $INDEX_FILE"
log "=== Skill Integration Complete ==="
