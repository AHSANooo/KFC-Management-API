# api/products/__init__.py
from fastapi import APIRouter

router = APIRouter()

from . import endpoints