from models.conversation import Conversation
from models.message import Message
from utils.dal import dal
from typing import List, Optional
from datetime import datetime

class DatabaseService:
    """
    Service for managing conversations and messages in the database
    """
    
    def create_conversation(self, title: Optional[str] = None) -> int:
        """
        Create a new conversation
        Returns the conversation_id
        """
        session = dal.create_session()
        try:
            conversation = Conversation(title=title or "New Conversation")
            session.add(conversation)
            session.commit()
            return conversation.conversation_id
        finally:
            session.close()
    
    def save_message(self, conversation_id: int, role: str, content: str) -> int:
        """
        Save a message to the database
        Returns the message_id
        """
        session = dal.create_session()
        try:
            message = Message(
                conversation_id=conversation_id,
                role=role,
                content=content
            )
            session.add(message)
            session.commit()
            
            # Update conversation's updated_at timestamp
            conversation = session.query(Conversation).filter(
                Conversation.conversation_id == conversation_id
            ).first()
            if conversation:
                conversation.updated_at = datetime.now()
                session.commit()
            
            return message.message_id
        finally:
            session.close()
    
    def get_conversation_messages(self, conversation_id: int) -> List[dict]:
        """
        Get all messages for a specific conversation
        Returns list of messages with role and content
        """
        session = dal.create_session()
        try:
            messages = session.query(Message).filter(
                Message.conversation_id == conversation_id
            ).order_by(Message.created_at).all()
            
            return [
                {
                    "message_id": msg.message_id,
                    "role": msg.role,
                    "content": msg.content,
                    "created_at": msg.created_at
                }
                for msg in messages
            ]
        finally:
            session.close()
    
    def get_all_conversations(self) -> List[dict]:
        """
        Get all conversations
        """
        session = dal.create_session()
        try:
            conversations = session.query(Conversation).order_by(
                Conversation.updated_at.desc()
            ).all()
            
            return [
                {
                    "conversation_id": conv.conversation_id,
                    "title": conv.title,
                    "created_at": conv.created_at,
                    "updated_at": conv.updated_at
                }
                for conv in conversations
            ]
        finally:
            session.close()
    
    def delete_conversation(self, conversation_id: int) -> bool:
        """
        Delete a conversation and all its messages
        Returns True if successful
        """
        session = dal.create_session()
        try:
            # Delete all messages first
            session.query(Message).filter(
                Message.conversation_id == conversation_id
            ).delete()
            
            # Delete conversation
            session.query(Conversation).filter(
                Conversation.conversation_id == conversation_id
            ).delete()
            
            session.commit()
            return True
        except:
            session.rollback()
            return False
        finally:
            session.close()


# Create singleton instance
database_service = DatabaseService()
