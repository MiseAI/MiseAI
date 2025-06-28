from pydantic import BaseModel
from datetime import datetime

class InvoiceOut(BaseModel):
    id: int
    filename: str
    uploaded_at: datetime

    class Config:
        orm_mode = True
