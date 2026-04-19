import streamlit as st
import json
from core.engine import run_agent

st.title("🤖 AI Customer Support Agent")

with open("data/tickets.json", "r") as f:
    tickets_data = json.load(f)

ticket_input = st.text_input("Enter Ticket ID or Text")

if st.button("Run Agent"):
    selected_ticket = None

    for t in tickets_data:
        if t["ticket_id"] == ticket_input:
            selected_ticket = t
            break

    if selected_ticket:
        full_text = selected_ticket["subject"] + " " + selected_ticket["body"]
        st.info(f"Using dataset ticket: {ticket_input}")
    else:
        full_text = ticket_input

    result = run_agent(full_text)
    log = result["log"]

    st.success("Agent Completed")

    for step in log["steps"]:
        st.write(step)

    st.write("Final Decision:", log["final_decision"])