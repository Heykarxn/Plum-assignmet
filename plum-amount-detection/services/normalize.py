def normalize_tokens(tokens: list):
    """
    Step 2: Normalization
    Fix OCR digit errors and convert tokens to integers
    """

    normalized = []

    for token in tokens:
        # Fix common OCR mistakes
        token = token.replace('l', '1').replace('O', '0')

        # Ignore percentages like 10%
        if '%' in token:
            continue

        try:
            normalized.append(int(token))
        except ValueError:
            continue

    return {
        "normalized_amounts": normalized,
        "normalization_confidence": 0.82
    }
