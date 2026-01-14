def build_final_response(classified: dict, text: str):
    """
    Step 4: Final Output with provenance
    """

    final_amounts = []

    for item in classified["amounts"]:
        label = item["type"].replace("_", " ").title()
        final_amounts.append({
            "type": item["type"],
            "value": item["value"],
            "source": f"text: '{label}'"
        })

    return {
        "currency": "INR",
        "amounts": final_amounts,
        "status": "ok"
    }
