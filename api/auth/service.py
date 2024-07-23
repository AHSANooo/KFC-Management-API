# api/auth/service.py

from datetime import datetime, timedelta
from typing import Union
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status
from pydantic import BaseModel
import json
from pathlib import Path

# Configuration
SECRET_KEY = "your_secret_key"  # Use a secure, randomly generated secret key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Define User data model
class User(BaseModel):
    username: str
    password: str


# Read and write JSON utilities
def read_json_file(file_path: str) -> dict:
    """Read JSON data from a file."""
    if not Path(file_path).exists():
        return {}
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json_file(file_path: str, data: dict) -> None:
    """Write JSON data to a file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


# User data file path
USERS_FILE = 'config/users.json'


def get_users_db() -> dict:
    """Read the user data from the JSON file."""
    return read_json_file(USERS_FILE)


def save_users_db(users: dict) -> None:
    """Save user data to the JSON file."""
    write_json_file(USERS_FILE, users)


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None) -> str:
    """Create a new access token."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str) -> Union[dict, None]:
    """Verify the access token and return the payload if valid."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against a hashed password."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Hash a password."""
    return pwd_context.hash(password)


def get_user(username: str) -> dict:
    """Retrieve a user from the database by username."""
    users_db = get_users_db()
    return users_db.get(username)


def authenticate_user(username: str, password: str) -> Union[dict, bool]:
    """Authenticate a user by username and password."""
    user = get_user(username)
    if user and verify_password(password, user.get("password", "")):
        return user
    return False


def register_user(user: User) -> dict:
    """Register a new user."""
    users_db = get_users_db()
    if user.username in users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    hashed_password = get_password_hash(user.password)
    users_db[user.username] = {"username": user.username, "password": hashed_password}
    save_users_db(users_db)
    return {"message": "User registered successfully"}
