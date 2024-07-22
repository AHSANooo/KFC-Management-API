# api/tasks/endpoints.py
from fastapi import APIRouter, Depends
from api.auth.models import Order
from api.auth.service import create_order, get_orders
from api.auth.endpoints import oauth2_scheme

router = APIRouter()

@router.post("/")
def place_order(order: Order, token: str = Depends(oauth2_scheme)):
    return create_order(order)

@router.get("/")
def list_orders(token: str = Depends(oauth2_scheme)):
    return get_orders()
