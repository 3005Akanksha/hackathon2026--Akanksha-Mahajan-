def search_kb(query):
    print("[Service] Searching knowledge base...")

    if "refund" in query:
        return "Refund allowed within 7 days"
    elif "return" in query:
        return "Return allowed within 15 days"
    else:
        return "No policy found"