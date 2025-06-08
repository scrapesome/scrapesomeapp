"""
File: api_key/models.py

Description:
Defines the APIKey data model schema used to validate API key documents stored
in MongoDB. Uses Pydantic BaseModel for data validation and serialization.

Fields:
- key: Unique API key string assigned to the user.
- owner: Optional string representing the owner (e.g., email or username).
- active: Boolean flag indicating if the API key is active.
- created_at: Timestamp when the API key was created.
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class APIKeyModel(BaseModel):
    key: str = Field(..., description="Unique API key string")
    owner: Optional[str] = Field(None, description="Owner or subscriber identifier")
    active: bool = Field(True, description="Indicates if the API key is active")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Timestamp of key creation")
