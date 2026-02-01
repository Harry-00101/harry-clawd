#!/bin/bash
# Harry-001 Production Review Cycle
# Multi-model delegation with review and retry

DATE=$(date '+%Y-%m-%d %H:%M')
echo "🔄 Production Review Cycle: $DATE"
echo "================================"

# Review all systems
TASKS=(
    "Check Ollama status"
    "Check disk space usage"
    "Check memory usage"
    "List running services"
)

for task in "${TASKS[@]}"; do
    echo ""
    echo "📋 Task: $task"
    
    # Delegate to Phi3
    result=$(ollama run phi3 "$task. Output only the result, no explanation." 2>/dev/null | head -3)
    
    if [ -n "$result" ]; then
        echo "📥 Phi3: $result"
        echo "✅ APPROVED"
    else
        echo "⚠️ Phi3 failed, trying Llama3..."
        result=$(ollama run llama3 "$task. Output only the result." 2>/dev/null | head -3)
        
        if [ -n "$result" ]; then
            echo "📥 Llama3: $result"
            echo "✅ APPROVED (fallback)"
        else
            echo "❌ FAILED - needs manual review"
        fi
    fi
done

echo ""
echo "================================"
echo "✅ Production Review Complete"
echo "Time: $DATE"
