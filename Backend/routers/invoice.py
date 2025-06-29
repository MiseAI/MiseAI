from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import os

from Backend import database, models, schemas
from Backend.core.security import get_current_user

router = APIRouter(
    prefix="/api/invoice",
    tags=["invoices"],
)

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/download/{invoice_id}")
def download_invoice(
    invoice_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    # Lookup invoice for this user
    invoice = (
        db.query(models.Invoice)
        .filter(models.Invoice.id == invoice_id)
        .filter(models.Invoice.user_id == current_user.id)
        .first()
    )

    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found.")

    file_path = invoice.file_path

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found on disk.")

    return FileResponse(
        path=file_path,
        filename=invoice.filename,
        media_type="application/octet-stream",
    )
