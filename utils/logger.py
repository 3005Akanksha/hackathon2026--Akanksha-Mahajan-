import json
import os
from datetime import datetime


def save_log(log_data):
    os.makedirs("logs", exist_ok=True)

    filename = f"logs/run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, "w") as f:
        json.dump(log_data, f, indent=4)

    print(f"[Log Saved] {filename}")