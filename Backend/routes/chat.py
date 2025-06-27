from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Define the request body model
class ChatRequest(BaseModel):
    message: str

# Define the response model (optional but good practice)
class ChatResponse(BaseModel):
    reply: str

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(payload: ChatRequest):
    # Access the message directly
    message = payload.message
    return ChatResponse(reply=f"You said: {message}")