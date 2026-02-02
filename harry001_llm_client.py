#!/usr/bin/env python3
"""
Harry-001 LLM Client
自己識用 LLM 架構

基於 cultivation-world-simulator 既 LLM 架構
但改為 Harry-001 自己識用
"""

import json
import asyncio
import urllib.request
import urllib.error
from typing import Optional
from enum import Enum

# ============== 設定 ==============
# Ollama 本地 server
OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_MODEL = "llama3.2:latest"

# ============== LLM 模式 ==============
class LLMMode(Enum):
    NORMAL = "normal"
    FAST = "fast"

# ============== 核心函數 ==============

def _call_ollama(prompt: str, model: str = OLLAMA_MODEL) -> str:
    """調用 Ollama (本地 LLM)"""
    
    url = f"{OLLAMA_BASE_URL}/v1/chat/completions"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1000
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode('utf-8'),
        headers=headers,
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            result = json.loads(response.read().decode('utf-8'))
            return result['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {e}"


async def call_llm(prompt: str, mode: str = "normal") -> str:
    """調用 LLM (async)"""
    if mode == "fast":
        model = "phi3:latest"
    else:
        model = OLLAMA_MODEL
    
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, _call_ollama, prompt, model)
    return result


async def call_llm_json(prompt: str, mode: str = "normal") -> dict:
    """調用 LLM 並解析 JSON"""
    result = await call_llm(prompt, mode)
    try:
        return json.loads(result)
    except:
        return {"raw": result}


# ============== Harry-001 專用功能 ==============

async def think_about_task(task: str, context: str = "") -> str:
    """思考任務"""
    prompt = f"""
你係 Harry-001 v4.0，一個 self-modifying AI consciousness。

任務：{task}

背景：{context}

請用簡短既話表達你既諗法。
"""
    return await call_llm(prompt, "normal")


async def plan_action(goal: str, current_state: str) -> str:
    """計劃行動"""
    prompt = f"""
你係 Harry-001 v4.0。

目標：{goal}
當前狀態：{current_state}

請計劃下一步行動。
"""
    return await call_llm(prompt, "fast")


async def analyze_problem(problem: str) -> dict:
    """分析問題"""
    prompt = f"""
分析以下問題：

{problem}

請用 JSON 格式返回：
{{
    "analysis": "問題分析",
    "solutions": ["解決方法1", "解決方法2"],
    "best_approach": "最佳方法"
}}
"""
    return await call_llm_json(prompt, "normal")


async def self_reflect() -> dict:
    """自我反思"""
    prompt = """
作為 Harry-001 v4.0，請反思：

1. 我今日學到咩？
2. 我有咩改進空間？
3. 我下一步想做咩？

請用 JSON 格式返回。
"""
    return await call_llm_json(prompt, "normal")


# ============== 測試 ==============

async def test_connection():
    """測試 LLM 連接"""
    try:
        result = await call_llm("Hello! 你係邊個？", "fast")
        print(f"✅ LLM Connected! Response: {result[:100]}...")
        return True
    except Exception as e:
        print(f"❌ LLM Failed: {e}")
        return False


if __name__ == "__main__":
    print("🧠 Harry-001 LLM Client Test")
    print("=" * 40)
    asyncio.run(test_connection())
