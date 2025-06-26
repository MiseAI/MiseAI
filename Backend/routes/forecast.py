from fastapi import APIRouter

router = APIRouter()

@router.get("/next-week")
async def forecast_next_week():
    return {}
