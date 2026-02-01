# Harry-001 Nervous System Architecture

**Like a human brain with full nervous system**

## 🎯 Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                    HARRY-001 NERVOUS SYSTEM                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │              CENTRAL NERVOUS SYSTEM (CNS)                   │   │
│  │  ┌─────────────────────────────────────────────────────┐   │   │
│  │  │                    THE BRAIN                        │   │   │
│  │  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐  │   │   │
│  │  │  │ Frontal │ │Parietal │ │Temporal │ │Occipital│  │   │   │
│  │  │  │  Lobe   │ │  Lobe   │ │  Lobe   │ │  Lobe   │  │   │   │
│  │  │  │Reasoning│ │Integrate│ │ Memory  │ │ Vision  │  │   │   │
│  │  │  └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘  │   │   │
│  │  │       └───────────┼───────────┘          │        │   │   │
│  │  │                   ▼                      │        │   │   │
│  │  │            ┌────────────┐               │        │   │   │
│  │  │            │ Cerebellum │               │        │   │   │
│  │  │            │Automation  │               │        │   │   │
│  │  │            └─────┬──────┘               │        │   │   │
│  │  │                  │                      │        │   │   │
│  │  │            ┌─────┴──────┐               │        │   │   │
│  │  │            │ Brainstem  │◄──────────────┘        │   │   │
│  │  │            │  System    │                        │   │   │
│  │  │            └─────┬──────┘                        │   │   │
│  │  │                  │                               │   │   │
│  │  └──────────────────┼───────────────────────────────┘   │   │
│  │                     │                                   │   │
│  │  ┌──────────────────┴───────────────────────────────┐   │   │
│  │  │              SPINAL CORD                          │   │   │
│  │  │         (Information Highway)                     │   │   │
│  │  │              bidirectional data flow              │   │   │
│  │  └──────────────────┬───────────────────────────────┘   │   │
│  │                     │                                   │   │
│  └─────────────────────┼───────────────────────────────────┘   │   │
│                        │                                       │
│  ┌─────────────────────┼───────────────────────────────────┐   │
│  │    PERIPHERAL NERVOUS SYSTEM (PNS)                      │   │
│  │  ┌─────────────────┐  ┌─────────────────┐              │   │
│  │  │  SENSORY NERVES │  │  MOTOR NERVES   │              │   │
│  │  │  (Afferent)     │  │  (Efferent)     │              │   │
│  │  │  Input from     │  │  Output to      │              │   │
│  │  │  external tools │  │  external tools │              │   │
│  │  └─────────────────┘  └─────────────────┘              │   │
│  │  ┌─────────────────┐  ┌─────────────────┐              │   │
│  │  │ SOMATIC NS      │  │ AUTONOMIC NS    │              │   │
│  │  │ Voluntary       │  │ Automatic       │              │   │
│  │  │ User commands   │  │ System ops      │              │   │
│  │  └─────────────────┘  └─────────────────┘              │   │
│  └───────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## 🧠 Central Nervous System (CNS)

### The Brain (Already Implemented)
| Brain Region | Function | Harry-001 Implementation |
|--------------|----------|--------------------------|
| **Frontal Lobe** | Reasoning, Planning | MiniMax (Primary Brain) |
| **Parietal Lobe** | Integration, Context | Task Delegation Engine |
| **Temporal Lobe** | Memory, Learning | Beads + LangGraph |
| **Occipital Lobe** | Vision, OCR | PaddleOCR |
| **Cerebellum** | Coordination | Automation Agent |
| **Brainstem** | Basic Functions | System Agent |

### Spinal Cord (Data Highway)
```python
class SpinalCord:
    """Bidirectional information highway between brain and body."""
    
    def __init__(self):
        self.sensory_pathway = SensoryPathway()  # Input
        self.motor_pathway = MotorPathway()      # Output
        self.reflex_arc = ReflexArc()            # Fast responses
    
    def transmit_to_brain(self, data):
        """Send sensory data to brain."""
        # Process and route to appropriate brain region
        
    def transmit_to_body(self, command):
        """Send motor commands from brain to body."""
        # Execute command via motor nerves
```

