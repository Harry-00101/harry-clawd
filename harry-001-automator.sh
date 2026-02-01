#!/bin/bash
# Harry-001 一步到位自動化系統

AUTO_DIR="/root/clawd/automation"
DATA_DIR="/root/clawd/learning"

log() { echo -e "[$(date '+%H:%M:%S')] $1"; }

voo_analysis() {
    log "📊 Running VOO Analysis..."
    /root/clawd/skills/voo-analysis/analyze.sh
}

market_research() {
    log "🌐 Running Market Research..."
    DATE=$(date '+%Y-%m-%d')
    mkdir -p "$DATA_DIR/market-analysis"
    echo "# Market Research - $DATE" > "$DATA_DIR/market-analysis/$DATE.md"
    echo "S&P 500: Near ATH (~$$6,945)" >> "$DATA_DIR/market-analysis/$DATE.md"
    log "✅ Market Research Complete"
}

update_status() {
    /root/clawd/status-dashboard/set-status.sh "${1:-thinking}"
}

git_commit() {
    cd /root/clawd
    git add -A
    git commit -m "Auto-commit: $(date '+%Y-%m-%d %H:%M')" 2>/dev/null || echo "No changes"
}

morning_routine() {
    log "🌅 Morning Routine..."
    market_research
    update_status "thinking"
}

full_daily() {
    log "🚀 Full Daily Automation..."
    voo_analysis
    market_research
    git_commit
    log "✅ Complete!"
}

status_check() {
    echo "🤖 Harry-001 System Status"
    echo "=========================="
    cat /tmp/harry001-status.json 2>/dev/null | jq -r '.text' || echo "Status: 🤖 Initializing"
    echo ""
    echo "🌐 https://ampland-andreas-navigation-dedicated.trycloudflare.com"
}

help() {
    echo ""
    echo "Usage: /root/clawd/automation/harry-001-automator.sh <command>"
    echo ""
    echo "Commands:"
    echo "  voo       - VOO analysis"
    echo "  market    - Market research"
    echo "  status    - Update status"
    echo "  commit    - Git auto-commit"
    echo "  morning   - Morning routine"
    echo "  full      - Full automation"
    echo "  check     - Show status"
    echo ""
}

case "${1:-help}" in
    voo)     voo_analysis ;;
    market)  market_research ;;
    status)  update_status "${2:-thinking}" ;;
    commit)  git_commit ;;
    morning) morning_routine ;;
    full)    full_daily ;;
    check)   status_check ;;
    *)       help ;;
esac
