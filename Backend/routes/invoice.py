from fastapi import APIRouter, UploadFile, File
import pytesseract, pdfminer.high_level as pdf

router = APIRouter()

@router.post("/parse")
async def parse_invoice(file: UploadFile = File(...)):
    content = await file.read()
    return {"vendor": "", "items": []}
