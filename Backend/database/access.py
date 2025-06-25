from models import SalesData, Recipe, InvoiceItem

def get_sales():
    return [SalesData(item="Pizza", quantity=30, price=12.0, category="Entree")]

def get_recipes():
    return [Recipe(name="Pizza", cost=5.0)]

def get_invoice_items():
    return [InvoiceItem(description="Pizza", quantity=30)]