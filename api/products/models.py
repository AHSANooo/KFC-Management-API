# api/products/models.py
from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

class ProductInDB(Product):
    id: int
