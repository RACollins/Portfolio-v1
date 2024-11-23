from typing import Optional
import os
from dataclasses import dataclass
from openai import AsyncOpenAI


@dataclass
class ChatConfig:
    model: str = "gpt-4o-mini"
    temperature: float = 0.7
    max_tokens: int = 500


class ChatService:
    def __init__(self, config: Optional[ChatConfig] = None):
        self.config = config or ChatConfig()
        self.client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
                messages = [
                    {"role": "system", "content": self.system_message},
                    {"role": "user", "content": user_message},
                ]

                response = await self.client.chat.completions.create(
                    model=self.config.model,
                    messages=messages,
                    temperature=self.config.temperature,
                    max_tokens=self.config.max_tokens,
                )
                return response.choices[0].message.content

            except Exception as e:
                print(f"Error in chat service: {e}")
                return "I apologize, but I'm having trouble processing your request right now. Please try again later."
