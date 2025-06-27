import pandas as pd
from schemas.forecast import ForecastRequest, ForecastResponse
from datetime import datetime
from typing import List

class ForecastEngine:
    def predict(self, data: ForecastRequest) -> ForecastResponse:
        df = pd.DataFrame(data.sales_data)
        df['date'] = pd.to_datetime(df['date'])

        summary = df.groupby('item').agg({'quantity': 'sum'}).reset_index()
        summary = summary.sort_values(by='quantity', ascending=False)

        forecast = [{"item": row['item'], "predicted_quantity": int(row['quantity'] * 1.1)} for _, row in summary.iterrows()]
        return ForecastResponse(forecast=forecast)
