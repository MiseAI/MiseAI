from fastapi import APIRouter, UploadFile, File
from services.invoice_parser import parse_pdf_invoice
import tempfile

router = APIRouter()

@router.post("/upload-invoice")
async def upload_invoice(file: UploadFile = File(...)):
    suffix = "." + file.filename.split(".")[-1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp:
        temp.write(await file.read())
        temp_path = temp.name

    invoice_data = parse_pdf_invoice(temp_path)
    return invoice_data
