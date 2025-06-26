from fastapi import APIRouter, UploadFile, File
import pandas as pd

router = APIRouter()

@router.post("/analyze")
async def analyze_menu(file: UploadFile = File(...)):
    df = pd.read_excel(await file.read())
    return {"topItems": [], "lowPerformers": []}