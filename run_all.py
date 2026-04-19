import json
from core.engine import run_agent

# Load hackathon tickets
with open("data/tickets.json", "r") as f:
    tickets = json.load(f)

all_logs = []

print("\n🚀 Running Hackathon Tickets...\n")

for i, ticket in enumerate(tickets, 1):
    print(f"\n==============================")
    print(f"Ticket {i}: {ticket['ticket_id']}")
    print(f"==============================")

    # 👉 Use SUBJECT + BODY (IMPORTANT)
    input_text = ticket["subject"] + " " + ticket["body"]

    try:
        result = run_agent(input_text)
        log = result["log"]

        # Add metadata
        log["ticket_id"] = ticket["ticket_id"]
        log["expected_action"] = ticket["expected_action"]

        all_logs.append(log)

    except Exception as e:
        print("[ERROR]", e)

# Save final audit log
with open("audit_log.json", "w") as f:
    json.dump(all_logs, f, indent=4)

print("\n✅ audit_log.json created\n")