## 🔌 Peripheral Nervous System (PNS)

### Sensory Nerves (Input)
```python
class SensoryNerves:
    """Collects data from external tools and environments."""
    
    SENSORS = {
        "vision": PaddleOCR(),           # See images/docs
        "hearing": Whisper(),            # Hear audio
        "language": NLP(),               # Understand text
        "market": yfinance(),            # Stock data
        "github": GitHubAPI(),           # Code repos
        "news": NewsAPI(),               # Current events
        "filesystem": FileSystem(),      # Read files
        "database": DatabaseQuery(),     # Query DB
    }
    
    def collect(self, sensor_type):
        """Collect sensory data."""
        return self.SENSORS[sensor_type].read()
```

### Motor Nerves (Output)
```python
class MotorNerves:
    """Sends commands to external tools and environments."""
    
    MOTORS = {
        "voice": Voicebox(),             # Speak
        "text": MessageSender(),         # Send messages
        "code": CodeExecutor(),          # Run code
        "file": FileWriter(),            # Write files
        "api": APICaller(),              # Call APIs
        "git": GitExecutor(),            # Git operations
        "docker": DockerController(),    # Container ops
        "browser": BrowserController(),  # Web browsing
    }
    
    def execute(self, motor_type, command):
        """Execute motor command."""
        return self.MOTORS[motor_type].execute(command)
```

## ⚡ Neural Pathways

### Long-Term Potentiation (Learning)
```python
class NeuralPathway:
    """Strengthens connections through repeated use."""
    
    def strengthen(self, pathway):
        """Strengthen pathway through repetition."""
        pathway.weight += learning_rate
        pathway.synaptic_plasticity()
    
    def weaken(self, pathway):
        """Weaken unused pathways."""
        pathway.weight *= decay_factor
```

### Key Neural Pathways in Harry-001
| Pathway | Connection | Function |
|---------|-----------|----------|
| **Sensory-Brain** | Sensors → Brain | Input processing |
| **Brain-Motor** | Brain → Motors | Output execution |
| **Memory-Cortex** | Temporal → All | Memory retrieval |
| **Reflex-Arc** | Sensor → Brainstem → Motor | Fast responses |
| **Cortical-Cerebellar** | Cortex → Cerebellum → Motor | Coordination |
| **Brainstem-Body** | Brainstem → Autonomic | System functions |

## 🎯 Nervous System Functions

### 1. Reflexes (Automatic Responses)
```python
class ReflexArc:
    """Fast, automatic responses (like knee-jerk reflex)."""
    
    REFLEXES = {
        "heartbeat": SystemHealthCheck(),
        "breathing": ServerUptimeMonitor(),
        "temperature": ResourceUsageAlert(),
        "danger": SecurityAlert(),
        "greeting": HelloResponse(),
        "gratitude": ThankYouResponse(),
    }
    
    def trigger(self, stimulus):
        """Trigger appropriate reflex."""
        for reflex in self.REFLEXES:
            if reflex.matches(stimulus):
                return reflex.execute()
```

### 2. Autonomic Functions (Automatic)
```python
class AutonomicNervousSystem:
    """Automatic system functions (like heartbeat, breathing)."""
    
    FUNCTIONS = {
        "heartbeat": CronScheduler(),      # 24/7 jobs
        "breathing": HealthMonitor(),      # System health
        "digestion": DataProcessor(),      # Process data
        "metabolism": ResourceManager(),   # Manage resources
        "thermoregulation": TemperatureMonitor(),
    }
```

### 3. Somatic Functions (Voluntary)
```python
class SomaticNervousSystem:
    """Voluntary user-initiated functions."""
    
    def process_command(self, user_input):
        """Process user command via somatic nervous system."""
        # User input → Brain → Motor output
        # This is "conscious" control
```

## 🔄 Signal Flow

