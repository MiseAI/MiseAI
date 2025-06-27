from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ChatHistoryOut(BaseModel):
    id: int
    prompt: str
    response: str
    created_at: datetime
    tags: Optional[str]

    class Config:
        orm_mode = True
