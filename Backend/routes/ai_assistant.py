# FastAPI route with streaming + retries + multi-prompt
from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from services.ai_utils import stream_ai_response

router = APIRouter()

@router.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_id = data.get("user_id")
    org_id = data.get("org_id")
    messages = data.get("messages", [])
    intent = data.get("intent", "general")

    return StreamingResponse(
        stream_ai_response(messages, user_id, org_id, intent),
        media_type="text/event-stream"
    )
