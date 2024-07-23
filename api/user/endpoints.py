# api/user/endpoints.py

from fastapi import APIRouter, Depends
from api.auth.dependencies import get_current_user

router = APIRouter()


@router.get("/profile/")
async def read_user_profile(current_user: dict = Depends(get_current_user)):
    return current_user
