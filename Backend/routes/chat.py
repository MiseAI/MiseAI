from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/chat")
async def chat_endpoint(request: Request):
    payload = await request.json()
    message = payload.get("message", "")
    # Simple echo for now. Replace with your real AI logic.
    return {"reply": f"You said: {message}"}