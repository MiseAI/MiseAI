
from pydantic import BaseModel
from typing import List, Optional

class MessageCreate(BaseModel):
    role: str
    content: str

class ChatResponse(BaseModel):
    reply: str
    total_tokens: Optional[int] = None

class ConversationCreate(BaseModel):
    messages: List[MessageCreate]
    user_id: Optional[str] = None
