"""
Logging configuration for the Scrapesome application.

This module provides a centralized way to configure and retrieve a logger
that writes logs to a rotating file. It includes filename and line number 
in debug mode, and supports log level configuration via environment variables.
"""

import logging
from logging.handlers import RotatingFileHandler
from app.settings.config import Settings

def get_logger(name: str = "ScrapeSome") -> logging.Logger:
    """
    Create and return a logger with a rotating file handler.
    
    Args:
        name (str): Name of the logger. Default is "scrapesome".

    Returns:
        logging.Logger: Configured logger instance.
    """
    settings = Settings()

    logger = logging.getLogger(name)
    if logger.handlers:
        return logger  # Return existing logger if already configured

    log_level = settings.log_level.upper()
    log_file = settings.log_level

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=1)
    handler.setFormatter(formatter)

    logger.setLevel(log_level)
    logger.addHandler(handler)
    logger.propagate = False

    return logger

logger = get_logger()
