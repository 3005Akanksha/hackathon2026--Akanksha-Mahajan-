import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.state import AgentState


state = AgentState(ticket="Refund for ORD123")

print("Ticket:", state.ticket)
print("Resolved:", state.resolved)

# change value
state.resolved = True

print("After update:", state.resolved)