from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional

class InvoiceItemBase(BaseModel):
    name: str
    quantity: float
    unit: Optional[str] = None
    price: float
    matched_ingredient_id: Optional[int] = None

class InvoiceItemCreate(InvoiceItemBase):
    pass

class InvoiceItem(InvoiceItemBase):
    id: int

    class Config:
        orm_mode = True

class InvoiceBase(BaseModel):
    vendor: str
    date: date
    file_name: Optional[str] = None

class InvoiceCreate(InvoiceBase):
    pass

class Invoice(InvoiceBase):
    id: int
    uploaded_at: datetime

    class Config:
        orm_mode = True
