from pydantic import BaseModel
from typing import Optional
from schemas.order_schema import Order


class AgentState(BaseModel):
    ticket: str
    order: Optional[Order] = None
    refund_eligible: Optional[bool] = None
    resolved: bool = False