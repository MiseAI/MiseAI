import fitz  # PyMuPDF
from typing import List
from models.invoice import Invoice, InvoiceItem
from datetime import date

def parse_pdf_invoice(file_path: str) -> Invoice:
    doc = fitz.open(file_path)
    text = "\n".join(page.get_text() for page in doc)

    # Dummy parser logic
    vendor = "Test Vendor Inc."
    invoice_date = date.today()
    items = [
        InvoiceItem(name="Butter", quantity=2, unit_price=3.5, total_price=7.0),
        InvoiceItem(name="Flour", quantity=5, unit_price=1.2, total_price=6.0),
    ]
    return Invoice(vendor=vendor, invoice_date=invoice_date, items=items)
