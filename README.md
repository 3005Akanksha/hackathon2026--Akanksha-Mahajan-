# 🤖 AutoResolve AI Agent

## 🚀 Overview

This project is a AutoResolve AI Agent that processes customer tickets end-to-end using a multi-step decision-making system.

Unlike traditional chatbots, this system:

* Understands user intent
* Executes multiple tools
* Handles failures
* Escalates when needed
* Logs every decision

---

## 🧠 Key Features

* 🔄 Multi-step Agent Loop (ReAct-style)
* 🧩 Tool-based Architecture (6+ tools)
* 📊 Structured Decision Making (Pydantic)
* ⚠️ Error Handling & Escalation
* 🧾 Full Audit Logging
* 🖥️ Interactive UI (Streamlit)
* 📦 Batch Processing (20 tickets)

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Pydantic
* Custom Agent Loop (LLM-agnostic)

---

## ⚙️ How to Run

### 1. Setup


git clone <repo>
cd hackathon2026-akanksha
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt


### 2. Run UI


streamlit run app.py


### 3. Run 20 Tickets (IMPORTANT)


python run_all.py


---

## 📁 Output

* `audit_log.json` → contains all 20 tickets with full reasoning
* `logs/` → individual execution logs

---

## 🧠 Agent Flow

Ticket → Classify → Plan → Execute Tools → Decide → Respond / Escalate

---

## 🔥 Why This is Different

* Not a chatbot — a decision-making system
* Multi-tool orchestration
* Handles uncertainty
* Fully auditable

---


## 🚧 Future Improvements

* Real LLM integration
* Async concurrency Better intent classification
* Memory & personalization

---
