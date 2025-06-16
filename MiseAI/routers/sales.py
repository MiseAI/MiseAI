from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import sales as models
from schemas import sales as schemas

router = APIRouter()

@router.post("/", response_model=schemas.Sale)
def create_sale(sale: schemas.SaleCreate, db: Session = Depends(get_db)):
    db_sale = models.Sale(**sale.dict())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale

@router.get("/", response_model=list[schemas.Sale])
def read_sales(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Sale).offset(skip).limit(limit).all()
