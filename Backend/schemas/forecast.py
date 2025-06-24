from pydantic import BaseModel
from typing import List, Dict

class ForecastRequest(BaseModel):
    past_sales: Dict[str, List[int]]  # {"Dish A": [10, 12, 9, 14], ...}

class ForecastResponse(BaseModel):
    forecast: Dict[str, int]  # {"Dish A": 11, ...}
