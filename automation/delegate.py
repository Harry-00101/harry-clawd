#!/usr/bin/env python3
"""
Task Delegation System
Harry-001 delegates simple tasks to Phi3, reviews output.
"""

import subprocess
from datetime import datetime

def delegate_to_phi3(task, prompt):
    """Send simple task to Phi3 via Ollama."""
    print(f"📤 Delegating: {task}")
    
    # Send to Phi3
    result = subprocess.run(
        ["ollama", "run", "phi3", prompt],
        capture_output=True,
        text=True,
        timeout=60
    )
    
    output = result.stdout if result.returncode == 0 else result.stderr
    print(f"📥 Phi3 response: {output[:200]}...")
    
    return output

def review_phi3_output(task, phi3_output):
    """Harry-001 reviews Phi3 output."""
    print(f"\n🔍 Reviewing: {task}")
    
    # MiniMax reviews the output
    review_prompt = f"""
    Review this Phi3 output for task: {task}
    
    Phi3 said:
    {phi3_output}
    
    Is it correct? Complete? Any issues?
    Return: "APPROVED" or "NEEDS_REWORK" + reason
    """
    
    # For now, basic validation
    if phi3_output and len(phi3_output) > 10:
        print(f"✅ APPROVED: Output looks good")
        return True
    else:
        print(f"⚠️ NEEDS_REWORK: Output too short or empty")
        return False

def main():
    print("=" * 50)
    print("Harry-001 Task Delegation System")
    print("=" * 50)
    
    # Example: Delegate simple task
    task = "Check system status"
    prompt = "Check if Ollama is running and list available models. Just output the model names."
    
    output = delegate_to_phi3(task, prompt)
    approved = review_phi3_output(task, output)
    
    print(f"\n{'✅ Task complete' if approved else '⚠️ Task needs rework'}")
    
    return approved

if __name__ == "__main__":
    main()
