from fastapi import APIRouter
from models.chat import Conversation

router = APIRouter()

@router.post("/chat")
async def chat(conv: Conversation):
    return {"reply": ""}