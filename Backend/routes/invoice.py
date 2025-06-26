from fastapi import APIRouter, UploadFile, File
import pytesseract
import pdfminer.high_level as pdf

router = APIRouter()

@router.post("/parse")
async def parse_invoice(file: UploadFile = File(...)):
    content = await file.read()
    # stub: parse content with PDFMiner and OCR
    return {"vendor": "", "items": []}