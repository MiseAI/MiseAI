from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from io import BytesIO

router = APIRouter()

@router.post("/analyze")
async def analyze_menu(file: UploadFile = File(...)):
    content = await file.read()
    try:
        # Support CSV or Excel
        if file.filename.lower().endswith('.csv'):
            df = pd.read_csv(BytesIO(content))
        else:
            df = pd.read_excel(BytesIO(content))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to read file: {e}")

    if 'item' not in df.columns or 'quantity' not in df.columns or 'price' not in df.columns:
        raise HTTPException(status_code=422, detail="File must contain 'item', 'quantity', and 'price' columns")

    # Calculate total sales per item
    df['sales'] = df['quantity'] * df['price']
    summary = df.groupby('item').agg(
        total_quantity=pd.NamedAgg(column='quantity', aggfunc='sum'),
        total_sales=pd.NamedAgg(column='sales', aggfunc='sum')
    ).reset_index()

    # Get top and bottom performers
    top_items = summary.nlargest(5, 'total_quantity').to_dict(orient='records')
    low_items = summary.nsmallest(5, 'total_quantity').to_dict(orient='records')

    return {
        "topItems": top_items,
        "lowPerformers": low_items,
        "summary": summary.to_dict(orient='records')
    }
