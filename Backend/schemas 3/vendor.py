
from pydantic import BaseModel

class VendorSuggestionRequest(BaseModel):
    item_name: str
