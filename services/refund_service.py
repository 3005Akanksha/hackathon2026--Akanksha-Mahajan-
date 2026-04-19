from schemas.order_schema import Order

def check_refund_eligibility(order: Order) -> bool:
    """
    Business logic:
    Only delivered orders are eligible for refund
    """

    print("[Service] Checking refund eligibility...")

    if order.status == "delivered":
        return True

    return False