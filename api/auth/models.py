# api/auth/models.py
from pydantic import BaseModel
from typing import Optional

# api/auth/models.py

from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str
