import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import streamlit as st
from core.engine import run_agent

st.set_page_config(page_title="AI Support Agent", layout="centered")

st.title("🤖 AI Customer Support Agent")

st.write("Enter your support request (example: 'I want refund for ORD123')")

ticket = st.text_input("Enter Ticket")

if st.button("Run Agent"):

    if ticket.strip() == "":
        st.warning("Please enter a valid ticket")
    else:
        with st.spinner("Processing..."):

            result = run_agent(ticket)

            state = result["state"]
            log = result["log"]

        st.success("✅ Agent Completed")

        # 🔹 Show Order Info
        if state.order:
            st.subheader("📦 Order Details")
            st.json(state.order.dict())

        # 🔹 Refund Decision
        if state.refund_eligible is not None:
            if state.refund_eligible:
                st.success("💰 Refund Approved")
            else:
                st.error("❌ Refund Not Eligible")

        # 🔹 Steps
        st.subheader("🧠 Agent Steps")
        for step in log["steps"]:
            st.write(f"➡️ Action: {step['action']}")
            st.write(f"Result: {step['result']}")
            st.write("---")