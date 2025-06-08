"""
Main Application Entry Point
----------------------------

This module initializes the FastAPI application and includes core route configurations.

Features:
    - Creates an instance of the FastAPI app.
    - Includes default routes for health and status checks.
    - Tags routes for documentation grouping in Swagger UI.

Usage:
    Run this file using a WSGI/ASGI server like `uvicorn`:
    $ uvicorn main:app --reload
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.public.routes import default_router
from app.public.routes.documentation import documentation_router
from app.settings.config import Settings
# from app.middlewares.token_middleware import TokenMiddleware

settings = Settings()

# Create the FastAPI application instance
app = FastAPI(title=settings.app_name)


# app.add_middleware(middleware_class=TokenMiddleware)

# Include the default routes for health and status checks
app.include_router(router=default_router, tags=["health", "status"])

# Include the routes for documentation
app.include_router(router=documentation_router, tags=["documentation"])