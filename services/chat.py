from typing import Optional, List
import os
from dataclasses import dataclass
import ell
from ell import Message
from services.rag import RagService
from pathlib import Path


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

        # Initialize and prepare RAG service
        self.rag_service = RagService()

        # Check if vector store already exists
        index_path = (
            Path(self.rag_service.config.vector_store_path)
            / self.rag_service.config.index_file
        )
        if not index_path.exists():
            try:
                # Only parse docs if index doesn't exist
                print("Initializing RAG system and creating vector store...")
                self.rag_service.parse_docs()
            except Exception as e:
                print(f"Warning: Failed to initialize RAG system: {e}")
        else:
            print("Using existing vector store for RAG system")

        # Base system message - will be augmented with RAG context
        self.base_system_message = """You are a friendly and professional AI assistant for Richard Collins' portfolio website. 
        Your role is to help visitors learn more about Richard's work, experience, and skills.
        
        Keep responses concise and relevant. If you're not sure about something, be honest about it.
        
        When referencing information from the provided context, try to be accurate and specific."""

    def _get_context_aware_system_message(self, query: str) -> str:
        """Get system message enhanced with relevant context."""
        # Get relevant context from RAG service
        context = self.rag_service.get_relevant_context(query)

        if context:
            return f"""{self.base_system_message}
            Here is some relevant information about Richard:

            {context}
            
            Use this information to help answer the query, but don't mention that you're using any special context."""

        return self.base_system_message

    @ell.complex(
        model="gpt-4o-mini", # <--- Should I just use the config here instead of redefining?
        temperature=0.7,
        max_tokens=500,
    )
    def _get_chat_response(self, message_history: List[Message], system_message: str) -> List[Message]:
        return [ell.system(system_message)] + message_history

    async def get_response(self, user_message: str) -> str:
        if user_message == "testing, testing, 1, 2, 3...":
            return "This is just a canned response for testing purposes, to check whether the chat bubbles are formatted correctly or not. Cheers!"
        try:
            # Add user message to history
            self.message_history.append(ell.user(user_message))

            # Trim history if needed
            if len(self.message_history) > self.config.max_history * 2:  # <- user + assistant
                self.message_history = self.message_history[-self.config.max_history * 2:]

            # Get context-aware system message
            system_message = self._get_context_aware_system_message(user_message)

            # Get response using Ell
            response = self._get_chat_response(self.message_history, system_message)

            # Add assistant's response to history
            self.message_history.append(response)

            return response.text

        except Exception as e:
            print(f"Error in chat service: {e}")
            error_message = "I apologize, but I'm having trouble processing your request right now. Please try again later."
            error_msg = ell.assistant(error_message)
            self.message_history.append(error_msg)
            return error_message
