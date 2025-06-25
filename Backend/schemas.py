from pydantic import BaseModel
from uuid import UUID

class ConversationCreate(BaseModel):
    title: str = "New Chat"

class MessageCreate(BaseModel):
    content: str

class ChatResponse(BaseModel):
    response: str