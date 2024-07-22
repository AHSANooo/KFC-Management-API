# api/inventory/endpoints.py
from fastapi import APIRouter, HTTPException, status
from typing import List
from .models import InventoryItem, InventoryItemInDB
from .service import create_inventory_item, get_inventory_item, update_inventory_item, delete_inventory_item, list_inventory_items

router = APIRouter()

@router.post("/", response_model=InventoryItemInDB)
def add_inventory_item(item: InventoryItem):
    return create_inventory_item(item)

@router.get("/{item_id}", response_model=InventoryItemInDB)
def read_inventory_item(item_id: int):
    item = get_inventory_item(item_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inventory item not found")
    return item

@router.put("/{item_id}", response_model=InventoryItemInDB)
def update_inventory_item(item_id: int, item: InventoryItem):
    updated_item = update_inventory_item(item_id, item)
    if updated_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inventory item not found")
    return updated_item

@router.delete("/{item_id}", response_model=InventoryItemInDB)
def delete_inventory_item(item_id: int):
    item = delete_inventory_item(item_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inventory item not found")
    return item

@router.get("/", response_model=List[InventoryItemInDB])
def list_all_inventory_items():
    return list_inventory_items()
