from pydantic import BaseModel
from typing import List, Dict

class OrderItem(BaseModel):
    item_id: int
    name: str
    quantity: int
    price: float

class OrderBase(BaseModel):
    items: List[OrderItem]
    total_price: float

class OrderCreate(OrderBase):
    business_id: int

class OrderResponse(OrderBase):
    id: int
    status: str
    paid_account: bool

    class Config:
        orm_mode = True