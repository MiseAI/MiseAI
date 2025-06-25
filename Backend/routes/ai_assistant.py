from fastapi import APIRouter
from services.ai_utils import get_ai_response

router = APIRouter()

@router.get("/ai")
def query_ai(prompt: str):
    return {"response": get_ai_response(prompt)}
