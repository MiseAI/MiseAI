from fastapi import APIRouter, HTTPException, Request
from services.openai_service import ask_assistant

router = APIRouter()

@router.post("/ask")
async def get_response(request: Request):
    try:
        body = await request.json()
        query = body.get("message", "")
        if not query:
            raise HTTPException(status_code=400, detail="No message provided.")
        response = ask_assistant(query)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))