"""
File: settings/db_config.py

Description:
MongoDB connection utility using Motor. Provides a shared AsyncIOMotorClient
instance with connection pooling configured. Ensures explicit database selection.
"""

from motor.motor_asyncio import AsyncIOMotorClient
from app.settings.config import Settings

settings = Settings()

_client = None


def get_mongo_client() -> AsyncIOMotorClient:
    """
    Returns a cached MongoDB client to reuse across requests.
    Configured with connection pool options to limit max open connections.

    Returns:
        AsyncIOMotorClient: Motor client instance
    """
    global _client
    if _client is None:
        MONGO_URI = settings.database_url
        _client = AsyncIOMotorClient(
            MONGO_URI,
            maxPoolSize=int(settings.database_max_pool_size),       # max simultaneous connections
            minPoolSize=int(settings.database_min_pool_size),        # minimum number of connections to keep
            maxIdleTimeMS=int(settings.database_idle_time)  # close idle connections
        )
    return _client


def get_database():
    """
    Returns the MongoDB database object for the configured database name.

    Returns:
        Database: Motor Database instance
    """
    client = get_mongo_client()
    # Explicitly select database if your URI does not contain it
    db_name = settings.database_name
    return client[db_name]
