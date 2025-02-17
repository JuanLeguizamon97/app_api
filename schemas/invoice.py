from pydantic import BaseModel
from typing import List, Dict

class InvoiceGeneration(BaseModel):
    invoice_id: int
    restaurant_id: int
    restaurant_name: str
    items: Dict
    total: int

    #Pendiente de revisión para generación de facturas