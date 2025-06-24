from fastapi import APIRouter
from schemas.forecast import ForecastRequest, ForecastResponse
from services.forecast import generate_forecast

router = APIRouter(prefix="/forecast", tags=["Forecast"])

@router.post("/", response_model=ForecastResponse)
def forecast(data: ForecastRequest):
    return generate_forecast(data)
