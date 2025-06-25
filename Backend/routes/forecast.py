from fastapi import APIRouter

router = APIRouter()

@router.get("/forecast")
def get_forecast():
    return {"message": "forecast works!"}
