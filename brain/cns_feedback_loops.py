#!/usr/bin/env python3
"""
Harry-001 CNS Feedback Loop System
仿照中樞神經系統 (CNS) 的反饋機制
Inspired by Central Nervous System feedback loops

Created: 2026-02-07

CNS Components:
- 脊髓 (Spinal Cord) = Data Highway
- 感覺神經 (Sensory) = Input
- 運動神經 (Motor) = Output
- 反射弧 (Reflex Arc) = Fast response
"""

import time
from dataclasses import dataclass, field
from typing import List, Dict, Callable, Any, Optional
from enum import Enum


class SignalType(Enum):
    """信號類型"""
    SENSORY = "sensory"      # 感覺輸入
    MOTOR = "motor"          # 運動輸出
    INTERNEURON = "inter"    # 中間神經元 (處理)
    REFLEX = "reflex"        # 反射
    FEEDBACK = "feedback"    # 負反饋


@dataclass
class NeuralSignal:
    """神經信號"""
    id: str
    source: str
    target: str
    signal_type: SignalType
    payload: Any
    timestamp: float = field(default_factory=time.time)
    strength: float = 1.0  # 信號強度
    latency_ms: float = 0.0  # 延遲
    processed: bool = False


@dataclass
class ReflexArc:
    """反射弧 - 快速響應"""
    name: str
    stimulus: str
    response: Callable
    threshold: float = 0.5
    cooldown_ms: int = 100


class SensoryNerve:
    """
    感覺神經 - 輸入通道
    仿照: 視覺、聽覺、觸覺等感覺受體
    """
    
    def __init__(self, name: str, sensitivity: float = 1.0):
        self.name = name
        self.sensitivity = sensitivity
        self.threshold = 0.3
        self.readings: List[Dict] = []
        
    def detect(self, stimulus: Any) -> Optional[NeuralSignal]:
        """檢測刺激"""
        intensity = self._measure_intensity(stimulus)
        
        if intensity >= self.threshold:
            signal = NeuralSignal(
                id=f"sensory_{self.name}_{int(time.time()*1000)}",
                source=self.name,
                target="spinal_cord",
                signal_type=SignalType.SENSORY,
                payload={
                    'stimulus': stimulus,
                    'intensity': intensity * self.sensitivity
                },
                strength=intensity * self.sensitivity
            )
            self.readings.append({
                'time': time.time(),
                'stimulus': stimulus,
                'intensity': intensity
            })
            return signal
        return None
    
    def _measure_intensity(self, stimulus: Any) -> float:
        """測量刺激強度"""
        if isinstance(stimulus, (int, float)):
            return min(1.0, abs(stimulus) / 100)
        elif isinstance(stimulus, str):
            urgency_words = ['urgent', '🔥', '⚡', '!', 'important']
            return min(1.0, sum(1 for w in urgency_words if w in stimulus) / 3)
        return 0.5


class MotorNerve:
    """
    運動神經 - 輸出通道
    仿照: 運動神經元控制肌肉
    """
    
    def __init__(self, name: str):
        self.name = name
        self.command_queue: List[NeuralSignal] = []
        self.execution_history: List[Dict] = []
        self.active = True
        
    def execute(self, command: str, strength: float = 1.0) -> bool:
        """執行運動命令"""
        if not self.active:
            return False
            
        signal = NeuralSignal(
            id=f"motor_{self.name}_{int(time.time()*1000)}",
            source="brain",
            target=self.name,
            signal_type=SignalType.MOTOR,
            payload=command,
            strength=strength
        )
        
        self.command_queue.append(signal)
        
        # 記錄執行
        self.execution_history.append({
            'time': time.time(),
            'command': command,
            'strength': strength
        })
        
        return True
    
    def get_next_command(self) -> Optional[NeuralSignal]:
        """獲取下一個命令"""
        if self.command_queue:
            return self.command_queue.pop(0)
        return None


class SpinalCord:
    """
    脊髓 - 中樞數據通道
    仿照: 感覺和運動信號的高速公路
    """
    
    def __init__(self):
        self.sensory_pathway: List[NeuralSignal] = []
        self.motor_pathway: List[NeuralSignal] = []
        self.interneuron_network: Dict[str, List[Callable]] = {}
        self.latency_sensory_ms = 5.0  # 感覺延遲
        self.latency_motor_ms = 8.0    # 運動延遲
        
    def transmit_sensory(self, signal: NeuralSignal) -> NeuralSignal:
        """傳輸感覺信號到大腦"""
        signal.latency_ms = self.latency_sensory_ms
        self.sensory_pathway.append(signal)
        return signal
    
    def transmit_motor(self, signal: NeuralSignal) -> NeuralSignal:
        """傳輸運動信號到效應器"""
        signal.latency_ms = self.latency_motor_ms
        self.motor_pathway.append(signal)
        return signal
    
    def register_interneuron(self, trigger: str, handler: Callable):
        """註冊中間神經元處理器"""
        if trigger not in self.interneuron_network:
            self.interneuron_network[trigger] = []
        self.interneuron_network[trigger].append(handler)


