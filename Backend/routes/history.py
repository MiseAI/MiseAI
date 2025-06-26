from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List, Optional
from database import get_db
from models import ChatHistory
from auth import get_current_user
from schemas import ChatHistoryOut

router = APIRouter(prefix="/api/history", tags=["Chat History"])

@router.get("/", response_model=List[ChatHistoryOut])
def get_user_history(
    q: Optional[str] = None,
    from_date: Optional[datetime] = None,
    to_date: Optional[datetime] = None,
    tag: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    query = db.query(ChatHistory).filter(ChatHistory.user_id == current_user["id"])

    if q:
        query = query.filter(ChatHistory.prompt.ilike(f"%{q}%") | ChatHistory.response.ilike(f"%{q}%"))
    if from_date:
        query = query.filter(ChatHistory.created_at >= from_date)
    if to_date:
        query = query.filter(ChatHistory.created_at <= to_date)
    if tag:
        query = query.filter(ChatHistory.tags.ilike(f"%{tag}%"))

    return query.order_by(ChatHistory.created_at.desc()).all()
