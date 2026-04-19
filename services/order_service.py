import random

def fetch_order(order_id):
    print("[Service] Fetching order...")

    return {
        "order_id": order_id,
        "status": random.choice(["delivered", "shipped", "processing", "cancelled"]),
        "amount": random.randint(100, 1000)
    }