from fastapi import APIRouter, UploadFile, File, HTTPException
from pdfminer.high_level import extract_text
import pytesseract
from PIL import Image
import io
import re

router = APIRouter()

@router.post("/parse")
async def parse_invoice(file: UploadFile = File(...)):
    content = await file.read()
    try:
        if file.filename.lower().endswith(".pdf"):
            text = extract_text(io.BytesIO(content))
        else:
            image = Image.open(io.BytesIO(content))
            text = pytesseract.image_to_string(image)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to extract text: {e}")

    lines = text.splitlines()
    items = []
    pattern = re.compile(r"(?P<item>\D+?)\s+(?P<price>\d+\.?\d*)$")
    for line in lines:
        m = pattern.search(line)
        if m:
            items.append({
                "item": m.group("item").strip(),
                "price": float(m.group("price"))
            })

    vendor = file.filename.split('_')[0]
    return {"vendor": vendor, "items": items}