class ReflexArcController:
    """
    反射弧控制器 - 快速響應系統
    仿照: 不經大腦的快速反射
    """
    
    def __init__(self, spinal_cord: SpinalCord):
        self.spinal_cord = spinal_cord
        self.reflexes: Dict[str, ReflexArc] = {}
        self.last_reflex_time: Dict[str, float] = {}
        
    def add_reflex(self, name: str, stimulus: str, 
                   response: Callable, threshold: float = 0.5):
        """添加反射弧"""
        self.reflexes[name] = ReflexArc(
            name=name,
            stimulus=stimulus,
            response=response,
            threshold=threshold
        )
        
    def trigger(self, sensory_signal: NeuralSignal) -> Optional[NeuralSignal]:
        """觸發反射"""
        for reflex in self.reflexes.values():
            if self._matches(sensory_signal, reflex):
                # 檢查冷卻
                now = time.time() * 1000
                last = self.last_reflex_time.get(reflex.name, 0)
                if now - last < reflex.cooldown_ms:
                    continue
                    
                self.last_reflex_time[reflex.name] = now
                
                # 執行反射響應
                result = reflex.response(sensory_signal)
                
                # 創建反射信號
                reflex_signal = NeuralSignal(
                    id=f"reflex_{reflex.name}_{int(now)}",
                    source=reflex.stimulus,
                    target="effector",
                    signal_type=SignalType.REFLEX,
                    payload=result,
                    strength=1.0,
                    latency_ms=1.0  # 非常快！
                )
                
                return reflex_signal
        return None
    
    def _matches(self, signal: NeuralSignal, reflex: ReflexArc) -> bool:
        """檢查信號是否匹配反射觸發"""
        payload_str = str(signal.payload)
        return reflex.stimulus.lower() in payload_str.lower()


class FeedbackLoop:
    """
    負反饋迴路 - 維持穩態
    仿照: 體溫調節、血壓調節等負反饋系統
    """
    
    def __init__(self, name: str, setpoint: float, 
                 sensor_range: tuple, correction_rate: float = 0.5):
        self.name = name
        self.setpoint = setpoint
        self.current_value = setpoint
        self.sensor_min, self.sensor_max = sensor_range
        self.correction_rate = correction_rate
        self.history: List[Dict] = []
        
    def read_sensor(self) -> float:
        """讀取傳感器 (模擬)"""
        noise = (time.time() % 1) * 0.1 - 0.05
        return max(self.sensor_min, min(self.sensor_max, self.current_value + noise))
    
    def correct(self) -> Dict:
        """執行負反饋校正"""
        current = self.read_sensor()
        error = self.setpoint - current
        
        if abs(error) < 0.01:
            return {'status': 'stable', 'error': error}
        
        # 校正量
        correction = error * self.correction_rate
        self.current_value += correction
        
        # 記錄
        self.history.append({
            'time': time.time(),
            'current': current,
            'correction': correction,
            'error': error
        })
        
        direction = "↑" if correction > 0 else "↓"
        
        return {
            'status': 'correcting',
            'error': error,
            'correction': correction,
            'direction': direction,
            'new_value': self.current_value
        }


