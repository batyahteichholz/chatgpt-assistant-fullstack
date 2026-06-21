from pydantic import BaseModel
from typing import List, Optional
from models.chat_message import ChatMessage

class ChatRequest(BaseModel):
    messages: List[ChatMessage]
    conversation_id: Optional[int] = None  # None means create new conversation
    model: str = "gpt-4o-mini"  # Default model
    temperature: float = 0.7
