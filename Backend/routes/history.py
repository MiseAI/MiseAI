from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from datetime import datetime

from database.session import get_db
from models.chat import ChatMessage
from schemas.chat import ChatMessageSchema

router = APIRouter()

@router.get("/chat/history", response_model=List[ChatMessageSchema])
def get_chat_history(
    user_id: int,
    query: Optional[str] = None,
    from_date: Optional[datetime] = None,
    to_date: Optional[datetime] = None,
    db: Session = Depends(get_db)
):
    q = db.query(ChatMessage).filter(ChatMessage.user_id == user_id)

    if query:
        q = q.filter(ChatMessage.message.ilike(f"%{query}%"))

    if from_date:
        q = q.filter(ChatMessage.timestamp >= from_date)
    if to_date:
        q = q.filter(ChatMessage.timestamp <= to_date)

    return q.order_by(ChatMessage.timestamp.desc()).all()
