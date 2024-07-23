# api/auth/endpoints.py

from datetime import timedelta
from api.auth.service import create_access_token, verify_password, get_password_hash, ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from api.auth.service import create_access_token, verify_password, get_password_hash
from api.auth.models import User
from src.utils.json_storage import read_json_file, write_json_file

router = APIRouter()
fake_users_db = {}

USERS_FILE = 'config/users.json'


def get_user(username: str):
    users_db = read_json_file(USERS_FILE)
    return users_db.get(username)


def authenticate_user(username: str, password: str):
    user = get_user(username)
    if user and verify_password(password, user["password"]):
        return user
    return False


@router.post("/register/")
async def register(user: User):
    users_db = read_json_file(USERS_FILE)
    if user.username in users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )
    users_db[user.username] = {"username": user.username, "password": get_password_hash(user.password), "tasks": []}
    write_json_file(USERS_FILE, users_db)
    return {"message": "User registered successfully"}


@router.post("/token/")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user["username"]}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
