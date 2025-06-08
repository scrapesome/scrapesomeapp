"""
File: app/user/schemas.py

Description:
Pydantic schemas for user registration, login, and response models.
"""

from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    """
    Schema for user registration or login input.
    """
    email: EmailStr
    password: str


class UserOut(BaseModel):
    """
    Schema for returning user details (excluding sensitive info).
    """
    email: EmailStr
    role: str
    is_active: bool
    created_at: datetime


class UserInDB(UserOut):
    """
    Internal schema with hashed password.
    """
    password_hash: str
