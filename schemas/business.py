from pydantic import BaseModel
from typing import List, Dict

class BusinessProfile(BaseModel):
    business_id: int
    business_name: str
    email: str
    password: str

    class Config:
        rom_attributes = True