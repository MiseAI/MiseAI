
from fastapi import APIRouter
from schemas.forecast import ForecastRequest, ForecastResponse

router = APIRouter()

@router.post("/forecast", response_model=ForecastResponse)
def get_forecast(data: ForecastRequest):
    return ForecastResponse(predicted_sales=data.days * 42.0)
