# api/orders/service.py
from typing import List, Optional
from .models import Order, OrderInDB

# Dummy database
fake_orders_db = {}
next_id = 1

def create_order(order: Order) -> OrderInDB:
    global next_id
    order_in_db = OrderInDB(**order.dict(), id=next_id)
    fake_orders_db[next_id] = order_in_db
    next_id += 1
    return order_in_db

def get_order(order_id: int) -> Optional[OrderInDB]:
    return fake_orders_db.get(order_id)

def update_order(order_id: int, order: Order) -> Optional[OrderInDB]:
    if order_id in fake_orders_db:
        updated_order = OrderInDB(**order.dict(), id=order_id)
        fake_orders_db[order_id] = updated_order
        return updated_order
    return None

def delete_order(order_id: int) -> Optional[OrderInDB]:
    return fake_orders_db.pop(order_id, None)

def list_orders() -> List[OrderInDB]:
    return list(fake_orders_db.values())
