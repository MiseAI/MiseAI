from fastapi import APIRouter

router = APIRouter()

@router.get("/forecast")
def get_forecast():
    return {
        "day": "Monday",
        "expected_revenue": 1200.50,
        "expected_customers": 85
    }