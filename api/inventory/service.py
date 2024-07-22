# api/inventory/service.py
from typing import List, Optional
from .models import InventoryItem, InventoryItemInDB

# Dummy database
fake_inventory_db = {}
next_id = 1

def create_inventory_item(item: InventoryItem) -> InventoryItemInDB:
    global next_id
    item_in_db = InventoryItemInDB(**item.dict(), id=next_id)
    fake_inventory_db[next_id] = item_in_db
    next_id += 1
    return item_in_db

def get_inventory_item(item_id: int) -> Optional[InventoryItemInDB]:
    return fake_inventory_db.get(item_id)

def update_inventory_item(item_id: int, item: InventoryItem) -> Optional[InventoryItemInDB]:
    if item_id in fake_inventory_db:
        updated_item = InventoryItemInDB(**item.dict(), id=item_id)
        fake_inventory_db[item_id] = updated_item
        return updated_item
    return None

def delete_inventory_item(item_id: int) -> Optional[InventoryItemInDB]:
    return fake_inventory_db.pop(item_id, None)

def list_inventory_items() -> List[InventoryItemInDB]:
    return list(fake_inventory_db.values())
