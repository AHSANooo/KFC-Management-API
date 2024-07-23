from typing import Dict, List
from pydantic import BaseModel
from src.utils.json_storage import read_json_file, write_json_file
from fastapi import HTTPException, status

PRODUCTS_FILE = 'config/products/products.json'

class Product(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

class ProductInDB(Product):
    id: int

def get_products_db() -> Dict[str, Dict]:
    """Read the product data from the JSON file."""
    try:
        return read_json_file(PRODUCTS_FILE)
    except FileNotFoundError:
        return {}

def save_products_db(products: Dict[str, Dict]) -> None:
    """Save product data to the JSON file."""
    write_json_file(PRODUCTS_FILE, products)

def get_all_products() -> List[ProductInDB]:
    """Retrieve all products."""
    products_db = get_products_db()
    return [ProductInDB(**product) for product in products_db.values()]

def create_product(product: Product) -> ProductInDB:
    """Create a new product."""
    products_db = get_products_db()
    product_id = max(map(int, products_db.keys()), default=0) + 1
    product_data = product.dict()
    product_data["id"] = product_id
    products_db[str(product_id)] = product_data
    save_products_db(products_db)
    return ProductInDB(id=product_id, **product_data)

def get_product(product_id: int) -> ProductInDB:
    """Retrieve a product by its ID."""
    products_db = get_products_db()
    product = products_db.get(str(product_id))
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return ProductInDB(id=product_id, **product)

def update_product(product_id: int, product: Product) -> ProductInDB:
    """Update an existing product by its ID."""
    products_db = get_products_db()
    if str(product_id) not in products_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    product_data = product.dict()
    product_data["id"] = product_id
    products_db[str(product_id)] = product_data
    save_products_db(products_db)
    return ProductInDB(id=product_id, **product_data)

def delete_product(product_id: int) -> None:
    """Delete a product by its ID."""
    products_db = get_products_db()
    if str(product_id) not in products_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    del products_db[str(product_id)]
    save_products_db(products_db)
