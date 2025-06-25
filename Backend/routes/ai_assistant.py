
from fastapi import APIRouter
from pydantic import BaseModel
from services.ai_utils import get_ai_response

router = APIRouter()

class UserPrompt(BaseModel):
    prompt: str

@router.post("/ai/ask")
async def ask_ai(prompt_input: UserPrompt):
    try:
        result = get_ai_response(prompt_input.prompt)
        return {"response": result}
    except Exception as e:
        return {"error": str(e)}
