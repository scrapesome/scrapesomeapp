"""
Token Middleware for FastAPI/Starlette Applications
---------------------------------------------------

This module defines a custom middleware class `TokenMiddleware` that handles
JWT-based authentication for incoming HTTP requests. It validates Bearer tokens,
extracts user roles and IDs, and ensures that only authorized users can access
protected routes.

Features:
- Skips authentication for public (unauthenticated) endpoints.
- Allows bypassing authentication in development, local, or test environments.
- Verifies JWT tokens using RS256 with a public key from environment variables.
- Injects `role` and `user_id` into the request state for downstream use.

Environment Variables Required:
- TOKEN_VALIDATION_PUBLIC_KEY: The RSA public key used to validate JWT tokens.
- public-endpoints: (Optional) Comma-separated paths that skip authentication.
- roles: (Optional) Comma-separated list of allowed roles.
- ENV: (Optional) The environment mode. In ["dev", "local", "test"], token validation is skipped.

Usage:
    Add `TokenMiddleware` to your FastAPI app via `add_middleware()`.
"""

import os
import logging
from dotenv import load_dotenv
from jwt import decode, PyJWTError
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from fastapi.responses import JSONResponse
from app.utils.string_utils import string_to_list
from app.settings.config import Settings

load_dotenv()
settings = Settings()

# Load the public key from environment variables
token_validation_public_key = settings.token_validation_public_key
if not token_validation_public_key:
    raise ValueError("TOKEN_VALIDATION_PUBLIC_KEY environment variable must be set")

# Middleware class to handle JWT validation for all incoming requests
class TokenMiddleware(BaseHTTPMiddleware):
    """
    Middleware to handle token-based authentication for FastAPI or Starlette apps.

    This middleware performs the following tasks:
    - Skips authentication for public endpoints.
    - Allows bypassing token validation in development, local, or test environments.
    - Validates a Bearer token from the Authorization header.
    - Extracts user roles and ID from the JWT token and stores them in the request state.
    - Rejects unauthorized users based on configured roles.

    Environment Variables:
        - public-endpoints: Comma-separated list of routes that bypass token validation.
        - roles: Comma-separated list of allowed roles for accessing protected routes.
        - ENV: Current environment (e.g., dev, local, test); skips validation if matched.

    Attributes:
        Inherits from BaseHTTPMiddleware.
    """

    async def dispatch(self, request: Request, call_next):
        """
        Intercepts incoming HTTP requests to enforce token-based access control.

        Parameters:
            request (Request): The incoming HTTP request.
            call_next (Callable): The next middleware or route handler in the chain.

        Returns:
            Response: Either a JSON error response or the response from the next handler.
        """
        # Get public endpoints from environment variable or use defaults
        public_endpoints = os.getenv("public-endpoints")
        if not public_endpoints:
            public_endpoints = ["/health", "/status"]
        public_endpoints = string_to_list(public_endpoints)

        # Skip token validation for public endpoints
        if any(request.url.path.startswith(endpoint.rstrip("/")) for endpoint in public_endpoints):
            return await call_next(request)


        # Bypass token validation in development/test environments
        if os.environ.get("ENV", "").lower() in ["dev", "local", "test"]:
            request.state.role = "local-user"
            return await call_next(request)

        # Extract the token from the Authorization header
        authorization = request.headers.get("Authorization")
        if not authorization:
            return JSONResponse(status_code=401, content={"error": "Token is missing"})

        if not authorization.startswith("Bearer "):
            return JSONResponse(status_code=401, content={"error": "Invalid token format"})

        token = authorization[len("Bearer "):]

        try:
            # Decode JWT token with public key (ensure 'token_validation_public_key' is defined elsewhere)
            payload = decode(token, token_validation_public_key, algorithms=["RS256"])

            # Extract role and user ID from the payload
            role = payload.get("extension_Roles")
            user_id = payload.get("user_id")

            # Check if the role is among allowed roles from the environment
            roles = os.getenv("roles")
            if not roles:
                roles = []
            roles = string_to_list(roles)

            if role not in roles:
                return JSONResponse(status_code=401,
                                    content={"error": "You are not allowed to use this API"})

            logging.info("Successfully verified token")

            # Store role and user_id in the request state for downstream access
            if role:
                request.state.role = role
            if user_id:
                request.state.user_id = user_id

        except PyJWTError as e:
            logging.error(str(e))
            return JSONResponse(status_code=401, content={"error": f"Token decode error: {str(e)}"})

        # Proceed to next handler
        response = await call_next(request)
        return response

