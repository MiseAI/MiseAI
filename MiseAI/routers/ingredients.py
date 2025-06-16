from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import ingredient as models
from schemas import ingredient as schemas

router = APIRouter()

@router.post("/", response_model=schemas.Ingredient)
def create_ingredient(ingredient: schemas.IngredientCreate, db: Session = Depends(get_db)):
    db_ingredient = models.Ingredient(**ingredient.dict())
    db.add(db_ingredient)
    db.commit()
    db.refresh(db_ingredient)
    return db_ingredient

@router.get("/", response_model=list[schemas.Ingredient])
def read_ingredients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Ingredient).offset(skip).limit(limit).all()
