from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
import os
from models.invoice import Invoice
from models.user import User
from schemas.invoice import InvoiceOut
from database import get_db
from core.security import get_current_user

router = APIRouter(prefix="/invoice", tags=["Invoices"])

UPLOAD_DIR = "uploaded_invoices"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_invoice(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    file_location = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_location, "wb") as f:
        f.write(await file.read())

    invoice = Invoice(
        filename=file.filename,
        file_path=file_location,
        user_id=current_user.id,
    )
    db.add(invoice)
    db.commit()
    db.refresh(invoice)

    return {"message": "File uploaded successfully", "invoice_id": invoice.id}


@router.get("/list", response_model=list[InvoiceOut])
def list_invoices(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    invoices = db.query(Invoice).filter(Invoice.user_id == current_user.id).all()
    return invoices
