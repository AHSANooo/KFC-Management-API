# api/auth/user_model.py

import csv
from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    username: str
    hashed_password: str

def load_users(filepath: str) -> List[User]:
    users = []
    with open(filepath, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(User(**row))
    return users

def save_users(filepath: str, users: List[User]):
    with open(filepath, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['username', 'hashed_password'])
        writer.writeheader()
        for user in users:
            writer.writerow(user.dict())

def get_user(filepath: str, username: str) -> Optional[User]:
    users = load_users(filepath)
    for user in users:
        if user.username == username:
            return user
    return None

def add_user(filepath: str, new_user: User):
    users = load_users(filepath)
    users.append(new_user)
    save_users(filepath, users)
