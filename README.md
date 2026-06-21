# ChatGPT Assistant - Full Stack Project

## 📋 תיאור הפרויקט / Project Description

**עברית:**  
פרויקט Full Stack המיישם מערכת ChatGPT המאפשרת למשתמשים לנהל שיחות מתמשכות עם בינה מלאכותית. השיחות נשמרות במסד נתונים MySQL ומאפשרות המשכיות מלאה של השיחה עם שמירת ההקשר.

**English:**  
A Full Stack project implementing a ChatGPT system that allows users to manage continuous conversations with AI. Conversations are saved to a MySQL database and support full conversation continuity with context preservation.

---

## 🛠️ טכנולוגיות / Technologies

### Frontend
- **React 18** - Library for building user interfaces
- **TypeScript** - Type-safe JavaScript
- **Vite** - Fast build tool and development server
- **React Router** - Client-side routing
- **Axios** - HTTP client for API calls

### Backend
- **Python** - Programming language
- **FastAPI** - Modern, fast web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **OpenAI API** - ChatGPT integration
- **Uvicorn** - ASGI server

### Database
- **MySQL** - Relational database management system
- Tables: `conversations`, `messages`

---

## 📂 מבנה הפרויקט / Project Structure

```
├── Backend/
│   ├── src/
│   │   ├── app.py                    # Main FastAPI application
│   │   ├── controllers/              # API controllers
│   │   │   └── chat_controller.py
│   │   ├── models/                   # Data models (Pydantic & SQLAlchemy)
│   │   │   ├── chat_message.py
│   │   │   ├── chat_request.py
│   │   │   ├── chat_response.py
│   │   │   ├── conversation.py
│   │   │   └── message.py
│   │   ├── services/                 # Business logic
│   │   │   ├── chat_service.py
│   │   │   └── database_service.py
│   │   ├── utils/                    # Utilities
│   │   │   ├── app_config.py
│   │   │   └── dal.py
│   │   └── middleware/               # Middleware
│   ├── .env                          # Environment variables (NOT in Git)
│   └── requirements.txt              # Python dependencies
│
├── Frontend/
│   ├── src/
│   │   ├── Components/
│   │   │   ├── LayoutArea/
│   │   │   │   ├── Header/
│   │   │   │   ├── Menu/
│   │   │   │   ├── Routing/
│   │   │   │   └── Layout/
│   │   │   └── PagesArea/
│   │   │       ├── ChatPage/
│   │   │       ├── About/
│   │   │       └── Page404/
│   │   ├── Models/                   # TypeScript models
│   │   ├── Services/                 # API services
│   │   └── Utils/                    # Utilities
│   ├── package.json                  # Node dependencies
│   └── vite.config.ts
│
└── Database/
    └── schema.sql                    # Database schema export
```

---

## 🚀 התקנה והרצה / Installation & Running

### Prerequisites
- **Python 3.10+**
- **Node.js 18+**
- **MySQL Server**

### 1️⃣ Database Setup

```bash
# Create database
mysql -u root -p
CREATE DATABASE chatgpt_assistant;
EXIT;

# Import schema
mysql -u root -p chatgpt_assistant < Database/schema.sql
```

### 2️⃣ Backend Setup

```bash
cd Backend

# Create virtual environment
python -m venv env

# Activate virtual environment
# Windows:
env\Scripts\activate
# Mac/Linux:
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with your configuration
# See .env.example for required variables

# Run the server
cd src
python app.py
```

The backend server will start on `http://localhost:4000`

### 3️⃣ Frontend Setup

```bash
cd Frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

The frontend will start on `http://localhost:5173`

---

## 🔑 Environment Variables

Create a `.env` file in the `Backend` folder:

```env
CONNECTION_STRING=mysql+mysqlconnector://root:YOUR_PASSWORD@localhost/chatgpt_assistant
OPENAI_API_KEY=your_openai_api_key_here
USE_DEMO_MODE=FALSE
```

> ⚠️ **Important:** Never commit the `.env` file to Git! It's already in `.gitignore`.

---

## ✨ תכונות / Features

- 💬 **Continuous Conversations** - Chat with full context preservation
- 💾 **Database Storage** - All conversations and messages saved to MySQL
- 🔄 **New Chat** - Start fresh conversations anytime
- 🎨 **Modern UI** - Beautiful, responsive interface
- ⚡ **Fast Responses** - Optimized API calls
- 🔒 **Secure** - API keys stored securely in environment variables
- 📱 **Responsive** - Works on desktop and mobile devices

---

## 🗄️ מבנה מסד הנתונים / Database Schema

### `conversations` Table
| Column | Type | Description |
|--------|------|-------------|
| conversation_id | INT (PK) | Unique conversation identifier |
| title | VARCHAR(200) | Conversation title |
| created_at | DATETIME | Creation timestamp |
| updated_at | DATETIME | Last update timestamp |

### `messages` Table
| Column | Type | Description |
|--------|------|-------------|
| message_id | INT (PK) | Unique message identifier |
| conversation_id | INT (FK) | Reference to conversation |
| role | VARCHAR(20) | 'user' or 'assistant' |
| content | TEXT | Message content |
| created_at | DATETIME | Creation timestamp |

---

## 📝 API Documentation

### POST `/api/chat/message`
Send a message to ChatGPT.

**Request:**
```json
{
  "messages": [
    { "role": "user", "content": "Hello!" }
  ],
  "conversation_id": null,
  "model": "gpt-4o-mini",
  "temperature": 0.7
}
```

**Response:**
```json
{
  "message": "Hello! How can I help you today?",
  "role": "assistant",
  "conversation_id": 1
}
```

### GET `/api/chat/health`
Check API health status.

---

## 🔗 קישורים / Links

- **GitHub Repository:** [הוסף קישור כאן / Add link here]
- **OpenAI API:** https://platform.openai.com/
- **FastAPI Documentation:** https://fastapi.tiangolo.com/
- **React Documentation:** https://react.dev/

---

## 👨‍💻 מפתח / Developer

**Name:** [Your Name]  
**Email:** [your.email@example.com]  
**GitHub:** [github.com/yourusername]

---

## 📄 License

This project is created for educational purposes as part of a Full Stack Web Development course.

---

## 🙏 תודות / Acknowledgments

- OpenAI for the ChatGPT API
- FastAPI framework
- React community
- All open-source contributors

---

**Built with ❤️ using Python, React, and MySQL**


## GitHub Repository

https://github.com/batyahteichholz/chatgpt-assistant-fullstack


