from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from utils.dal import BaseModel
from datetime import datetime

class Message(BaseModel):
    """
    Message model - represents a single message in a conversation
    """
    __tablename__ = "messages"
    
    message_id = Column(Integer, primary_key=True, autoincrement=True)
    conversation_id = Column(Integer, ForeignKey("conversations.conversation_id"), nullable=False)
    role = Column(String(20), nullable=False)  # 'user' or 'assistant'
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    
    # Relationship to conversation
    # conversation = relationship("Conversation", backref="messages")
