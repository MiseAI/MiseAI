from pydantic import BaseModel
from datetime import datetime

class ChatMessageSchema(BaseModel):
    id: int
    user_id: int
    message: str
    sender: str
    timestamp: datetime

    class Config:
        orm_mode = True
