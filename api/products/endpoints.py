from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import List
from api.auth.service import verify_token
from api.products.service import (
    get_product,
    create_product,
    update_product,
    delete_product,
    get_all_products
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

@router.get("/", response_model=List[Product])
async def read_all_products(user: dict = Depends(get_current_user)):
    """Retrieve all products. Requires authentication."""
    products = get_all_products()
    return products

@router.get("/{product_id}", response_model=Product)
async def read_product(product_id: int, user: dict = Depends(get_current_user)):
    """Retrieve a single product by ID. Requires authentication."""
    product = get_product(product_id)
    return product

@router.post("/", response_model=Product)
async def create_new_product(product: Product, user: dict = Depends(get_current_user)):
    """Create a new product. Requires authentication."""
    new_product = create_product(product)
    return new_product

@router.put("/{product_id}", response_model=Product)
async def update_existing_product(product_id: int, product: Product, user: dict = Depends(get_current_user)):
    """Update an existing product by ID. Requires authentication."""
    updated_product = update_product(product_id, product)
    return updated_product

@router.delete("/{product_id}", response_model=dict)
async def delete_product_by_id(product_id: int, user: dict = Depends(get_current_user)):
    """Delete a product by ID. Requires authentication."""
    delete_product(product_id)
    return {"message": "Product deleted successfully"}
