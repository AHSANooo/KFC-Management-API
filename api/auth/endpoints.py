from datetime import timedelta
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from api.auth.models import User, Token, TokenData
from api.auth.service import authenticate_user, create_access_token, get_user, get_password_hash, get_users_db, \
    save_users_db
from api.auth.dependencies import get_current_user
from config.settings import ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()


@router.post("/register/")
async def register(user: User):
    users_db = get_users_db()
    if user.username in users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )
    hashed_password = get_password_hash(user.password)
    users_db[user.username] = {"username": user.username, "password": hashed_password}
    save_users_db(users_db)
    return {"message": "User registered successfully"}


@router.post("/token/", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
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


@router.get("/profile/", response_model=User)
async def get_user_profile(current_user: User = Depends(get_current_user)):
    return current_user
