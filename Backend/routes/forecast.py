from fastapi import APIRouter
from services.forecast_engine import ForecastEngine
from schemas.forecast import ForecastRequest, ForecastResponse

router = APIRouter()

@router.post("/forecast", response_model=ForecastResponse)
def forecast_items(data: ForecastRequest):
    engine = ForecastEngine()
    return engine.predict(data)
