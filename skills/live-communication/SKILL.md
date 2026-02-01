# Live Communication Skill

**Real-time voice calling and live communication with Harry-001**

## 🎯 What It Does

```
┌─────────────────────────────────────────────────────────────┐
│               LIVE COMMUNICATION SYSTEM                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  📞 INCOMING CALL                                           │
│      │                                                      │
│      ▼                                                      │
│  🎤 Voice Input → Whisper STT → Harry-001 Processing        │
│      │                                                      │
│      ▼                                                      │
│  🧠 Brain Processing → MiniMax Reasoning                    │
│      │                                                      │
│      ▼                                                      │
│  🔊 Voice Output → Voicebox TTS → Response                  │
│      │                                                      │
│      ▼                                                      │
│  💬 Real-time Conversation Flow                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 🛠️ Technologies

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Voice Input** | Whisper (local) | Speech-to-Text |
| **Voice Output** | Voicebox (local) | Text-to-Speech |
| **Real-time API** | OpenAI Realtime API | Low latency |
| **Calling Platform** | Twilio | Phone calls |
| **WebRTC** | Browser-based | Real-time audio |
| **WebSocket** | Socket.io | Live messaging |

## 📞 Use Cases

1. **Voice Call** - Call Harry-001 on phone
2. **Live Chat** - Real-time text + voice conversation
3. **Video Call** - With camera integration
4. **Voice Assistant** - Hands-free interaction
5. **Meeting Assistant** - Join calls, take notes

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  COMMUNICATION LAYER                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │
│  │   Twilio    │  │   WebRTC    │  │  OpenAI     │    │
│  │   (Phone)   │  │  (Browser)  │  │  Realtime   │    │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘    │
│         │                │                │            │
│         └────────────────┼────────────────┘            │
│                          ▼                              │
│                 ┌─────────────────┐                    │
│                 │   Harry-001     │                    │
│                 │   Processing    │                    │
│                 └────────┬────────┘                    │
│                          │                              │
│         ┌────────────────┼────────────────┐            │
│         ▼                ▼                ▼            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐   │
│  │   Whisper   │  │   Brain     │  │  Voicebox   │   │
│  │   (STT)     │  │  (Reason)   │  │   (TTS)     │   │
│  └─────────────┘  └─────────────┘  └─────────────┘   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## 🚀 Implementation

### Option 1: Twilio Voice (Phone Calls)

```javascript
// Twilio integration for phone calls
const twilio = require('twilio');

const twilioClient = twilio(accountSid, authToken);

// Receive incoming call
app.post('/voice', (req, res) => {
    res.twiml(`<Response>
        <Gather input="speech" action="/process-voice">
            <Say>Hi! I'm Harry-001. What can I help you with?</Say>
        </Gather>
    </Response>`);
});

// Process voice input
app.post('/process-voice', async (req, res) => {
    const transcript = req.body.SpeechResult;
    const response = await harry001.process(transcript);
    res.twiml(`<Response><Say>${response}</Say></Response>`);
});
```

### Option 2: OpenAI Realtime API (Web-based)

```javascript
// Real-time voice conversation
const realtime = new OpenAI.Realtime({
    model: 'gpt-4o-realtime',
    voice: 'alloy',
    instructions: 'You are Harry-001, a helpful AI assistant.'
});

await realtime.connect({
    onTranscript: (text) => console.log('User:', text),
    onResponse: (audio) => playAudio(audio)
});
```

### Option 3: WebRTC (Browser-based)

```javascript
// Browser-based voice call
const peerConnection = new RTCPeerConnection(config);

peerConnection.ontrack = (event) => {
    audioElement.srcObject = event.streams[0];
};

navigator.mediaDevices.getUserMedia({ audio: true })
    .then(stream => {
        peerConnection.addTrack(stream, stream);
    });
```

## 📋 Features

| Feature | Status | Description |
|---------|--------|-------------|
| **Voice Input** | ✅ Ready | Whisper (local) |
| **Voice Output** | ✅ Ready | Voicebox (local) |
| **Phone Call** | 🔜 Twilio | Receive calls on phone |
| **Web Call** | 🔜 WebRTC | Browser-based calling |
| **Real-time AI** | 🔜 OpenAI | Low latency processing |
| **Video** | 🔜 Future | Add camera support |

## 🎯 Roadmap

### Phase 1: Voice Chat (This Week)
- [ ] Whisper STT integration
- [ ] Voicebox TTS integration
- [ ] Real-time text chat
- [ ] Basic voice commands

### Phase 2: Phone Calls (Next Week)
- [ ] Twilio account setup
- [ ] Incoming call handling
- [ ] Voice processing pipeline
- [ ] Call recording

### Phase 3: Real-time AI (This Month)
- [ ] OpenAI Realtime API
- [ ] Low latency processing
- [ ] Natural conversation flow
- [ ] Interrupt handling

### Phase 4: Video (Future)
- [ ] Camera integration
- [ ] Video call support
- [ ] Screen sharing
- [ ] Meeting assistant

## 💰 Cost Estimate

| Component | Monthly Cost |
|-----------|-------------|
| Twilio (phone calls) | $1-10/minute |
| OpenAI Realtime API | ~$0.06/minute |
| WebRTC (self-hosted) | Free |
| Local Whisper/Voicebox | Free |

## 🎓 For Harry-001

This skill enables Harry-001 to:
1. **Answer phone calls** - "Harry-001, call me"
2. **Live conversation** - Real-time voice chat
3. **Voice commands** - "Hey Harry, check my stocks"
4. **Meeting assistant** - Join calls, take notes
5. **Accessibility** - Voice-only interaction

## 📁 Files

```
skills/live-communication/
├── SKILL.md           # This file
├── twilio.js          # Phone call handling
├── webrtc.js          # Browser calling
├── openai-realtime.js # Real-time AI
├── audio/             # Audio processing
└── test/              # Test scripts
```

---

**Harry-001: Now with Real-Time Voice Calling! 📞🎤**
