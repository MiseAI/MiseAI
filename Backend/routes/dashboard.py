from fastapi import APIRouter
from models import SalesData, Recipe, InvoiceItem
from database.access import get_sales, get_recipes, get_invoice_items
from collections import defaultdict

router = APIRouter()

@router.get("/dashboard/summary")
async def get_dashboard_summary():
    sales = get_sales()
    recipes = get_recipes()
    invoices = get_invoice_items()

    recipe_costs = {r.name: r.cost for r in recipes}

    summary = []
    category_revenue = defaultdict(float)

    for item in sales:
        dish_name = item.item
        units_sold = item.quantity
        price = item.price
        total_sales = units_sold * price
        cost = recipe_costs.get(dish_name, 0) * units_sold
        profit = total_sales - cost
        margin = (profit / total_sales) * 100 if total_sales else 0

        category_revenue[item.category] += total_sales

        summary.append({
            "dish": dish_name,
            "units_sold": units_sold,
            "revenue": round(total_sales, 2),
            "cost": round(cost, 2),
            "profit": round(profit, 2),
            "margin_pct": round(margin, 2),
        })

    summary = sorted(summary, key=lambda x: x["profit"], reverse=True)

    return {
        "top_items": summary[:5],
        "low_margin": sorted(summary, key=lambda x: x["margin_pct"])[:5],
        "category_breakdown": category_revenue,
        "total_profit": sum(item["profit"] for item in summary),
        "total_revenue": sum(item["revenue"] for item in summary)
    }
