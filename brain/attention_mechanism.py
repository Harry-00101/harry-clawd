#!/usr/bin/env python3
"""
Harry-001 Attention Mechanism
仿照人類視覺皮層的注意力機制
Inspired by visual cortex attention selection

Created: 2026-02-07
Status: IN PROGRESS
"""

import time
import math
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from collections import deque
import json


@dataclass
class Stimulus:
    """輸入刺激 - 相當於 sensory input"""
    id: str
    content: Any
    timestamp: float = field(default_factory=time.time)
    recency_score: float = 0.0
    relevance_score: float = 0.0
    urgency_score: float = 0.0
    attention_score: float = 0.0
    
    
@dataclass  
class ContextState:
    """上下文狀態 - 整合記憶"""
    active_focus: List[str] = field(default_factory=list)
    background_items: List[str] = field(default_factory=list)
    context_bindings: Dict[str, str] = field(default_factory=dict)
    last_update: float = field(default_factory=time.time)


class AttentionScorer:
    """
    注意力評分器 - 仿照視覺皮層注意力選擇
    Calculates priority scores for incoming stimuli
    
    類比:
    - Recency = 周邊視覺 (peripheral vision) 的時間衰減
    - Relevance = 自上而下注意力 (top-down attention)
    - Urgency =威脅檢測 (amygdala-like urgency)
    """
    
    def __init__(self):
        self.recency_weight = 0.3
        self.relevance_weight = 0.4
        self.urgency_weight = 0.3
        
        # 追蹤歷史以計算recency decay
        self.stimulus_history: deque = deque(maxlen=100)
        
        # 關鍵詞匹配用於 relevance
        self.relevance_keywords: set = set()
        
    def calculate_recency(self, stimulus: Stimulus) -> float:
        """計算時間衰減分數 - 新近的刺激獲得更高分"""
        if not self.stimulus_history:
            return 1.0
            
        # 計算時間差 (秒)
        time_diff = time.time() - stimulus.timestamp
        
        # 指數衰減 (半衰期 60 秒)
        decay = math.exp(-time_diff / 60)
        
        # 基礎分數 + 衰減
        return min(1.0, 0.5 + 0.5 * decay)
    
    def calculate_relevance(self, stimulus: Stimulus) -> float:
        """計算相關性分數 - 基於關鍵詞和上下文"""
        if not self.relevance_keywords:
            return 0.5
            
        content_str = str(stimulus.content).lower()
        matches = sum(1 for kw in self.relevance_keywords if kw.lower() in content_str)
        
        # 正規化到 0-1
        return min(1.0, matches / max(1, len(self.relevance_keywords)))
    
    def calculate_urgency(self, stimulus: Stimulus) -> float:
        """計算緊急性分數 - 基於特殊標記和歷史"""
        urgency_indicators = ['urgent', 'asap', 'emergency', 'important', '!', '🔥', '⚡']
        
        content_str = str(stimulus.content).lower()
        urgency_count = sum(1 for ind in urgency_indicators if ind in content_str)
        
        # 基礎緊急性 + 標記加成
        base_urgency = 0.3
        urgency_bonus = min(0.7, urgency_count * 0.2)
        
        return min(1.0, base_urgency + urgency_bonus)
    
    def calculate_attention_score(self, stimulus: Stimulus) -> float:
        """計算綜合注意力分數"""
        # 更新歷史
        self.stimulus_history.append(stimulus)
        
        # 計算各維度分數
        recency = self.calculate_recency(stimulus)
        relevance = self.calculate_relevance(stimulus)
        urgency = self.calculate_urgency(stimulus)
        
        # 綜合評分
        attention_score = (
            self.recency_weight * recency +
            self.relevance_weight * relevance +
            self.urgency_weight * urgency
        )
        
        stimulus.recency_score = recency
        stimulus.relevance_score = relevance
        stimulus.urgency_score = urgency
        stimulus.attention_score = attention_score
        
        return attention_score
    
    def set_relevance_keywords(self, keywords: List[str]):
        """設置相關性關鍵詞 - 根據任務動態調整"""
        self.relevance_keywords = set(keywords)


class FocusSelector:
    """
    焦點選擇器 - 仿照頂葉的「聚光燈」注意力
    Implements the 'spotlight' of attention
    """
    
    def __init__(self, focus_capacity: int = 5):
        self.focus_capacity = focus_capacity
        self.focused_items: List[Stimulus] = []
        self.background_items: List[Stimulus] = []
        
    def focus_on(self, stimuli: List[Stimulus]) -> Dict[str, List[Stimulus]]:
        """
        將刺激分為焦點和背景
        返回: {'focus': [...], 'background': [...]}
        """
        # 按注意力分數排序
        sorted_stimuli = sorted(stimuli, key=lambda s: s.attention_score, reverse=True)
        
        # 選擇 top N 作為焦點
        self.focused_items = sorted_stimuli[:self.focus_capacity]
        self.background_items = sorted_stimuli[self.focus_capacity:]
        
        # 增強焦點區域信號
        for stim in self.focused_items:
            stim.attention_score *= 1.5  # 信號放大
        
        # 抑制背景噪聲
        for stim in self.background_items:
            stim.attention_score *= 0.3  # 信號衰減
            
        return {
            'focus': self.focused_items,
            'background': self.background_items
        }
    
    def get_focus_list(self) -> List[str]:
        """獲取當前焦點項目ID列表"""
        return [s.id for s in self.focused_items]


