from pydantic import BaseModel

class Order(BaseModel):
    order_id: str
    status: str
    amount: float