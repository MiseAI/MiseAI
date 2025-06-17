from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.invoice import InvoiceItem
from models.ingredient import Ingredient

router = APIRouter()

@router.get("/cost/alerts")
def get_cost_alerts(db: Session = Depends(get_db)):
    alerts = []
    items = db.query(InvoiceItem).all()
    for item in items:
        if item.matched_ingredient_id:
            ingredient = db.query(Ingredient).filter(Ingredient.id == item.matched_ingredient_id).first()
            if ingredient and ingredient.latest_price:
                difference = item.price - ingredient.latest_price
                pct_diff = (difference / ingredient.latest_price) * 100
                if abs(pct_diff) > 10:
                    alerts.append({
                        "ingredient": ingredient.name,
                        "latest_price": ingredient.latest_price,
                        "invoice_price": item.price,
                        "difference_pct": round(pct_diff, 2),
                        "invoice_id": item.invoice_id
                    })
        else:
            alerts.append({
                "ingredient": item.name,
                "invoice_price": item.price,
                "issue": "Unmatched ingredient",
                "invoice_id": item.invoice_id
            })
    return alerts

@router.get("/cost/summary")
def get_cost_summary(db: Session = Depends(get_db)):
    summary = []
    ingredients = db.query(Ingredient).all()
    for ing in ingredients:
        summary.append({
            "ingredient": ing.name,
            "latest_price": ing.latest_price,
            "unit": ing.unit
        })
    return summary
