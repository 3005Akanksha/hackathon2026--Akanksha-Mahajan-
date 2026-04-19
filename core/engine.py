import re
from core.state import AgentState
from core.classifier import classify_ticket

from services.order_service import fetch_order
from services.refund_service import check_refund_eligibility
from services.refund_executor import issue_refund
from services.reply_service import send_reply
from services.escalation_service import escalate
from services.knowledge_service import search_kb


def extract_order_id(text):
    match = re.search(r'ORD[-\s]?\d+', text)
    return match.group(0) if match else None


def run_agent(ticket: str):
    state = AgentState(ticket=ticket)

    log = {
        "ticket": ticket,
        "intent": None,
        "steps": []
    }

    # 🧠 classify
    intent = classify_ticket(ticket)
    state.intent = intent
    log["intent"] = intent

    # 🔍 extract order id
    order_id = extract_order_id(ticket)

    if order_id:
        order = fetch_order(order_id)
        state.order = order

        log["steps"].append({
            "action": "fetch_order",
            "result": order
        })
    else:
        log["steps"].append({
            "action": "fetch_order",
            "result": "No order ID"
        })
        escalate("Missing order ID")
        log["final_decision"] = "escalated"
        return {"state": state, "log": log}

    # 🔁 flows
    if intent == "refund":
        eligible = check_refund_eligibility(order_id)

        log["steps"].append({
            "action": "check_refund",
            "result": eligible
        })

        if eligible:
            result = issue_refund(order_id)

            log["steps"].append({
                "action": "issue_refund",
                "result": result
            })

            reply = send_reply("Refund processed")

            log["steps"].append({
                "action": "send_reply",
                "result": reply
            })

            log["final_decision"] = "refund_processed"

        else:
            kb = search_kb("refund")

            log["steps"].append({
                "action": "search_kb",
                "result": kb
            })

            escalate("Not eligible")
            log["final_decision"] = "escalated"

    elif intent == "cancel":
        reply = send_reply(f"{order_id} cancelled")

        log["steps"].append({
            "action": "cancel_order",
            "result": f"{order_id} cancelled"
        })

        log["steps"].append({
            "action": "send_reply",
            "result": reply
        })

        log["final_decision"] = "cancelled"

    elif intent == "tracking":
        reply = send_reply("Order in transit")

        log["steps"].append({
            "action": "track_order",
            "result": "In transit"
        })

        log["steps"].append({
            "action": "send_reply",
            "result": reply
        })

        log["final_decision"] = "tracking_shared"

    else:
        escalate("Unknown intent")

        log["steps"].append({
            "action": "escalate",
            "result": "Unknown intent"
        })

        log["final_decision"] = "escalated"

    return {"state": state, "log": log}