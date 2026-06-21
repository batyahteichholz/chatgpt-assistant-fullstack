from pydantic import BaseModel

class ChatResponse(BaseModel):
    message: str
    role: str = "assistant"
    conversation_id: int  # ID of the conversation
