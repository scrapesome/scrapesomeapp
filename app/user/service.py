"""
File: app/user/service.py

Description:
User business logic including DB operations with MongoDB.
"""

from motor.motor_asyncio import AsyncIOMotorClient
from app.utils.auth_utils import hash_password, verify_password
from app.common.jwt import create_access_token, create_refresh_token
from app.user.schemas import UserCreate
from pymongo.errors import DuplicateKeyError


class UserService:
    """
    Service for user operations.
    """

    def __init__(self, db_client: AsyncIOMotorClient):
        self.users = db_client["scrapesome"]["users"]
        # Ensure index for unique email
        self.users.create_index("email", unique=True)

    async def register_user(self, payload: UserCreate) -> dict:
        hashed_pw = hash_password(payload.password)
        user_doc = {
            "email": payload.email,
            "password_hash": hashed_pw,
            "role": "user",
            "is_active": True,
            "created_at": payload.created_at if hasattr(payload, "created_at") else None,
        }
        try:
            await self.users.insert_one(user_doc)
            return {"message": "User registered successfully."}
        except DuplicateKeyError:
            raise ValueError("User already exists.")

    async def login_user(self, payload: UserCreate) -> dict:
        user = await self.users.find_one({"email": payload.email})
        if not user:
            raise ValueError("User not found.")
        if not verify_password(payload.password, user["password_hash"]):
            raise ValueError("Invalid credentials.")
        if not user["is_active"]:
            raise ValueError("User is inactive.")

        user_data = {"sub": str(user["_id"]), "role": user["role"]}
        return {
            "access_token": create_access_token(user_data),
            "refresh_token": create_refresh_token(user_data),
            "token_type": "bearer"
        }
