import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.state import AgentState
from core.llm import ask_llm
from core.classifier import classify_ticket

from services.order_service import fetch_order
from services.refund_service import check_refund_eligibility
from services.refund_executor import issue_refund
from services.reply_service import send_reply
from services.escalation_service import escalate
from services.knowledge_service import search_knowledge_base

from utils.logger import save_log
from utils.extractor import extract_order_id


def run_agent(ticket: str):
    print("\n[Agent Started]\n")

    # 🔹 Initialize state
    state = AgentState(ticket=ticket)

    # 🔹 Classify ticket
    intent = classify_ticket(ticket)
    print("[Intent]", intent)

    # 🔹 Initialize log
    log = {
        "ticket": ticket,
        "intent": intent,
        "steps": []
    }

    # 🔹 Agent loop
    while not state.resolved:

        decision = ask_llm(state)
        print("[Decision]", decision)

        step_data = {
            "action": decision.action,
            "result": None
        }

        # ===============================
        # 🔹 ACTION 1: FETCH ORDER
        # ===============================
        if decision.action == "fetch_order":
            try:
                order_id = extract_order_id(state.ticket)

                if not order_id:
                    print("[Error] No order ID found")
                    step_data["result"] = "No order ID"
                    state.resolved = True
                else:
                    state.order = fetch_order(order_id)
                    print("[Order Fetched]", state.order)

                    step_data["result"] = state.order.dict()

            except Exception as e:
                print("[Error - fetch_order]", e)
                step_data["result"] = str(e)

        # ===============================
        # 🔹 ACTION 2: CHECK REFUND
        # ===============================
        elif decision.action == "check_refund":
            if state.order:
                state.refund_eligible = check_refund_eligibility(state.order)
                print("[Refund Eligibility]", state.refund_eligible)

                step_data["result"] = state.refund_eligible
            else:
                print("[Warning] No order found")
                step_data["result"] = "No order"

        # ===============================
        # 🔹 ACTION 3: KNOWLEDGE BASE
        # ===============================
        elif decision.action == "search_kb":
            result = search_knowledge_base("refund policy")
            print("[KB Result]", result)

            step_data["result"] = result
            state.kb_checked = True

        # ===============================
        # 🔹 ACTION 4: ISSUE REFUND
        # ===============================
        elif decision.action == "issue_refund":
            if state.refund_eligible:
                result = issue_refund(state.order)
                print("[Refund Issued]", result)

                step_data["result"] = result
            else:
                print("[Refund Not Allowed]")
                step_data["result"] = "Not eligible"

        # ===============================
        # 🔹 ACTION 5: ESCALATE
        # ===============================
        elif decision.action == "escalate":
            result = escalate(state.ticket)
            print("[Escalated]", result)

            step_data["result"] = result
            state.resolved = True

        # ===============================
        # 🔹 ACTION 6: SEND REPLY
        # ===============================
        elif decision.action == "send_reply":
            message = "Your request has been processed successfully"
            result = send_reply(message)
            print("[Reply Sent]", result)

            step_data["result"] = result
            state.resolved = True

        # ===============================
        # 🔹 FINISH
        # ===============================
        elif decision.action == "finish":
            state.resolved = True
            step_data["result"] = "completed"

        # ===============================
        # 🔹 UNKNOWN
        # ===============================
        else:
            print("[Unknown Action]", decision.action)
            state.resolved = True
            step_data["result"] = "unknown action"

        # 🔹 Save step
        log["steps"].append(step_data)

    # 🔹 Final output
    print("\n[Final State]")
    print(state)

    save_log(log)

    print("\n[Agent Finished]\n")

    # 🔹 Return for UI
    return {
        "state": state,
        "log": log
    }