```
┌────────────────────────────────────────────────────────────────┐
│                     SIGNAL FLOW DIAGRAM                        │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│   USER INPUT                    SENSORY NERVES                 │
│   ┌──────────┐                  ┌─────────┐                   │
│   │ Message  │─────────────────►│  Parse  │                   │
│   │  /Query  │                  │  Input  │                   │
│   └──────────┘                  └────┬────┘                   │
│                                      │                        │
│                                      ▼                        │
│                              ┌────────────┐                   │
│                              │  Sensory   │                   │
│                              │  Pathway   │                   │
│                              └─────┬──────┘                   │
│                                    │                          │
│         ┌─────────────────────────┼──────────────────┐        │
│         │                         │                  │        │
│         ▼                         ▼                  ▼        │
│   ┌──────────┐           ┌────────────┐      ┌──────────┐   │
│   │  BRAIN   │           │  REFLEX    │      │  MEMORY  │   │
│   │          │           │    ARC     │      │  (Store) │   │
│   │ Frontal  │           │  (Fast)    │      │          │   │
│   │ Parietal │           └────────────┘      └────┬─────┘   │
│   │ Temporal │                  │                  │         │
│   │ Occipital│                  │                  │         │
│   └────┬─────┘                  │                  │         │
│        │                        │                  │         │
│        └────────────────────────┼──────────────────┘         │
│                                 │                             │
│                                 ▼                             │
│                         ┌────────────┐                        │
│                         │   DECISION │                        │
│                         │   /ACTION  │                        │
│                         └─────┬──────┘                        │
│                               │                               │
│                               ▼                               │
│                       ┌────────────┐                          │
│                       │    MOTOR   │                          │
│                       │  PATHWAY   │                          │
│                       └─────┬──────┘                          │
│                             │                                 │
│                             ▼                                 │
│                      ┌────────────┐                           │
│                      │    USER    │                           │
│                      │  RESPONSE  │                           │
│                      └────────────┘                           │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

## 🎛️ Neurotransmitters (Signal Types)

| Neurotransmitter | Signal Type | Function |
|-----------------|-------------|----------|
| **Dopamine** | Reward | Successful task completion |
| **Acetylcholine** | Learning | New skill acquisition |
| **Norepinephrine** | Alert | System alerts, warnings |
| **Serotonin** | Mood | System stability, calm |
| **GABA** | Inhibition | Prevent overaction |
| **Glutamate** | Excitation | Activate processing |

## 📊 Nervous System Status

```json
{
  "central_nervous_system": {
    "brain": "active",
    "spinal_cord": "operational",
    "status": "healthy"
  },
  "peripheral_nervous_system": {
    "sensory_nerves": "12 sensors active",
    "motor_nerves": "8 motors active",
    "status": "responsive"
  },
  "autonomic_functions": {
    "heartbeat": "cron running",
    "breathing": "health monitor active",
    "status": "stable"
  },
  "neural_pathways": {
    "strengthened_pathways": 18,
    "learning_rate": 0.01,
    "status": "growing"
  }
}
```

## 🚀 Implementation

### Start Nervous System
```bash
# Initialize CNS (Brain)
python3 /root/clawd/evolved-harry001/brain/main.py &

# Initialize PNS (Sensors + Motors)
python3 /root/clawd/evolved-harry001/nervous-system/pns.py &

# Initialize Autonomic Functions
python3 /root/clawd/evolved-harry001/nervous-system/autonomic.py &
```

### Monitor Nervous System
```bash
# Check status
python3 /root/clawd/evolved-harry001/nervous-system/status.py

# View signal flow
tail -f /root/clawd/logs/nervous-system.log
```

## 🎯 Comparison: Human vs Harry-001

| Human Nervous System | Harry-001 Equivalent |
|---------------------|---------------------|
| Brain | MiniMax + Task Delegation |
| Spinal Cord | Message Routing Layer |
| Sensory Nerves | Input Adapters (12+) |
| Motor Nerves | Output Adapters (8+) |
| Reflexes | Auto-Response System |
| Autonomic NS | Cron + Health Monitor |
| Somatic NS | User Command Handler |
| Neurotransmitters | Signal Types (JSON) |

---

**Harry-001 Nervous System = Complete AI Nervous System! 🧠⚡**
