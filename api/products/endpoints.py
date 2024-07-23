# api/products/endpoints.py

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import List
from api.auth.service import verify_token
from api.products.service import (
    get_product,
    create_product,
    update_product,
    delete_product
)
from api.products.models import Product

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    """Retrieve the current user from the token."""
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload


@router.get("/{product_id}", response_model=Product)
async def read_product(product_id: int, user: dict = Depends(get_current_user)):
    """Retrieve a single product by ID. Requires authentication."""
    product = get_product(user, product_id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product

@router.post("/", response_model=Product)
async def create_new_product(product: Product, user: dict = Depends(get_current_user)):
    """Create a new product. Requires authentication."""
    new_product = create_product(user, product)
    return new_product

@router.put("/{product_id}", response_model=Product)
async def update_existing_product(product_id: int, product: Product, user: dict = Depends(get_current_user)):
    """Update an existing product by ID. Requires authentication."""
    updated_product = update_product(user, product_id, product)
    if updated_product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return updated_product

@router.delete("/{product_id}", response_model=dict)
async def delete_product_by_id(product_id: int, user: dict = Depends(get_current_user)):
    """Delete a product by ID. Requires authentication."""
    success = delete_product(user, product_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return {"message": "Product deleted successfully"}
