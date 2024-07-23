from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from .models import InventoryItem, InventoryItemInDB
from .service import create_inventory_item, get_inventory_item, update_inventory_item, delete_inventory_item, \
    list_inventory_items
from api.auth.dependencies import get_current_user
from api.auth.models import User

router = APIRouter()


@router.post("/", response_model=InventoryItemInDB)
def add_inventory_item(item: InventoryItem, current_user: User = Depends(get_current_user)):
    return create_inventory_item(item)


@router.get("/{item_id}", response_model=InventoryItemInDB)
def read_inventory_item(item_id: int, current_user: User = Depends(get_current_user)):
    item = get_inventory_item(item_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inventory item not found")
    return item


@router.put("/{item_id}", response_model=InventoryItemInDB)
def update_inventory_item(item_id: int, item: InventoryItem, current_user: User = Depends(get_current_user)):
    updated_item = update_inventory_item(item_id, item)
    if updated_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inventory item not found")
    return updated_item


@router.delete("/{item_id}", response_model=InventoryItemInDB)
def delete_inventory_item(item_id: int, current_user: User = Depends(get_current_user)):
    item = delete_inventory_item(item_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inventory item not found")
    return item


@router.get("/", response_model=List[InventoryItemInDB])
def list_all_inventory_items(current_user: User = Depends(get_current_user)):
    return list_inventory_items()
