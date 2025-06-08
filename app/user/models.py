"""
File: app/user/models.py

Description:
MongoDB document model representation for users.
Used for structuring and accessing user documents in the database.
"""

from datetime import datetime
from typing import Literal, Optional
from pydantic import BaseModel, EmailStr, Field


class UserModel(BaseModel):
    """
    MongoDB user document structure.
    """
    email: EmailStr
    password_hash: str
    role: Literal["user", "admin", "superadmin"] = "user"
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True
