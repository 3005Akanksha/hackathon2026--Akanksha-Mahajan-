Failure Modes & Handling

Failure Modes & Handling

1. Missing or Invalid Order ID

Scenario:
User submits a request without a valid order ID
(e.g., "I want a refund")

Impact:
System cannot fetch order details → flow breaks

Handling:

* Regex-based extraction fails
* Agent detects missing ID
* Stops execution safely
* Escalates to human support

Outcome:
No crash, graceful fallback with audit log entry

---

3. Refund Not Eligible

Scenario:
Order does not meet refund criteria
(e.g., already shipped or outside policy)

Impact:
Refund action should not be executed

Handling:

* `check_refund_eligibility` returns False
* Agent skips refund execution
* Uses knowledge base for policy reasoning
* Escalates or informs user

Outcome:
Correct business logic enforcement

---

3. Knowledge Gap (Policy Uncertainty)

Scenario:
System unsure about refund rules

Impact:
Incorrect decision risk

Handling:

* Queries knowledge base (`search_kb`)
* Adds reasoning step
* Falls back to escalation if unclear

Outcome:
Improved decision quality + transparency

---
