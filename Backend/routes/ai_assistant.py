from fastapi import APIRouter, Depends, HTTPException
from models.chat import Conversation, Message
from database.session import get_db
from schemas.chat import MessageCreate, ChatResponse, ConversationCreate
from sqlalchemy.orm import Session
from services.ai_utils import get_ai_response
from auth import get_current_user
import uuid

router = APIRouter()

@router.post("/conversations", response_model=ChatResponse)
def create_conversation(payload: ConversationCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    convo = Conversation(user_id=user.id, title=payload.title)
    db.add(convo)
    db.commit()
    db.refresh(convo)
    return convo

@router.get("/conversations")
def get_user_conversations(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Conversation).filter_by(user_id=user.id).order_by(Conversation.created_at.desc()).all()

@router.get("/conversations/{convo_id}/messages")
def get_messages(convo_id: uuid.UUID, db: Session = Depends(get_db), user=Depends(get_current_user)):
    convo = db.query(Conversation).filter_by(id=convo_id, user_id=user.id).first()
    if not convo:
        raise HTTPException(404, "Conversation not found")
    return db.query(Message).filter_by(conversation_id=convo_id).order_by(Message.created_at).all()

@router.post("/chat", response_model=ChatResponse)
def chat(convo_id: uuid.UUID, msg: MessageCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    convo = db.query(Conversation).filter_by(id=convo_id, user_id=user.id).first()
    if not convo:
        raise HTTPException(404, "Conversation not found")

    user_msg = Message(conversation_id=convo_id, role="user", content=msg.content)
    db.add(user_msg)
    db.commit()

    history = db.query(Message).filter_by(conversation_id=convo_id).order_by(Message.created_at).all()
    history_payload = [{"role": m.role, "content": m.content} for m in history]

    reply = get_ai_response(history_payload)
    bot_msg = Message(conversation_id=convo_id, role="assistant", content=reply)
    db.add(bot_msg)
    db.commit()

    return {"response": reply}