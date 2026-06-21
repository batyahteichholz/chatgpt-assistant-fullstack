# 🏗️ ארכיטקטורת המערכת / System Architecture

## 📊 תרשים זרימת המערכת

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER BROWSER                             │
│                    http://localhost:5173                         │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           │ React Router
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
    ┌───▼───┐         ┌───▼───┐         ┌───▼───┐
    │ Home  │         │ Chat  │         │ About │
    └───────┘         └───┬───┘         └───────┘
                          │
                          │ ChatService.sendMessage()
                          │
                          ▼
    ┌─────────────────────────────────────────────────┐
    │           FRONTEND (React + TypeScript)          │
    │                                                  │
    │  • ChatPage.tsx - UI Component                  │
    │  • ChatService.ts - API Communication           │
    │  • Models: ChatMessage, ChatRequest             │
    └──────────────────────┬───────────────────────────┘
                           │
                           │ HTTP POST
                           │ http://localhost:4000/api/chat/message
                           │
                           ▼
    ┌─────────────────────────────────────────────────┐
    │           BACKEND (Python FastAPI)               │
    │                                                  │
    │  ┌──────────────────────────────────────────┐  │
    │  │ chat_controller.py                       │  │
    │  │  • Receive request                       │  │
    │  │  • Validate messages                     │  │
    │  │  • Create/Get conversation_id            │  │
    │  └────────┬──────────────┬───────────────────┘  │
    │           │              │                       │
    │           │              │                       │
    │  ┌────────▼────────┐  ┌─▼──────────────────┐   │
    │  │ chat_service.py │  │database_service.py │   │
    │  │                 │  │                    │   │
    │  │ • Send to       │  │• Save user msg     │   │
    │  │   OpenAI API    │  │• Save assistant msg│   │
    │  │ • Get response  │  │• Get conversations │   │
    │  └────────┬────────┘  └─┬──────────────────┘   │
    │           │              │                       │
    └───────────┼──────────────┼───────────────────────┘
                │              │
                │              │ SQLAlchemy ORM
       ┌────────▼──────┐       │
       │  OpenAI API   │       │
       │  ChatGPT      │       │
       │  gpt-4o-mini  │       │
       └───────────────┘       │
                               ▼
                    ┌──────────────────────┐
                    │   MySQL Database     │
                    │                      │
                    │  ┌────────────────┐ │
                    │  │ conversations  │ │
                    │  ├────────────────┤ │
                    │  │conversation_id │ │
                    │  │title           │ │
                    │  │created_at      │ │
                    │  │updated_at      │ │
                    │  └────────────────┘ │
                    │           │         │
                    │           │ 1:N     │
                    │           ▼         │
                    │  ┌────────────────┐ │
                    │  │ messages       │ │
                    │  ├────────────────┤ │
                    │  │message_id      │ │
                    │  │conversation_id │ │
                    │  │role            │ │
                    │  │content         │ │
                    │  │created_at      │ │
                    │  └────────────────┘ │
                    └──────────────────────┘
```

---

## 🔄 תרשים זרימת שיחה / Conversation Flow

### 1️⃣ שיחה חדשה / New Conversation

```
User types message
       │
       ▼
┌──────────────┐
│ "Hello!"     │ User Message
└──────┬───────┘
       │
       ▼
Frontend: Create ChatMessage("user", "Hello!")
       │
       ▼
Frontend: Call chatService.sendMessage([...], conversationId=null)
       │
       ▼
Backend: Receive request with conversation_id=null
       │
       ▼
Backend: Create new conversation → conversation_id = 1
       │
       ▼
Backend: Save user message to DB
       │   INSERT INTO messages (conversation_id=1, role="user", content="Hello!")
       │
       ▼
Backend: Send to OpenAI API
       │   messages: [{"role": "user", "content": "Hello!"}]
       │
       ▼
OpenAI: Returns "Hi! How can I help you?"
       │
       ▼
Backend: Save assistant message to DB
       │   INSERT INTO messages (conversation_id=1, role="assistant", content="Hi! ...")
       │
       ▼
Backend: Return response + conversation_id
       │   { message: "Hi! ...", conversation_id: 1 }
       │
       ▼
Frontend: Update conversationId state = 1
       │
       ▼
Frontend: Display user + assistant messages
```

### 2️⃣ המשך שיחה / Continue Conversation

```
User types "What can you do?"
       │
       ▼
Frontend: messages = [
    {role: "user", content: "Hello!"},
    {role: "assistant", content: "Hi! How can I help?"},
    {role: "user", content: "What can you do?"}
]
       │
       ▼
Frontend: Call chatService.sendMessage(messages, conversationId=1)
       │
       ▼
Backend: Use existing conversation_id=1
       │
       ▼
Backend: Save new user message
       │   INSERT INTO messages (conversation_id=1, role="user", content="What...")
       │
       ▼
Backend: Send FULL message history to OpenAI
       │   (This maintains context!)
       │
       ▼
OpenAI: Returns contextual response
       │
       ▼
Backend: Save assistant response
       │   INSERT INTO messages (conversation_id=1, role="assistant", ...)
       │
       ▼
Frontend: Display updated conversation
```

---

## 📦 מבנה נתונים / Data Structure

### Frontend State (ChatPage)
```typescript
{
  messages: ChatMessage[],        // All messages in current view
  conversationId: number | null,  // Current conversation ID
  inputValue: string,             // User input field
  isLoading: boolean              // Loading state
}
```

### API Request
```json
{
  "messages": [
    {"role": "user", "content": "Hello!"},
    {"role": "assistant", "content": "Hi!"}
  ],
  "conversation_id": 1,
  "model": "gpt-4o-mini",
  "temperature": 0.7
}
```

### API Response
```json
{
  "message": "How can I help you?",
  "role": "assistant",
  "conversation_id": 1
}
```

### Database Record (messages)
```
message_id: 1
conversation_id: 1
role: "user"
content: "Hello!"
created_at: 2026-06-14 10:30:00
```

---

## 🔐 אבטחה / Security

```
.env File (Backend)
├── CONNECTION_STRING → Database credentials
├── OPENAI_API_KEY → Secret API key
└── USE_DEMO_MODE → true/false

.gitignore
├── .env ✅ (Never commit!)
├── env/ ✅ (Virtual environment)
└── node_modules/ ✅ (Dependencies)

Environment Variables Flow:
.env → app_config.py → Services
  ↓
Never exposed to frontend!
```

---

## 📡 תקשורת API / API Communication

### Ports
- **Frontend**: `http://localhost:5173` (Vite)
- **Backend**: `http://localhost:4000` (FastAPI/Uvicorn)
- **Database**: `localhost:3306` (MySQL)

### CORS Configuration
```python
# Backend allows frontend to communicate
server.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production: specific domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 🎯 נתיב קריאה מלא / Full Request Path

```
User clicks "Send"
    ↓
ChatPage.handleSendMessage()
    ↓
chatService.sendMessage()
    ↓
axios.post("http://localhost:4000/api/chat/message")
    ↓
FastAPI router: @router.post("/message")
    ↓
chat_controller.send_chat_message()
    ├─→ database_service.create_conversation() (if new)
    ├─→ database_service.save_message() (user)
    ├─→ chat_service.send_message() → OpenAI API
    └─→ database_service.save_message() (assistant)
    ↓
Return ChatResponse
    ↓
Frontend receives response
    ↓
Update UI with new messages
```

---

**הבנת הארכיטקטורה תעזור לך לתחזק ולהרחיב את הפרויקט בעתיד! 💪**
