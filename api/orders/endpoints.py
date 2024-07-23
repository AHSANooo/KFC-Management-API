# api/orders/endpoints.py

from fastapi import APIRouter, Depends, HTTPException
from api.auth.dependencies import get_current_user

router = APIRouter()

orders_db = {}

@router.get("/orders/")
async def read_orders(current_user: dict = Depends(get_current_user)):
    return orders_db

@router.post("/orders/")
async def create_order(order: dict, current_user: dict = Depends(get_current_user)):
    order_id = len(orders_db) + 1
    orders_db[order_id] = order
    return {"id": order_id, "order": order}

@router.put("/orders/{order_id}")
async def update_order(order_id: int, order: dict, current_user: dict = Depends(get_current_user)):
    if order_id not in orders_db:
        raise HTTPException(status_code=404, detail="Order not found")
    orders_db[order_id] = order
    return {"id": order_id, "order": order}

@router.delete("/orders/{order_id}")
async def delete_order(order_id: int, current_user: dict = Depends(get_current_user)):
    if order_id not in orders_db:
        raise HTTPException(status_code=404, detail="Order not found")
    del orders_db[order_id]
    return {"message": "Order deleted"}
