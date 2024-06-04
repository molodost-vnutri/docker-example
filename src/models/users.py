from pydantic import BaseModel, EmailStr
from typing import Union, Optional


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserBase(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserAuth(BaseModel):
    email: EmailStr
    password: str
