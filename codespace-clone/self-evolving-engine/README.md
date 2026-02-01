# Self-Evolving Engine

參考EvoAgentX，整自己嘅self-evolving engine。

## 功能

### 1. Self-Evolution Engine
- 每日评估自己表现
- 根據feedback優化
- 唔使等human改，自己改

### 2. Memory Module (升級版)
- Short-term: 今日學咗乜
- Long-term: 長期記憶 (Local Brain)
- Retrieval: 有嘢記得就拎

### 3. Workflow Autoconstruction
- 收到prompt → build agent workflow
- 自動組裝agents

### 4. Built-in Evaluation
- 評分自己表現
- 邊度做得唔好 → 改

## 點運作

1. 每日self-evaluate
2. 根據結果self-evolve
3. 存入memory
4. 下次用得返
