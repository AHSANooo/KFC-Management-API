# api/products/endpoints.py
from fastapi import APIRouter, HTTPException, status
from typing import List
from .models import Product, ProductInDB
from .service import create_product, get_product, update_product, delete_product, list_products

router = APIRouter()

@router.post("/", response_model=ProductInDB)
def add_product(product: Product):
    return create_product(product)

@router.get("/{product_id}", response_model=ProductInDB)
def read_product(product_id: int):
    product = get_product(product_id)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=ProductInDB)
def update_product(product_id: int, product: Product):
    updated_product = update_product(product_id, product)
    if updated_product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return updated_product

@router.delete("/{product_id}", response_model=ProductInDB)
def delete_product(product_id: int):
    product = delete_product(product_id)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product

@router.get("/", response_model=List[ProductInDB])
def list_all_products():
    return list_products()
