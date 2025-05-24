"""
Environment configuration loader for the Scrapesome application.

This module defines a `Settings` class that loads all required environment
variables at startup and makes them available as attributes.

Raises:
    EnvironmentError: If a required environment variable is missing.
"""

import os
import logging

class Settings:
    """
    Loads and stores all required environment variables for the application.
    """

    def __init__(self) -> None:
        #🔧 General App Settings
        self.env = self._get("ENV", default="development")

        self.app_name = self._get("APP_NAME", default="ScrapeSome")
        self.app_version = self._get("APP_VERSION", default="0.0.1")

        #🛢️ Database Config
        self.database_url = self._get("DATABASE_URL", default="")

        #🌐 API Configuration
        self.host = self._get("HOST", default="0.0.0.0")
        self.port = self._get("PORT", default="8000")

        # APP Configuration
        self.log_level = self._get("LOG_LEVEL", default="INFO")

        #📂 File Paths
        self.log_file = self._get("LOG_FILE", default="app/app.log")

        #🛡️ Security
        self.access_token_expire_minutes = self._get("ACCESS_TOKEN_EXPIRE_MINUTES", default="60")
        self.token_validation_secret_key = self._get("TOKEN_VALIDATION_SECRET_KEY", default="")

        #⚙️ Scraper Behavior Settings
        self.max_workers = self._get("MAX_WORKERS", default="1")

        #📤 Output Format Defaults
        self.default_export_format = self._get("EXPORT_FORMAT", default="text")


    def _get(self, key: str, default: str | None = None) -> str:
        """
        Retrieve an environment variable, or raise an error if missing and no default is provided.

        Args:
            key (str): The name of the environment variable.
            default (Optional[str]): Default value if the variable is not set.

        Returns:
            str: The value of the environment variable.

        Raises:
            EnvironmentError: If the variable is not set and no default is provided.
        """
        value = os.getenv(key)
        if value is None:
            if default is not None:
                logging.warning("[Config] Environment variable '%s' not set, using default: '%s'", key, default)
                return default
            raise EnvironmentError(f"Missing required environment variable: '{key}'")
        return value
