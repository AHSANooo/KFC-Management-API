# api/inventory/models.py
from pydantic import BaseModel
from typing import Optional

class InventoryItem(BaseModel):
    name: str
    description: Optional[str] = None
    quantity: int
    price: float

class InventoryItemInDB(InventoryItem):
    id: int
