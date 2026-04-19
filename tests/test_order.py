import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.order_service import fetch_order
from services.refund_service import check_refund_eligibility


def run_test():
    try:
        order = fetch_order("ORD123")
        print("[Order]", order)

        eligible = check_refund_eligibility(order)
        print("[Refund Eligible]", eligible)

    except Exception as e:
        print("[Error]", e)


if __name__ == "__main__":
    run_test()