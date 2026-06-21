from openai import OpenAI
from typing import List
from models.chat_message import ChatMessage
from utils.app_config import AppConfig
import random

class ChatService:
    def __init__(self):
        self.use_demo_mode = AppConfig.use_demo_mode
        if not self.use_demo_mode:
            self.client = OpenAI(api_key=AppConfig.openai_api_key)
    
    async def send_message(self, messages: List[ChatMessage], model: str = "gpt-4o-mini", temperature: float = 0.7) -> str:
        """
        Send messages to ChatGPT and get a response
        
        Args:
            messages: List of chat messages (conversation history)
            model: OpenAI model to use (default: gpt-4o-mini)
            temperature: Response creativity (0-1, default: 0.7)
            
        Returns:
            The assistant's response message
        """
        # Demo Mode - Return mock responses
        if self.use_demo_mode:
            return self._get_demo_response(messages)
        
        # Real OpenAI Mode
        try:
            # Convert messages to OpenAI format
            formatted_messages = [
                {"role": msg.role, "content": msg.content}
                for msg in messages
            ]
            
            # Call OpenAI API
            response = self.client.chat.completions.create(
                model=model,
                messages=formatted_messages,  # type: ignore
                temperature=temperature
            )
            
            # Extract and return the assistant's message
            content = response.choices[0].message.content
            return content if content else "Sorry, I couldn't generate a response."
            
        except Exception as e:
            raise Exception(f"Error communicating with OpenAI: {str(e)}")
    
    def _get_demo_response(self, messages: List[ChatMessage]) -> str:
        """Generate a demo response based on user input"""
        last_message = messages[-1].content.lower() if messages else ""
        
        # Smart responses based on keywords
        if "hello" in last_message or "hi" in last_message or "שלום" in last_message:
            return "Hello! 👋 I'm running in Demo Mode. This is a simulated response. How can I help you today?"
        
        elif "joke" in last_message or "בדיחה" in last_message:
            jokes = [
                "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
                "Why did the developer go broke? Because he used up all his cache! 💰",
                "How many programmers does it take to change a light bulb? None, that's a hardware problem! 💡"
            ]
            return random.choice(jokes)
        
        elif "react" in last_message:
            return "React is a JavaScript library for building user interfaces. It uses a component-based architecture and features like hooks (useState, useEffect) make state management easier. Would you like to know more about a specific React topic?"
        
        elif "python" in last_message:
            return "Python is a high-level, interpreted programming language known for its simplicity and readability. It's great for web development, data science, AI, and automation. Is there something specific about Python you'd like to know?"
        
        elif "help" in last_message or "עזרה" in last_message:
            return "I'm currently in Demo Mode, which means I'm not connected to the real ChatGPT API. I can still respond to your messages with pre-programmed responses! Try asking about React, Python, or request a joke. To use the real ChatGPT, add a valid OpenAI API key and set USE_DEMO_MODE=false in the .env file."
        
        elif "?" in last_message:
            return f"That's an interesting question! In Demo Mode, I provide simulated responses. Your question was: '{messages[-1].content}'. To get real AI-powered answers, configure a valid OpenAI API key."
        
        else:
            responses = [
                f"I received your message: '{messages[-1].content}'. I'm in Demo Mode, so this is a simulated response! 🤖",
                f"Thanks for your message! In Demo Mode, I can only provide pre-programmed responses. Try asking about React, Python, or request a joke!",
                f"Interesting! You said: '{messages[-1].content}'. Remember, I'm in Demo Mode - for real AI responses, configure your OpenAI API key."
            ]
            return random.choice(responses)

# Create a singleton instance
chat_service = ChatService()
