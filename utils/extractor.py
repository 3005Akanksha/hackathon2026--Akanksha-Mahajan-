import re

def extract_order_id(text: str) -> str:
    """
    Extract order ID like ORD123 from text
    """

    match = re.search(r"ORD\d+", text)

    if match:
        return match.group()

    return None