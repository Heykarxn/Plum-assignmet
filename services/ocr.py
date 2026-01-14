import re

def extract_raw_tokens(text: str):
    """
    Step 1: OCR / Text Extraction
    Extract numeric tokens from text input
    """

    # Extract numbers and percentages
    tokens = re.findall(r'\d+%?', text)

    if not tokens:
        return {
            "status": "no_amounts_found",
            "reason": "document too noisy"
        }

    return {
        "raw_tokens": tokens,
        "currency_hint": "INR",
        "confidence": 0.74
    }

