from sqlalchemy.orm import Session
from models import SalesData, Recipe, InvoiceItem
from database_config import SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_sales(db: Session):
    return db.query(SalesData).all()


def get_recipes(db: Session):
    return db.query(Recipe).all()


def get_invoice_items(db: Session):
    return db.query(InvoiceItem).all()