class CNS:
    """
    中樞神經系統 (CNS) 整合
    仿照完整的神經系統架構
    
    數據流:
    Sensory → Spinal Cord → Brain → Spinal Cord → Motor → Effectors
                     ↓                    ↑
                  Reflex Arc         Feedback Loop
    """
    
    def __init__(self):
        # 組件
        self.sensory_nerves: Dict[str, SensoryNerve] = {}
        self.motor_nerves: Dict[str, MotorNerve] = {}
        self.spinal_cord = SpinalCord()
        self.reflex_controller = ReflexArcController(self.spinal_cord)
        self.feedback_loops: Dict[str, FeedbackLoop] = {}
        
        # 統計
        self.stats = {
            'sensory_signals': 0,
            'motor_signals': 0,
            'reflexes_triggered': 0,
            'feedback_corrections': 0
        }
        
        # 初始化默認反射
        self._setup_default_reflexes()
        
    def _setup_default_reflexes(self):
        """設置默認反射弧"""
        def emergency_response(signal):
            return "EMERGENCY_ACK"
            
        def error_response(signal):
            return "ERROR_LOGGED"
            
        self.reflex_controller.add_reflex(
            "emergency", "urgent", emergency_response, threshold=0.6
        )
        self.reflex_controller.add_reflex(
            "error", "error", error_response, threshold=0.5
        )
        
    def add_sensory_nerve(self, name: str, sensitivity: float = 1.0):
        """添加感覺神經"""
        self.sensory_nerves[name] = SensoryNerve(name, sensitivity)
        
    def add_motor_nerve(self, name: str):
        """添加運動神經"""
        self.motor_nerves[name] = MotorNerve(name)
        
    def add_feedback_loop(self, name: str, setpoint: float,
                          min_val: float, max_val: float):
        """添加負反饋迴路"""
        self.feedback_loops[name] = FeedbackLoop(
            name, setpoint, (min_val, max_val)
        )
        
    def process_input(self, nerve_name: str, stimulus: Any) -> Dict:
        """處理輸入 (感覺 → 脊髓 → 大腦/反射)"""
        if nerve_name not in self.sensory_nerves:
            return {'error': f'Unknown nerve: {nerve_name}'}
            
        nerve = self.sensory_nerves[nerve_name]
        
        # 1. 感覺檢測
        signal = nerve.detect(stimulus)
        if not signal:
            return {'status': 'below_threshold', 'stimulus': stimulus}
            
        self.stats['sensory_signals'] += 1
        
        # 2. 脊髓傳輸
        self.spinal_cord.transmit_sensory(signal)
        
        # 3. 反射檢查 (並行於大腦處理)
        reflex_response = self.reflex_controller.trigger(signal)
        
        result = {
            'status': 'processed',
            'sensory_signal_id': signal.id,
            'intensity': signal.strength,
            'reflex_triggered': reflex_response is not None,
            'reflex_response': reflex_response.payload if reflex_response else None
        }
        
        if reflex_response:
            self.stats['reflexes_triggered'] += 1
            # 反射直接執行
            for motor in self.motor_nerves.values():
                motor.execute(reflex_response.payload, reflex_response.strength)
            self.stats['motor_signals'] += 1
            
        return result
    
    def send_command(self, nerve_name: str, command: str, 
                     strength: float = 1.0) -> bool:
        """發送運動命令 (大腦 → 脊髓 → 運動)"""
        if nerve_name not in self.motor_nerves:
            return False
            
        success = self.motor_nerves[nerve_name].execute(command, strength)
        if success:
            self.stats['motor_signals'] += 1
        return success
    
    def run_feedback_cycles(self) -> Dict:
        """運行所有負反饋迴路"""
        corrections = {}
        for name, loop in self.feedback_loops.items():
            result = loop.correct()
            if result['status'] == 'correcting':
                self.stats['feedback_corrections'] += 1
            corrections[name] = result
        return corrections
    
    def get_stats(self) -> Dict:
        """獲取統計"""
        return {
            **self.stats,
            'sensory_nerves': len(self.sensory_nerves),
            'motor_nerves': len(self.motor_nerves),
            'feedback_loops': len(self.feedback_loops),
            'active_reflexes': len(self.reflex_controller.reflexes)
        }


# ============================================
# 使用示例
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("🔗 CNS FEEDBACK LOOP SYSTEM")
    print("=" * 60)
    
    # 初始化 CNS
    cns = CNS()
    
    # 添加感覺神經
    cns.add_sensory_nerve("vision", sensitivity=1.0)
    cns.add_sensory_nerve("text_input", sensitivity=1.2)
    cns.add_sensory_nerve("system_monitor", sensitivity=0.8)
    
    # 添加運動神經
    cns.add_motor_nerve("response_generator")
    cns.add_motor_nerve("action_executor")
    cns.add_motor_nerve("logger")
    
    # 添加負反饋迴路
    cns.add_feedback_loop("response_quality", setpoint=0.8, min_val=0.0, max_val=1.0)
    cns.add_feedback_loop("load_balance", setpoint=0.5, min_val=0.0, max_val=1.0)
    
    print("\n🧠 CNS Initialized:")
    print(f"   • Sensory nerves: {len(cns.sensory_nerves)}")
    print(f"   • Motor nerves: {len(cns.motor_nerves)}")
    print(f"   • Feedback loops: {len(cns.feedback_loops)}")
    
    # 測試感覺輸入
    print("\n📥 Testing sensory inputs...")
    
    test_inputs = [
        ("text_input", "Normal message"),
        ("text_input", "🔥 URGENT: System alert!"),
        ("text_input", "Check the error log"),
        ("system_monitor", "CPU at 45%"),
        ("text_input", "Another normal message"),
    ]
    
    for nerve, inp in test_inputs:
        result = cns.process_input(nerve, inp)
        print(f"   [{nerve}] '{inp[:30]}...' → {result['status']}")
        if result.get('reflex_triggered'):
            print(f"      ⚡ REFLEX: {result['reflex_response']}")
    
    # 測試運動命令
    print("\n📤 Testing motor commands...")
    cns.send_command("response_generator", "Analyze request")
    cns.send_command("action_executor", "Execute task")
    cns.send_command("logger", "Log event")
    
    # 運行負反饋
    print("\n🔄 Running feedback loops...")
    corrections = cns.run_feedback_cycles()
    
    for name, result in corrections.items():
        if result['status'] == 'correcting':
            print(f"   [{name}] {result['direction']} Correction: {result['correction']:.4f}")
        else:
            print(f"   [{name}] ✓ Stable at setpoint")
    
    # 統計
    print("\n📊 CNS Statistics:")
    stats = cns.get_stats()
    for key, value in stats.items():
        print(f"   • {key}: {value}")
    
    print("\n" + "=" * 60)
    print("✅ CNS Feedback Loop System working!")
    print("=" * 60)
