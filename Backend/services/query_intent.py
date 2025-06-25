
def simple_fallback(prompt: str) -> str:
    prompt_lower = prompt.lower()

    if "top selling" in prompt_lower or "top dish" in prompt_lower:
        return "Top selling item: Burger (120 units sold)"
    elif "revenue" in prompt_lower:
        return "Total revenue for this period: $1,400"
    elif "profit" in prompt_lower:
        return "Highest profit margin: Chicken Sandwich - 65%"
    elif "invoice" in prompt_lower:
        return "Found 3 invoices containing 'chicken'."
    else:
        return "I'm not sure how to answer that, but I’m learning!"
