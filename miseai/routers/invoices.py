from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.invoice import Invoice, InvoiceItem
from schemas import invoice as schemas
import csv
from io import StringIO
from datetime import datetime

router = APIRouter()

@router.post("/upload")
async def upload_invoice(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are supported.")

    contents = await file.read()
    decoded = contents.decode("utf-8")
    reader = csv.DictReader(StringIO(decoded))

    invoice = Invoice(
        vendor="Unknown Vendor",
        date=datetime.utcnow().date(),
        file_name=file.filename
    )
    db.add(invoice)
    db.commit()
    db.refresh(invoice)

    for row in reader:
        item = InvoiceItem(
            invoice_id=invoice.id,
            name=row.get("Item", ""),
            quantity=float(row.get("Quantity", 0)),
            unit=row.get("Unit", ""),
            price=float(row.get("Price", 0)),
        )
        db.add(item)

    db.commit()
    return {"message": "Invoice uploaded", "invoice_id": invoice.id}

@router.get("/", response_model=list[schemas.Invoice])
def list_invoices(db: Session = Depends(get_db)):
    return db.query(Invoice).all()

@router.get("/{invoice_id}", response_model=list[schemas.InvoiceItem])
def get_invoice_items(invoice_id: int, db: Session = Depends(get_db)):
    return db.query(InvoiceItem).filter(InvoiceItem.invoice_id == invoice_id).all()
