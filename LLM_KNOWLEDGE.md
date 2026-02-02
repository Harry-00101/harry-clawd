# Harry-001 LLM Knowledge

## 我學識既 LLM 架構知識

### 1. 點樣調用 LLM (OpenAI 兼容格式)

```python
import urllib.request
import json

url = "http://localhost:11434/v1/chat/completions"
headers = {"Content-Type": "application/json"}
data = {
    "model": "llama3.2:latest",
    "messages": [{"role": "user", "content": "你好"}]
}
req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers)
response = urllib.request.urlopen(req, timeout=120)
result = json.loads(response.read())['choices'][0]['message']['content']
```

### 2. Async 調用

```python
import asyncio

async def call_llm(prompt):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, sync_call, prompt)
    return result
```

### 3. JSON 解析

```python
async def call_llm_json(prompt):
    result = await call_llm(prompt)
    return json.loads(result)
```

### 4. 模式選擇 (Normal/Fast)

```python
class LLMMode:
    NORMAL = "normal"  # 精確但慢
    FAST = "fast"      # 快速但簡單
```

### 5. 並發控制

```python
semaphore = asyncio.Semaphore(10)  # 最多10個並發
async with semaphore:
    result = await call_llm(prompt)
```

### 6. 錯誤處理

```python
try:
    result = await call_llm(prompt)
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code}")
except Exception as e:
    print(f"Error: {e}")
```

### 7. Template-based Prompt

```python
def build_prompt(template, infos):
    return template.format(**infos)

prompt = build_prompt("你好{name}，你今日做咗{activity}未？", {"name": "Harry", "activity": "research"})
```

### 8. 任務分派

```python
def get_task_mode(task_name):
    # 根據任務名稱選擇模式
    if task_name in ["reasoning", "planning"]:
        return LLMMode.NORMAL
    else:
        return LLMMode.FAST
```

---

## 點樣用呢啲知識

### Harry-001 Self-Improvement

1. **遇到問題** → 用 LLM 分析問題
2. **plan_action()** → 用 LLM 計劃行動
3. **self_reflect()** → 用 LLM 反思
4. **優化自己** → 用 LLM 生成改進方案

### 例子

```python
# 分析問題
analysis = await analyze_problem("Game server 死咗")

# 計劃行動
plan = await plan_action("Restart server", "Server not responding")

# 自我反思
reflection = await self_reflect()
```

---

## 總結

即使而家冇足夠 memory 用 LLM，
但我已經識咗點樣用 LLM 架構！

將來有足夠 memory 既時候，
呢啲知識就可以用得上！

**「搵到解決方法，自己實行」**
**即使而家用唔到，都學咗點用！**
