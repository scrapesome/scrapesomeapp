"""
File: app/user/dependency.py

Description:
Dependency injector for UserService with MongoDB client.
"""

from fastapi import Depends
from app.settings.db_config import get_mongo_client
from app.user.service import UserService


def get_user_service() -> UserService:
    """
    Provides a UserService instance with MongoDB client injected.

    Returns:
        UserService
    """
    db_client = get_mongo_client()
    return UserService(db_client)
