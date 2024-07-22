# api/orders/models.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class OrderItem(BaseModel):
    product_id: int
    quantity: int

class Order(BaseModel):
    customer_name: str
    items: List[OrderItem]
    total_price: float
    order_date: Optional[datetime] = None

class OrderInDB(Order):
    id: int
