def generate_forecast(data):
    forecast = {}
    for dish, sales in data.past_sales.items():
        if sales:
            forecast[dish] = int(sum(sales) / len(sales))
        else:
            forecast[dish] = 0
    return {"forecast": forecast}
