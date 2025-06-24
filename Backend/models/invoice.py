from pydantic import BaseModel
from typing import List
from datetime import date

class InvoiceItem(BaseModel):
    name: str
    quantity: float
    unit_price: float
    total_price: float

class Invoice(BaseModel):
    vendor: str
    invoice_date: date
    items: List[InvoiceItem]
