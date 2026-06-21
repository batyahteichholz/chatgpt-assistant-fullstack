from fastapi import APIRouter, HTTPException
from models.chat_request import ChatRequest
from models.chat_response import ChatResponse
from services.chat_service import chat_service
from services.database_service import database_service

# Create router
router = APIRouter(prefix="/api/chat", tags=["chat"])

@router.post("/message", response_model=ChatResponse)
async def send_chat_message(request: ChatRequest):
    """
    Send a message to ChatGPT and get a response.
    Supports conversation history for context.
    Saves all messages to database.
    """
    try:
        print(f"📨 Received request: {len(request.messages)} messages")
        
        # Validate that there's at least one message
        if not request.messages or len(request.messages) == 0:
            raise HTTPException(status_code=400, detail="At least one message is required")
        
        # Create new conversation or use existing one
        conversation_id = request.conversation_id
        if conversation_id is None:
            print("🆕 Creating new conversation...")
            conversation_id = database_service.create_conversation()
            print(f"✅ Created conversation ID: {conversation_id}")
        
        # Get the last user message (the new one to save)
        last_user_message = request.messages[-1]
        
        print(f"💾 Saving user message to DB...")
        # Save user message to database
        database_service.save_message(
            conversation_id=conversation_id,
            role=last_user_message.role,
            content=last_user_message.content
        )
        print(f"✅ User message saved")
        
        print(f"🤖 Calling OpenAI API...")
        # Send message to ChatGPT
        response_message = await chat_service.send_message(
            messages=request.messages,
            model=request.model,
            temperature=request.temperature
        )
        print(f"✅ Got response from OpenAI")
        
        print(f"💾 Saving assistant response to DB...")
        # Save assistant response to database
        database_service.save_message(
            conversation_id=conversation_id,
            role="assistant",
            content=response_message
        )
        print(f"✅ Assistant response saved")
        
        # Return the response with conversation_id
        return ChatResponse(
            message=response_message,
            role="assistant",
            conversation_id=conversation_id
        )
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ ERROR: {type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
async def health_check():
    """Check if the chat service is working"""
    return {"status": "ok", "service": "chat"}
