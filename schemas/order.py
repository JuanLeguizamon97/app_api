from pydantic import BaseModel, Field
from typing import Optional, List

class Order(BaseModel):

    id: Optional[int] = None
    restaurant_id: int