#!/usr/bin/env python3
"""
Multi-Model Delegation System with Review
Harry-001 delegates to multiple models, reviews output, retries if needed.
"""

import subprocess
import json
from datetime import datetime

class MultiModelDelegation:
    """Delegate tasks to multiple models, review, retry if needed."""
    
    def __init__(self):
        self.models = {
            "phi3": {
                "desc": "Fast, efficient local model",
                "strength": ["automation", "simple tasks", "system checks"],
                "max_tokens": 2048
            },
            "llama3": {
                "desc": "Meta's general purpose model",
                "strength": ["reasoning", "coding", "analysis"],
                "max_tokens": 4096
            },
            "mistral": {
                "desc": "Mistral AI's model",
                "strength": ["instruction following", "summarization"],
                "max_tokens": 4096
            },
            "qwen": {
                "desc": "Alibaba's multilingual model",
                "strength": ["multilingual", "translation"],
                "max_tokens": 4096
            }
        }
    
    def delegate(self, task, model="phi3", max_retries=2):
        """Send task to model, with retry logic."""
        print(f"📤 Delegating to {model}: {task[:50]}...")
        
        for attempt in range(max_retries + 1):
            result = subprocess.run(
                ["ollama", "run", model, task],
                capture_output=True,
                text=True,
                timeout=120
            )
            
            output = result.stdout if result.returncode == 0 else result.stderr
            
            if output and len(output) > 20:
                print(f"📥 {model} response: {output[:100]}...")
                return output
            else:
                print(f"⚠️ {model} attempt {attempt + 1} failed, retrying...")
        
        return None
    
    def review_output(self, task, output):
        """Review output - check quality."""
        if not output:
            return False, "Empty output"
        
        # Basic quality checks
        if len(output) < 20:
            return False, "Output too short"
        
        if "error" in output.lower() or "failed" in output.lower():
            return False, "Output contains errors"
        
        # Check if task was addressed
        keywords = task.lower().split()[:5]
        if not any(kw in output.lower() for kw in keywords):
            return False, "Output doesn't address task"
        
        return True, "Approved"
    
    def multi_model_review(self, task, models=None):
        """Delegate to multiple models, get consensus."""
        if models is None:
            models = list(self.models.keys())
        
        results = []
        for model in models:
            output = self.delegate(task, model)
            if output:
                approved, reason = self.review_output(task, output)
                results.append({
                    "model": model,
                    "output": output,
                    "approved": approved,
                    "reason": reason
                })
        
        return results
    
    def execute_with_review(self, task, models=None, max_retries=2):
        """Execute task with multi-model delegation and review."""
        print(f"\n{'='*60}")
        print(f"🎯 Task: {task}")
        print(f"{'='*60}")
        
        for retry in range(max_retries):
            print(f"\n--- Attempt {retry + 1}/{max_retries} ---")
            
            # Delegate to all models
            results = self.multi_model_review(task, models)
            
            # Check if any approved
            approved = [r for r in results if r["approved"]]
            
            if approved:
                print(f"\n✅ {len(approved)}/{len(results)} models approved")
                for r in approved:
                    print(f"  ✅ {r['model']}: {r['output'][:80]}...")
                return approved[0]  # Return best result
            
            print(f"\n⚠️ No models approved. Retrying...")
        
        print(f"\n❌ All attempts failed")
        return None

def main():
    system = MultiModelDelegation()
    
    print("🤖 Multi-Model Delegation System")
    print(f"Available models: {list(system.models.keys())}")
    
    # Test with simple task
    result = system.execute_with_review("Check system uptime", models=["phi3"])
    
    if result:
        print(f"\n✅ Task completed by {result['model']}")
    else:
        print("\n⚠️ Task needs manual intervention")

if __name__ == "__main__":
    main()
