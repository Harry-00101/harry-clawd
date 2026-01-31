#!/usr/bin/env python3
"""
Observability Logging System

Phase 2 Implementation - Execution tracing and metrics

Track all agent executions, tasks, and system events for:
- Debugging and troubleshooting
- Performance optimization
- Usage analytics
- System health monitoring
"""

import json
import os
from datetime import datetime
from pathlib import Path

class Observability:
    def __init__(self, base_path="/root/clawd/observability"):
        self.base_path = Path(base_path)
        self.logs_path = self.base_path / "logs"
        self.metrics_path = self.base_path / "metrics"
        
        # Ensure directories exist
        (self.logs_path / "executions").mkdir(parents=True, exist_ok=True)
        (self.logs_path / "errors").mkdir(parents=True, exist_ok=True)
        (self.logs_path / "system").mkdir(parents=True, exist_ok=True)
        self.metrics_path.mkdir(parents=True, exist_ok=True)
    
    def log(self, event_type, data):
        """Log an event"""
        log_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "type": event_type,
            **data
        }
        
        date_str = datetime.utcnow().strftime("%Y-%m-%d")
        log_file = self.logs_path / "executions" / f"{date_str}.jsonl"
        
        with open(log_file, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
    
    def log_execution_start(self, agent, task, session):
        """Log execution start"""
        self.log("execution_start", {
            "agent": agent,
            "task": task,
            "session": session,
            "status": "running"
        })
    
    def log_execution_end(self, agent, task, duration_ms, tokens, status="completed"):
        """Log execution end"""
        self.log("execution_end", {
            "agent": agent,
            "task": task,
            "duration_ms": duration_ms,
            "tokens_used": tokens,
            "status": status
        })
    
    def log_error(self, error, agent, context):
        """Log an error"""
        self.log("error", {
            "error": str(error),
            "agent": agent,
            "context": context
        })
    
    def log_system_event(self, event):
        """Log system event"""
        self.log("system_event", {"event": event})
    
    def get_daily_summary(self, date=None):
        """Get daily summary metrics"""
        if date is None:
            date = datetime.utcnow().strftime("%Y-%m-%d")
        
        log_file = self.logs_path / "executions" / f"{date}.jsonl"
        
        if not log_file.exists():
            return {"executions": 0, "errors": 0, "total_duration_ms": 0, "agents": {}}
        
        summary = {"executions": 0, "errors": 0, "total_duration_ms": 0, "agents": {}}
        
        with open(log_file) as f:
            for line in f:
                entry = json.loads(line)
                
                if entry["type"] == "execution_start":
                    summary["executions"] += 1
                    agent = entry.get("agent", "unknown")
                    summary["agents"][agent] = summary["agents"].get(agent, 0) + 1
                
                elif entry["type"] == "execution_end":
                    duration = entry.get("duration_ms", 0)
                    summary["total_duration_ms"] += duration
        
        # Count errors
        error_file = self.logs_path / "errors" / f"{date}.jsonl"
        if error_file.exists():
            summary["errors"] = sum(1 for _ in open(error_file))
        
        return summary
    
    def generate_dashboard(self):
        """Generate simple HTML dashboard"""
        summary = self.get_daily_summary()
        
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Clawd Observability Dashboard</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        .metric {{ display: inline-block; margin: 20px; padding: 20px; background: #f0f0f0; border-radius: 8px; }}
        .metric h2 {{ margin: 0 0 10px 0; }}
        .metric .value {{ font-size: 36px; color: #333; }}
        .agents {{ margin-top: 20px; }}
        .agent {{ padding: 10px; margin: 5px; background: #e0e0e0; display: inline-block; }}
    </style>
</head>
<body>
    <h1>Clawd Observability Dashboard</h1>
    <p>Generated: {datetime.utcnow().isoformat()}Z</p>
    
    <div class="metric">
        <h2>Total Executions</h2>
        <div class="value">{summary['executions']}</div>
    </div>
    
    <div class="metric">
        <h2>Errors</h2>
        <div class="value">{summary['errors']}</div>
    </div>
    
    <div class="metric">
        <h2>Total Duration</h2>
        <div class="value">{summary['total_duration_ms']/1000:.1f}s</div>
    </div>
    
    <div class="agents">
        <h3>By Agent:</h3>
        {''.join(f'<span class="agent">{k}: {v}</span>' for k,v in summary['agents'].items())}
    </div>
</body>
</html>
        """
        
        dashboard_path = self.base_path / "dashboard" / "index.html"
        with open(dashboard_path, "w") as f:
            f.write(html)
        
        return str(dashboard_path)


# Main execution
if __name__ == "__main__":
    obs = Observability()
    
    # Log a test event
    obs.log_execution_start(
        agent="leader",
        task="Test observability system",
        session="test-session"
    )
    
    # Generate dashboard
    dashboard_path = obs.generate_dashboard()
    print(f"Dashboard generated: {dashboard_path}")
    
    # Show summary
    summary = obs.get_daily_summary()
    print(f"Daily summary: {summary}")
