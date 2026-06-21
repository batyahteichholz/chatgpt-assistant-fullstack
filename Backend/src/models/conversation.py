from sqlalchemy import Column, Integer, String, DateTime
from utils.dal import BaseModel
from datetime import datetime

class Conversation(BaseModel):
    """
    Conversation model - represents a chat conversation
    """
    __tablename__ = "conversations"
    
    conversation_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=True)  # Optional conversation title
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
