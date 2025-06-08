"""
File: app/user/route.py

Description:
User-related API endpoints for registration and login.
Routes utilize dependency injection for UserService, enabling clean separation of concerns
and easier unit testing.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from app.user.schemas import UserCreate
from app.user.service import UserService
from app.user.dependency import get_user_service

router = APIRouter(prefix="/users", tags=["User"])


@router.post("/register", status_code=201)
async def register_user(
    payload: UserCreate,
    user_service: UserService = Depends(get_user_service),
):
    """
    Registers a new user with the provided registration data.

    Args:
        payload (UserCreate): User registration data (email and password).
        user_service (UserService): Injected user service dependency.

    Returns:
        dict: Success message confirming user registration.

    Raises:
        HTTPException: Raises 400 if the user already exists.
    """
    try:
        return await user_service.register_user(payload)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/login")
async def login_user(
    payload: UserCreate,
    user_service: UserService = Depends(get_user_service),
):
    """
    Authenticates a user with login credentials.

    Args:
        payload (UserCreate): User login credentials (email and password).
        user_service (UserService): Injected user service dependency.

    Returns:
        dict: JWT access and refresh tokens, and token type.

    Raises:
        HTTPException: Raises 401 if credentials are invalid or user is inactive.
    """
    try:
        return await user_service.login_user(payload)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
