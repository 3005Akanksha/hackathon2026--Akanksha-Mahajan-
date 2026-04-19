def classify_ticket(text: str) -> str:
    text = text.lower()

    if "refund" in text:
        return "refund"

    if "cancel" in text:
        return "cancel"

    if "where" in text or "track" in text:
        return "tracking"

    return "unknown"