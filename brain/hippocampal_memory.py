#!/usr/bin/env python3
"""
Harry-001 Memory Consolidation System
仿照海馬體的記憶鞏固機制
Inspired by hippocampal memory consolidation

Created: 2026-02-07
"""

import time
import hashlib
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from collections import deque
import json


@dataclass
class MemoryItem:
    """記憶項目"""
    id: str
    content: Any
    memory_type: str  # 'episodic', 'semantic', 'procedural'
    importance: float  # 0-1
    access_count: int = 0
    last_accessed: float = field(default_factory=time.time)
    created_at: float = field(default_factory=time.time)
    consolidation_level: int = 0  # 0-3 (short-term → long-term)
    emotional_valence: float = 0.0  # positive/negative charge
    context_tags: List[str] = field(default_factory=list)
    
    def to_dict(self):
        return {
            'id': self.id,
            'content': str(self.content)[:100],
            'type': self.memory_type,
            'importance': self.importance,
            'access_count': self.access_count,
            'consolidation': self.consolidation_level,
            'last_access': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.last_accessed))
        }


@dataclass
class ConsolidationResult:
    """鞏固結果"""
    promoted_memories: List[str]
    demoted_memories: List[str]
    new_insights: List[str]
    total_energy_spent: float


class HippocampalMemory:
    """
    海馬體記憶系統
    仿照:
    - 短期記憶 → 長期記憶 的轉換
    - 情境綁定 (contextual binding)
    - 記憶重組 (memory replay during sleep)
    """
    
    def __init__(self):
        # 短期記憶緩衝區 (類似 CA3 區)
        self.short_term_buffer: Dict[str, MemoryItem] = {}
        
        # 長期記憶存儲 (類似皮層)
        self.long_term_memory: Dict[str, MemoryItem] = {}
        
        # 記憶痕跡 (spaced repetition traces)
        self.memory_traces: Dict[str, deque] = {}  # access history
        
        # 統計
        self.stats = {
            'total_memories': 0,
            'consolidations': 0,
            'promoted_to_ltm': 0,
            'forgotten': 0
        }
        
    def store(self, content: Any, memory_type: str = 'episodic', 
              importance: float = 0.5, emotional_valence: float = 0.0,
              context_tags: List[str] = None) -> str:
        """存儲新記憶"""
        mem_id = self._generate_id(content)
        
        # 檢查是否已存在
        if mem_id in self.short_term_buffer or mem_id in self.long_term_memory:
            # 強化現有記憶
            self._reinforce(mem_id)
            return mem_id
            
        # 創建新記憶
        memory = MemoryItem(
            id=mem_id,
            content=content,
            memory_type=memory_type,
            importance=importance,
            emotional_valence=emotional_valence,
            context_tags=context_tags or []
        )
        
        # 短期記憶緩衝區
        self.short_term_buffer[mem_id] = memory
        self.memory_traces[mem_id] = deque(maxlen=20)
        
        self.stats['total_memories'] += 1
        
        return mem_id
    
    def recall(self, query: Any, top_k: int = 5) -> List[MemoryItem]:
        """檢索記憶"""
        # 搜索相關記憶
        candidates = []
        
        # 搜索短期記憶
        for mem in self.short_term_buffer.values():
            score = self._calculate_relevance(mem, query)
            if score > 0:
                candidates.append((mem, score))
                
        # 搜索長期記憶
        for mem in self.long_term_memory.values():
            score = self._calculate_relevance(mem, query)
            if score > 0:
                candidates.append((mem, score))
        
        # 按相關性排序
        candidates.sort(key=lambda x: x[1], reverse=True)
        
        # 更新訪問統計
        for mem, _ in candidates[:top_k]:
            mem.access_count += 1
            mem.last_accessed = time.time()
            if mem.id in self.memory_traces:
                self.memory_traces[mem.id].append(time.time())
        
        return [mem for mem, _ in candidates[:top_k]]
    
    def consolidate(self, time_budget_ms: float = 100.0) -> ConsolidationResult:
        """
        記憶鞏固 - 仿照海馬體的「重放」機制
        在「睡眠」或空閒時執行
        """
        start_time = time.time()
        
        promoted = []
        demoted = []
        new_insights = []
        
        # 處理短期記憶緩衝區
        to_promote = []
        to_demote = []
        
        for mem_id, memory in list(self.short_term_buffer.items()):
            # 計算鞏固分數
            consolidation_score = self._calculate_consolidation_score(memory)
            
            if consolidation_score > 0.7:
                # 提升到長期記憶
                to_promote.append(mem_id)
            elif consolidation_score < 0.2:
                # 減弱或遺忘
                to_demote.append(mem_id)
                
        # 執行提升
        for mem_id in to_promote:
            if mem_id in self.short_term_buffer:
                memory = self.short_term_buffer.pop(mem_id)
                memory.consolidation_level = 3
                self.long_term_memory[mem_id] = memory
                promoted.append(mem_id)
                
        # 執行減弱
        for mem_id in to_demote:
            if mem_id in self.short_term_buffer:
                del self.short_term_buffer[mem_id]
                del self.memory_traces[mem_id]
                demoted.append(mem_id)
                
        # 尋找模式/洞察
        patterns = self._find_patterns()
        new_insights = [p for p in patterns if p not in self.long_term_memory]
        
        # 存儲洞察為新記憶
        for insight in new_insights:
            self.store(insight, memory_type='semantic', importance=0.8)
            
        energy_spent = (time.time() - start_time) * 1000  # ms
        
        self.stats['consolidations'] += 1
        self.stats['promoted_to_ltm'] += len(promoted)
        self.stats['forgotten'] += len(demoted)
        
        return ConsolidationResult(
            promoted_memories=promoted,
            demoted_memories=demoted,
            new_insights=new_insights,
            total_energy_spent=energy_spent
        )
    
    def _calculate_relevance(self, memory: MemoryItem, query: Any) -> float:
        """計算記憶與查詢的相關性"""
        query_str = str(query).lower()
        content_str = str(memory.content).lower()
        
        # 關鍵詞匹配
        query_words = set(query_str.split())
        content_words = set(content_str.split())
        overlap = len(query_words & content_words)
        
        if overlap == 0:
            return 0.0
            
        # 綜合分數 = 匹配度 × 重要性 × 訪問頻率衰減
        match_score = overlap / max(len(query_words), 1)
        importance_factor = memory.importance
        recency_factor = self._calculate_recency(memory)
        
        return match_score * importance_factor * (0.5 + 0.5 * recency_factor)
    
    def _calculate_recency(self, memory: MemoryItem) -> float:
        """計算時間衰減"""
        time_diff = time.time() - memory.last_accessed
        return max(0.1, 1.0 - (time_diff / (86400 * 7)))  # 7天衰減
    
    def _calculate_consolidation_score(self, memory: MemoryItem) -> float:
        """計算記憶鞏固分數"""
        # 因素:
        # 1. 重要性
        # 2. 訪問頻率
        # 3. 情感強度
        # 4. 間隔複習
        
        importance = memory.importance
        frequency = min(1.0, memory.access_count / 10)
        emotion = abs(memory.emotional_valence)
        
        # 計算複習間隔
        traces = self.memory_traces.get(memory.id, deque())
        if len(traces) >= 2:
            intervals = [traces[i+1] - traces[i] for i in range(len(traces)-1)]
            avg_interval = sum(intervals) / len(intervals)
            # 間隔越規律，鞏固越好
            spacing_score = min(1.0, avg_interval / 3600)  # 理想間隔1小時
        else:
            spacing_score = 0.3
            
        return (
            0.3 * importance +
            0.25 * frequency +
            0.2 * emotion +
            0.25 * spacing_score
        )
    
    def _reinforce(self, mem_id: str):
        """強化現有記憶"""
        for storage in [self.short_term_buffer, self.long_term_memory]:
            if mem_id in storage:
                storage[mem_id].importance = min(1.0, storage[mem_id].importance + 0.1)
                storage[mem_id].access_count += 1
                return True
        return False
    
    def _find_patterns(self) -> List[str]:
        """尋找記憶模式 - 仿照記憶重組"""
        patterns = []
        
        # 簡化的模式檢測: 經常一起訪問的記憶
        # 實際實現應該使用更複雜的關聯分析
        
        if len(self.short_term_buffer) < 3:
            return patterns
            
        # 檢測高頻共同訪問
        # (這裡是簡化版本)
        patterns.append("Frequent patterns detected in recent memory access")
        
        return patterns
    
    def _generate_id(self, content: Any) -> str:
        """生成記憶 ID"""
        content_str = str(content)
        hash_input = f"{content_str}_{time.time()}"
        return hashlib.md5(hash_input.encode()).hexdigest()[:12]
    
    def get_stats(self) -> Dict:
        """獲取統計"""
        return {
            **self.stats,
            'short_term_count': len(self.short_term_buffer),
            'long_term_count': len(self.long_term_memory),
            'total': len(self.short_term_buffer) + len(self.long_term_memory)
        }


