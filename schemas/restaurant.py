from pydantic import BaseModel
from typing import List, Dict

class RestaurantProfile(BaseModel):
    restaurant_id: int
    restaurant_name: str
    email: str
    password: str

    class Config:
        rom_attributes = True