
from fastapi import APIRouter, UploadFile, File
import pandas as pd
import openai
import os

router = APIRouter()

openai.api_key = os.getenv("OPENAI_API_KEY")

@router.post("/chat/")
async def chat_assistant(query: str, sales_file: UploadFile = File(...)):
    # Load sales data
    df = pd.read_csv(sales_file.file)

    # Sample prompt to guide GPT
    prompt = f"""
You are a restaurant operations AI assistant.
You have access to the following sales data:

{df.head(10).to_string(index=False)}

User question: {query}

Use the data to provide a concise, helpful answer.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You analyze restaurant sales and performance."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return {"response": response.choices[0].message["content"]}
