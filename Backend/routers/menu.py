from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from io import BytesIO

router = APIRouter()

@router.post("/menu/analyze")
async def analyze_menu(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        if file.filename.endswith('.csv'):
            df = pd.read_csv(BytesIO(contents))
        elif file.filename.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(BytesIO(contents))
        else:
            raise HTTPException(status_code=400, detail="Invalid file format")

        required_cols = ['Item Name', 'Price', 'Quantity Sold']
        if not all(col in df.columns for col in required_cols):
            raise HTTPException(status_code=400, detail=f"Missing required columns: {required_cols}")

        df['Total Sales'] = df['Price'] * df['Quantity Sold']
        summary = df.groupby('Item Name').agg({
            'Quantity Sold': 'sum',
            'Total Sales': 'sum',
            'Price': 'mean'
        }).sort_values(by='Total Sales', ascending=False).reset_index()

        top_items = summary.head(5).to_dict(orient='records')
        bottom_items = summary.tail(5).to_dict(orient='records')

        response = {
            "top_performers": top_items,
            "underperformers": bottom_items,
            "recommendations": [
                "Consider promoting low-volume, high-priced dishes.",
                "Review pricing for top-selling items with low average price.",
            ]
        }
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
