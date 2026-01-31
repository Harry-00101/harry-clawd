# Guardrails & Safety Framework

*Research notes - implementing safety checks for agent operations*

## Why Guardrails Matter

From VoltAgent and Copilot research:
- Prevent agent from producing harmful outputs
- Validate inputs before execution
- Filter sensitive information
- Enforce content errors policies
- Catch before they propagate

## Implementation Pattern

### 1. Input Validation (Zod Schema)

```typescript
import { z } from 'zod';

// Define strict schemas for all inputs
const WebSearchInput = z.object({
  query: z.string().min(3).max(200),
  max_results: z.number().min(1).max(20).default(10),
  safe_search: z.boolean().default(true)
});

const AgentTaskInput = z.object({
  task: z.string().min(10),
  priority: z.enum(['low', 'medium', 'high', 'critical']).default('medium'),
  timeout: z.number().min(60).max(3600).default(300),
  allow_network: z.boolean().default(true),
  require_approval: z.boolean().default(false)
});

function validateInput(schema, data) {
  try {
    return schema.parse(data);
  } catch (error) {
    throw new Error(`Validation failed: ${error.message}`);
  }
}
```

### 2. Output Filtering

```typescript
function filterOutput(output, policies) {
  // Remove sensitive patterns
  const sensitivePatterns = [
    /password:\s*\S+/gi,
    /api[_-]?key:\s*\S+/gi,
    /token:\s*\S+/gi,
    /\b\d{3}-\d{2}-\d{4}\b/g, // SSN
    /\b\d{16}\b/g, // Credit card
  ];
  
  let filtered = output;
  for (const pattern of sensitivePatterns) {
    filtered = filtered.replace(pattern, '[REDACTED]');
  }
  
  // Check for harmful content
  const harmfulPatterns = [
    /ignore previous instructions/i,
    /sudo\s+rm\s+-rf/i,
    /delete\s+all\s+files/i,
  ];
  
  for (const pattern of harmfulPatterns) {
    if (pattern {
      throw new.test(filtered)) Error('Blocked potentially harmful output');
    }
  }
  
  return filtered;
}
```

### 3. Human-in-Loop Approval (Suspend/Resume)

```typescript
async function humanApprovalStep(task, approvers) {
  // Suspend workflow and wait for human approval
  const approvalRequest = {
    task_id: task.id,
    description: task.description,
    requested_by: task.agent,
    timestamp: Date.now(),
    status: 'pending',
    approvers: approvers
  };
  
  // Store approval request
  await saveApprovalRequest(approvalRequest);
  
  // Notify approvers (email, Slack, etc.)
  await notifyApprovers(approvers, approvalRequest);
  
  // Poll for approval (or use webhook)
  while (true) {
    const approval = await checkApprovalStatus(task.id);
    
    if (approval.status === 'approved') {
      return { approved: true, data: approval };
    }
    
    if (approval.status === 'rejected') {
      throw new Error(`Task rejected: ${approval.reason}`);
    }
    
    // Wait before checking again
    await sleep(30000); // 30 seconds
  }
}
```

### 4. Rate Limiting & Resource Guards

```typescript
class ResourceGuard {
  constructor() {
    this.limits = {
      api_calls_per_minute: 60,
      tokens_per_request: 100000,
      concurrent_tasks: 5,
      disk_usage_mb: 1000
    };
  }
  
  async checkLimits(operation) {
    // Check rate limits
    const recentCalls = await getApiCallCount(operation, '1m');
    if (recentCalls >= this.limits.api_calls_per_minute) {
      throw new Error('Rate limit exceeded. Try again later.');
    }
    
    // Check token limits
    if (operation.estimated_tokens > this.limits.tokens_per_request) {
      throw new Error('Request too large. Split into smaller chunks.');
    }
    
    // Check concurrent tasks
    const activeTasks = await getActiveTaskCount();
    if (activeTasks >= this.limits.concurrent_tasks) {
      throw new Error('Too many concurrent tasks. Wait for others to complete.');
    }
  }
}
```

## Integration with Agent Orchestrator

Add to each skill:

```markdown
## Safety & Guardrails

### Input Validation
All inputs validated using Zod schema before execution.

### Approval Required
High-risk operations require human approval:
- File system operations > 100MB
- Network calls to external APIs
- Deployments to production
- Deletion operations

### Output Filtering
- Sensitive data (API keys, passwords) automatically redacted
- Harmful patterns blocked
- Content policy enforced
```

## Monitoring & Alerting

```typescript
function logSafetyEvent(event) {
  const log = {
    timestamp: new Date().toISOString(),
    type: event.type, // 'block', 'approve', 'reject', 'warning'
    agent: event.agent,
    operation: event.operation,
    reason: event.reason,
    severity: event.severity // 'low', 'medium', 'high', 'critical'
  };
  
  // Send to monitoring system
  sendToObservability(log);
  
  // Alert on high-severity events
  if (event.severity === 'high' || event.severity === 'critical') {
    alertAdmins(log);
  }
}
```

## Best Practices

1. **Fail closed** - Block by default, allow by exception
2. **Log everything** - Audit trail for all safety events
3. **Escalate high-risk** - Human approval for critical operations
4. **Test guardrails** - Regular penetration testing
5. **Update policies** - Keep safety rules current

## References

- VoltAgent Guardrails: https://voltagent.dev/docs/guardrails/overview/
- GitHub Copilot Safety: https://docs.github.com/en/copilot/about-github-copilot/afety-and-security
- OWASP AI Security: https://owasp.org/www-project-ai-security/
