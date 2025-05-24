"""
Default API Routes for Health and Status Checks
------------------------------------------------

This module defines default API endpoints for system diagnostics and fallback behavior.

Routes:
    - GET /        : Root Path or HomePage.
    - GET /heath   : Returns a simple health check response.
    - GET /status  : Returns a basic status response.

These endpoints are typically excluded from authentication in middleware
(e.g., for health probes or uptime checks).
"""

from fastapi import APIRouter
from fastapi.responses import RedirectResponse

default_router = APIRouter()

@default_router.get("/")
async def root():
    """
    Default root path handler.
    """
    return RedirectResponse(url="/documentation")


@default_router.get("/health")
async def health():
    """
    Health check endpoint.

    This route is used to confirm the server is up and running.
    It can be used by load balancers or uptime monitors.

    Returns:
        dict: A JSON response indicating the health status of the server.
    """
    return {"health": "Good"}


@default_router.get("/status")
async def status():
    """
    Status check endpoint.

    Provides basic status information for service availability checks.

    Returns:
        dict: A JSON response indicating the operational status of the server.
    """
    return {"status": "Ok"}
