from pydantic import BaseModel
from typing import List

class SaleData(BaseModel):
    item: str
    quantity: int
    date: str

class ForecastRequest(BaseModel):
    sales_data: List[SaleData]

class ForecastItem(BaseModel):
    item: str
    predicted_quantity: int

class ForecastResponse(BaseModel):
    forecast: List[ForecastItem]
