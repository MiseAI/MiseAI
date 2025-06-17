from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import sales as models, restaurant as restaurant_models
from schemas import sales as schemas
from routers.auth import get_current_user
from models.user import User

router = APIRouter()

@router.post("/", response_model=schemas.Sale)
def create_sale(sale: schemas.SaleCreate, restaurant_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    restaurant = db.query(restaurant_models.Restaurant).filter_by(id=restaurant_id, owner_id=current_user.id).first()
    if not restaurant:
        raise HTTPException(status_code=403, detail="Unauthorized restaurant")
    db_sale = models.Sale(**sale.dict(), user_id=current_user.id, restaurant_id=restaurant_id)
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale

@router.get("/", response_model=list[schemas.Sale])
def read_sales(restaurant_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(models.Sale).filter(models.Sale.user_id == current_user.id, models.Sale.restaurant_id == restaurant_id).all()
