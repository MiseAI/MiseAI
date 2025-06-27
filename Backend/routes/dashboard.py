from database.access import get_sales, get_recipes, get_invoice_items

def example_dashboard_data():
    return {
        'sales': get_sales(),
        'recipes': get_recipes(),
        'invoice_items': get_invoice_items()
    }
