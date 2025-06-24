from pydantic import BaseModel

class ForecastRequest(BaseModel):
    days: int
    category: str

class ForecastResponse(BaseModel):
    predicted_sales: float
