
import pandas as pd
from datetime import datetime
from schemas.vendor import VendorSuggestionRequest

class VendorAnalyzer:
    def __init__(self):
        self.data = pd.read_csv("data/vendor_prices.csv")

    def get_price_history(self, item_name: str):
        filtered = self.data[self.data["item_name"] == item_name]
        history = filtered[["date", "price", "vendor"]].sort_values("date")
        return {
            "item": item_name,
            "history": history.to_dict(orient="records")
        }

    def suggest_vendors(self, req: VendorSuggestionRequest):
        item_data = self.data[self.data["item_name"] == req.item_name]
        latest_prices = item_data.sort_values("date").groupby("vendor").last().reset_index()
        sorted_vendors = latest_prices.sort_values("price")
        return {
            "item": req.item_name,
            "suggestions": sorted_vendors[["vendor", "price"]].to_dict(orient="records")
        }
