from typing import Optional
import os
from dataclasses import dataclass
from collections import deque
from openai import AsyncOpenAI


@dataclass
class ChatConfig:
    model: str = "gpt-4o-mini"
    temperature: float = 0.7
    max_tokens: int = 500
    max_history: int = 10


class ChatService:
    def __init__(self, config: Optional[ChatConfig] = None):
        self.config = config or ChatConfig()
        self.client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.message_history = deque(maxlen=self.config.max_history)

        # Default system message - we'll replace this with RAG context later
        self.system_message = """You are a friendly and professional AI assistant for Richard Collins' portfolio website. 
        Your role is to help visitors learn more about Richard's work, experience, and skills.
        
        Keep responses concise and relevant. If you're not sure about something, be honest about it.
        
        Some key points about Richard:
        - Data scientist and analyst
        - Expertise in machine learning, statistical analysis, and data visualization
        - Helps organizations make data-driven decisions
        - Created projects like Manimflow and Global Economics Dashboard"""

    async def get_response(self, user_message: str) -> str:
        if user_message == "testing, testing, 1, 2, 3...":
            return "This is just a canned response for testing purposes, to check whether the chat bubbles are formatted correctly or not. Cheers!"
        else:
            try:
                # Add user message to history
                self.message_history.append({"role": "user", "content": user_message})

                # Construct messages with system message and history
                messages = [{"role": "system", "content": self.system_message}]
                messages.extend(list(self.message_history))

                # Get response from API
                response = await self.client.chat.completions.create(
                    model=self.config.model,
                    messages=messages,
                    temperature=self.config.temperature,
                    max_tokens=self.config.max_tokens,
                )

                # Add assistant's response to history
                assistant_message = response.choices[0].message.content
                self.message_history.append(
                    {"role": "assistant", "content": assistant_message}
                )

                return assistant_message

            except Exception as e:
                print(f"Error in chat service: {e}")
                error_message = "I apologize, but I'm having trouble processing your request right now. Please try again later."
                self.message_history.append(
                    {"role": "assistant", "content": error_message}
                )
                return error_message
