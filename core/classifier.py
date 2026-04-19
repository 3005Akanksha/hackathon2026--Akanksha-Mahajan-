def classify_ticket(text: str):
    text = text.lower()

    if "refund" in text or "return" in text:
        return "refund"
    elif "cancel" in text:
        return "cancel"
    elif "where" in text or "track" in text:
        return "tracking"
    else:
        return "unknown"