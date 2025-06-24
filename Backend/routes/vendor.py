
from fastapi import APIRouter
from services.vendor_analyzer import VendorAnalyzer
from schemas.vendor import VendorSuggestionRequest

router = APIRouter()

@router.post("/vendors/suggestions")
def get_suggestions(req: VendorSuggestionRequest):
    analyzer = VendorAnalyzer()
    return analyzer.suggest_vendors(req)

@router.get("/vendors/items/{item_name}/history")
def get_price_history(item_name: str):
    analyzer = VendorAnalyzer()
    return analyzer.get_price_history(item_name)
