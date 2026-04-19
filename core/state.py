from pydantic import BaseModel
from typing import Optional, Dict


class AgentState(BaseModel):
    ticket: str
    intent: Optional[str] = None
    order: Optional[Dict] = None
    refund_eligible: Optional[bool] = None
    resolved: bool = False