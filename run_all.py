from core.engine import run_agent
from data.tickets import tickets
import json

print("\n🚀 Running 20 Tickets...\n")

all_logs = []   # 👉 store all results

for i, ticket in enumerate(tickets, 1):
    print(f"\n==============================")
    print(f"Ticket {i}: {ticket}")
    print(f"==============================")

    try:
        result = run_agent(ticket)   # 👈 IMPORTANT
        all_logs.append(result["log"])   # 👈 collect log

    except Exception as e:
        print("[ERROR]", e)

# 👉 SAVE ALL LOGS IN ONE FILE
with open("audit_log.json", "w") as f:
    json.dump(all_logs, f, indent=4)

print("\n✅ audit_log.json created\n")