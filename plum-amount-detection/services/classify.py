def classify_amounts(text: str, amounts: list):
    """
    Step 3: Classification by Context
    Label amounts based on surrounding keywords
    """

    results = []
    text_lower = text.lower()

    for amount in amounts:
        if "total" in text_lower:
            results.append({"type": "total_bill", "value": amount})
            text_lower = text_lower.replace("total", "", 1)
        elif "paid" in text_lower:
            results.append({"type": "paid", "value": amount})
            text_lower = text_lower.replace("paid", "", 1)
        elif "due" in text_lower:
            results.append({"type": "due", "value": amount})
            text_lower = text_lower.replace("due", "", 1)

    return {
        "amounts": results,
        "confidence": 0.80
    }