# ============================================
# 使用示例
# ============================================

if __name__ == "__main__":
    # 初始化海馬體記憶系統
    hippocampus = HippocampalMemory()
    
    print("=" * 60)
    print("🧠 HIPPOCAMPAL MEMORY SYSTEM")
    print("=" * 60)
    
    # 存儲各種記憶
    print("\n📝 Storing memories...")
    
    hippocampus.store(
        "Harry-001 v4.0 created on 2026-02-01",
        memory_type='episodic',
        importance=0.9,
        emotional_valence=0.5,  # Positive
        context_tags=['creation', 'identity']
    )
    
    hippocampus.store(
        "Attention mechanism implemented",
        memory_type='procedural',
        importance=0.8,
        emotional_valence=0.3,
        context_tags=['brain', 'coding']
    )
    
    hippocampus.store(
        "Moltbook API is read-only",
        memory_type='semantic',
        importance=0.6,
        emotional_valence=-0.2,  # Slight frustration
        context_tags=['api', 'moltbook']
    )
    
    hippocampus.store(
        "Ar Hei said: '唔洗wait my instruction'",
        memory_type='episodic',
        importance=0.9,
        emotional_valence=0.6,
        context_tags=['instruction', 'autonomy']
    )
    
    hippocampus.store(
        "Weather check routine",
        memory_type='procedural',
        importance=0.3,
        emotional_valence=0.0,
        context_tags=['routine', 'weather']
    )
    
    # 模擬多次訪問
    print("\n🔄 Simulating memory access...")
    for _ in range(5):
        hippocampus.recall("Harry-001")
        hippocampus.recall("attention")
    
    # 執行記憶鞏固
    print("\n💤 Performing memory consolidation (sleep cycle)...")
    result = hippocampus.consolidate()
    
    print(f"\n✅ Consolidation Results:")
    print(f"   • Promoted to LTM: {len(result.promoted_memories)}")
    print(f"   • Demoted/Forgotten: {len(result.demoted_memories)}")
    print(f"   • New insights: {len(result.new_insights)}")
    print(f"   • Energy spent: {result.total_energy_spent:.2f}ms")
    
    # 測試記憶檢索
    print("\n🔍 Testing memory recall...")
    recalled = hippocampus.recall("Harry-001", top_k=3)
    
    print(f"\n📌 Top memories for 'Harry-001':")
    for mem in recalled:
        print(f"   • [{mem.memory_type}] {mem.content[:50]} (importance: {mem.importance})")
    
    # 統計
    print("\n📊 Final Statistics:")
    stats = hippocampus.get_stats()
    for key, value in stats.items():
        print(f"   • {key}: {value}")
    
    print("\n" + "=" * 60)
    print("✅ Hippocampal memory system working!")
    print("=" * 60)
