
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Message(BaseModel):
    role: str  # "user" or "assistant"
    content: str
    timestamp: Optional[datetime] = None

class Conversation(BaseModel):
    messages: List[Message]
    user_id: Optional[str] = None
