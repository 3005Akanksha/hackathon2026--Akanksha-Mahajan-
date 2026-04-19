import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.engine import run_agent


if __name__ == "__main__":
    run_agent("I want refund for ORD123")
    run_agent("refund ORD999 please")