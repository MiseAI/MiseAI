from fastapi import APIRouter

router = APIRouter()

@router.get("/invoice")
def get_invoice():
    return {"message": "invoice works!"}
