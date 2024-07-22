# api/orders/endpoints.py
from fastapi import APIRouter, HTTPException, status
from typing import List
from .models import Order, OrderInDB
from .service import create_order, get_order, update_order, delete_order, list_orders

router = APIRouter()

@router.post("/", response_model=OrderInDB)
def add_order(order: Order):
    return create_order(order)

@router.get("/{order_id}", response_model=OrderInDB)
def read_order(order_id: int):
    order = get_order(order_id)
    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return order

@router.put("/{order_id}", response_model=OrderInDB)
def update_order(order_id: int, order: Order):
    updated_order = update_order(order_id, order)
    if updated_order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return updated_order

@router.delete("/{order_id}", response_model=OrderInDB)
def delete_order(order_id: int):
    order = delete_order(order_id)
    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return order

@router.get("/", response_model=List[OrderInDB])
def list_all_orders():
    return list_orders()
