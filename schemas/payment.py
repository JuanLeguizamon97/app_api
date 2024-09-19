from pydantic import BaseModel
from typing import List, Dict

class PaymentInfo(BaseModel):
    payment_id: int
    user_id: int
    order_id: int
    amount: float
    payment_method: str
    payment_status: str

class PaymentCreate(PaymentInfo):
    pass   