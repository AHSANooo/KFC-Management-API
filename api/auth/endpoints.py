# api/auth/endpoints.py
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from .service import create_access_token, verify_token, get_password_hash, verify_password
from .models import User, UserInDB, Token, TokenData
from typing import Optional

router = APIRouter()

class Login(BaseModel):
    username: str
    password: str

# Dummy database
fake_users_db = {
    "testuser": {
        "username": "testuser",
        "email": "testuser@example.com",
        "hashed_password": get_password_hash("password")
    }
}

@router.post("/token", response_model=Token)
def login(form_data: Login):
    user = fake_users_db.get(form_data.username)
    if user is None or not verify_password(form_data.password, user['hashed_password']):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me", response_model=User)
def read_users_me(token: str = Depends(verify_token)):
    if token is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    user = fake_users_db.get(token.username)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
