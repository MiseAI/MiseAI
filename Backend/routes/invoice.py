from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class InvoiceItem(BaseModel):
    item: str
    quantity: int
    price: float

invoices = []

@router.post("/invoice", response_model=InvoiceItem)
def create_invoice(item: InvoiceItem):
    invoices.append(item)
    return item

@router.get("/invoice", response_model=List[InvoiceItem])
def list_invoices():
    return invoices