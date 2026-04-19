from schemas.action_schema import Action

def ask_llm(state) -> Action:
    """
    Fake structured LLM
    """

    if state.order is None:
        return Action(action="fetch_order")

    if state.refund_eligible is None:
        return Action(action="check_refund")

    return Action(action="finish")