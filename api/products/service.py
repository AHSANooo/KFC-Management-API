# api/products/service.py
from typing import List, Optional
from .models import Product, ProductInDB

# Dummy database
fake_products_db = {}
next_id = 1

def create_product(product: Product) -> ProductInDB:
    global next_id
    product_in_db = ProductInDB(**product.dict(), id=next_id)
    fake_products_db[next_id] = product_in_db
    next_id += 1
    return product_in_db

def get_product(product_id: int) -> Optional[ProductInDB]:
    return fake_products_db.get(product_id)

def update_product(product_id: int, product: Product) -> Optional[ProductInDB]:
    if product_id in fake_products_db:
        updated_product = ProductInDB(**product.dict(), id=product_id)
        fake_products_db[product_id] = updated_product
        return updated_product
    return None

def delete_product(product_id: int) -> Optional[ProductInDB]:
    return fake_products_db.pop(product_id, None)

def list_products() -> List[ProductInDB]:
    return list(fake_products_db.values())
