from services.order_service import fetch_order

def check_refund_eligibility(order_id):
    order = fetch_order(order_id)

    if order["status"] == "delivered":
        return True
    return False