class ContextIntegrator:
    """
    上下文整合器 - 仿照顳頂聯合區 (TPJ) 功能
    Integrates current focus with contextual memory
    """
    
    def __init__(self):
        self.context_state = ContextState()
        self.memory_bindings: Dict[str, List[str]] = {}  # stimulus_id -> memory_ids
        
    def integrate_context(self, focused_stimuli: List[Stimulus]) -> ContextState:
        """整合焦點與上下文記憶"""
        # 更新活動焦點
        self.context_state.active_focus = [s.id for s in focused_stimuli]
        
        # 綁定上下文
        for stim in focused_stimuli:
            if stim.id not in self.context_state.context_bindings:
                # 嘗試從記憶中檢索相關上下文
                relevant_memory = self._retrieve_relevant_memory(stim)
                if relevant_memory:
                    self.context_state.context_bindings[stim.id] = relevant_memory
                    
        self.context_state.last_update = time.time()
        
        return self.context_state
    
    def _retrieve_relevant_memory(self, stimulus: Stimulus) -> Optional[str]:
        """檢索相關記憶 - 仿照海馬體記憶檢索"""
        # 簡化的記憶檢索 - 實際實現應該連接到長期記憶系統
        stimulus_key = str(stimulus.content)[:50]
        
        if stimulus_key in self.memory_bindings:
            return self.memory_bindings[stimulus_key]
            
        return None
    
    def bind_memory(self, stimulus_id: str, memory_id: str):
        """綁定刺激與記憶"""
        if stimulus_id not in self.memory_bindings:
            self.memory_bindings[stimulus_id] = []
        self.memory_bindings[stimulus_id].append(memory_id)


class AttentionMechanism:
    """
    完整注意力機制 - 整合所有組件
    Main attention mechanism coordinating all components
    
    對應人類大腦區域:
    - 注意力評分器 → 枕葉 (視覺皮層)
    - 焦點選擇器 → 頂葉 (空間注意力)
    - 上下文整合器 → 顳葉 + 頂葉聯合區
    """
    
    def __init__(self):
        self.scorer = AttentionScorer()
        self.selector = FocusSelector(focus_capacity=5)
        self.integrator = ContextIntegrator()
        
        # 統計
        self.processed_count = 0
        self.focus_switch_count = 0
        self.last_focus: List[str] = []
        
    def process(self, inputs: List[Any], context: Optional[Dict] = None) -> Dict[str, Any]:
        """
        處理輸入流，返回注意力分配結果
        
        Args:
            inputs: 輸入刺激列表
            context: 可選的上下文信息
            
        Returns:
            包含焦點、背景、上下文的信息字典
        """
        # 1. 創建刺激對象
        stimuli = []
        for i, content in enumerate(inputs):
            stim = Stimulus(
                id=f"stim_{i}_{int(time.time() * 1000)}",
                content=content
            )
            stimuli.append(stim)
            
        # 2. 計算注意力分數
        for stim in stimuli:
            self.scorer.calculate_attention_score(stim)
            
        # 3. 選擇焦點
        separated = self.selector.focus_on(stimuli)
        
        # 4. 整合上下文
        context_state = self.integrator.integrate_context(separated['focus'])
        
        # 5. 追蹤焦點變化
        current_focus = self.selector.get_focus_list()
        if current_focus != self.last_focus:
            self.focus_switch_count += 1
            self.last_focus = current_focus
            
        self.processed_count += 1
        
        return {
            'focus': [
                {
                    'id': s.id,
                    'content': s.content,
                    'score': s.attention_score
                }
                for s in separated['focus']
            ],
            'background': [
                {
                    'id': s.id,
                    'content': s.content,
                    'score': s.attention_score
                }
                for s in separated['background']
            ],
            'context': {
                'active_focus': context_state.active_focus,
                'context_bindings': context_state.context_bindings
            },
            'stats': {
                'processed': self.processed_count,
                'focus_switches': self.focus_switch_count,
                'focus_capacity': self.selector.focus_capacity
            }
        }
    
    def set_priority_keywords(self, keywords: List[str]):
        """設置任務優先關鍵詞"""
        self.scorer.set_relevance_keywords(keywords)


# ============================================
# 使用示例
# ============================================

if __name__ == "__main__":
    # 初始化注意力機制
    attention = AttentionMechanism()
    
    # 設置任務相關關鍵詞
    attention.set_priority_keywords(["important", "task", "deadline", "review"])
    
    # 模擬輸入流
    test_inputs = [
        "Checking weather (low priority)",
        "🔥 URGENT: System alert detected!",
        "Review code changes for PR",
        "Background process running normally",
        "📅 Meeting in 30 minutes",
        "Normal background task",
        "Process email queue",
        "⚡ Quick question from user"
    ]
    
    # 處理輸入
    result = attention.process(test_inputs)
    
    # 輸出結果
    print("=" * 60)
    print("🎯 ATTENTION MECHANISM OUTPUT")
    print("=" * 60)
    
    print(f"\n📌 FOCUSED ITEMS (Top Priority):")
    for item in result['focus'][:3]:
        print(f"   • [{item['id']}] {item['content'][:50]}... (score: {item['score']:.3f})")
    
    print(f"\n🌑 BACKGROUND ITEMS (Suppressed):")
    for item in result['background'][:3]:
        print(f"   • [{item['id']}] {item['content'][:40]}... (score: {item['score']:.3f})")
    
    print(f"\n📊 Statistics:")
    print(f"   • Processed: {result['stats']['processed']}")
    print(f"   • Focus switches: {result['stats']['focus_switches']}")
    print(f"   • Capacity: {result['stats']['focus_capacity']}")
    
    print("\n" + "=" * 60)
    print("✅ Attention mechanism working!")
    print("=" * 60)
