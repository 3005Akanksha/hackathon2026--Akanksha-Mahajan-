import random
import time
from schemas.order_schema import Order

def fetch_order(order_id: str) -> Order:
    """
    Simulates fetching order from database/API
    """

    print(f"[Service] Fetching order {order_id}...")

    # simulate delay
    time.sleep(1)

    # simulate failure
    if random.random() < 0.2:
        raise Exception("Order service unavailable")

    return Order(
        order_id=order_id,
        status=random.choice(["delivered", "shipped", "cancelled"]),
        amount=round(random.uniform(100, 1000), 2)
    )