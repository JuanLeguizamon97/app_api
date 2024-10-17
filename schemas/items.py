from pydantic import BaseModel
from typing import Optional

class ItemCreateResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    available: bool

    class Config:
        from_attributes = True

class ItemModel(BaseModel):
    name: str
    description: Optional[str]
    price: float
    available: bool
    quantity: int

    class Config:
        from_attributes = True 