"""
API Routes for Documentation
------------------------------------------------

This module defines API endpoints for documentation.

Routes:
    - GET /documentation        : Documentation Page.

These endpoints are typically excluded from authentication in middleware
"""

from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from app.settings.config import Settings

settings = Settings()

documentation_router = APIRouter()

@documentation_router.get("/documentation")
async def documentation():
    """
    Documentation path handler.
    """
    documentation_redirect_url = settings.documentation_redirect_url
    return RedirectResponse(url=documentation_redirect_url)
