from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from services.ai_utils import get_chat_response

router = APIRouter()

class Message(BaseModel):
    role: str
    content: str

class Conversation(BaseModel):
    messages: List[Message]

@router.post("/chat")
async def chat(conv: Conversation):
    try:
        reply = get_chat_response(conv.messages)
        return {"reply": reply}
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=500, detail="Internal AI chat error")
