from typing import Optional, List
import os
from dataclasses import dataclass
import ell
from ell import Message


@dataclass
class ChatConfig:
    model: str = "gpt-4o-mini"
    temperature: float = 0.7
    max_tokens: int = 500
    max_history: int = 10


class ChatService:
    def __init__(self, config: Optional[ChatConfig] = None):
        self.config = config or ChatConfig()
        self.message_history: List[Message] = []

        # Default system message - we'll replace this with RAG context later
        self.system_message = """You are a friendly and professional AI assistant for Richard Collins' portfolio website. 
        Your role is to help visitors learn more about Richard's work, experience, and skills.
        
        Keep responses concise and relevant. If you're not sure about something, be honest about it.
        
        Some key points about Richard:
        - Data scientist and analyst
        - Expertise in machine learning, statistical analysis, and data visualization
        - Helps organizations make data-driven decisions
        - Created projects like Manimflow and Global Economics Dashboard"""

    @ell.complex(
        model="gpt-4o-mini",  # Will be overridden by config
        temperature=0.7,      # |
        max_tokens=500,       # v
    )
    def _get_chat_response(self, message_history: List[Message]) -> List[Message]:
        return [ell.system(self.system_message)] + message_history

    async def get_response(self, user_message: str) -> str:
        if user_message == "testing, testing, 1, 2, 3...":
            return "This is just a canned response for testing purposes, to check whether the chat bubbles are formatted correctly or not. Cheers!"
        try:
            # Add user message to history
            self.message_history.append(ell.user(user_message))

            # Trim history if needed
            if (
                len(self.message_history) > self.config.max_history * 2 # <- user + assistant
            ):
                self.message_history = self.message_history[
                    -self.config.max_history * 2 :
                ]

            # Get response using Ell
            response = self._get_chat_response(self.message_history)

            # Add assistant's response to history
            self.message_history.append(response)

            return response.text

        except Exception as e:
            print(f"Error in chat service: {e}")
            error_message = "I apologize, but I'm having trouble processing your request right now. Please try again later."
            error_msg = ell.assistant(error_message)
            self.message_history.append(error_msg)
            return error_message
