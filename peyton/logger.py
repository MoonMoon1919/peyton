"""Logging module for Peyton."""

from datetime import datetime
from functools import wraps
import logging
import os
import sys

logger = logging.getLogger("peyton")
logger.setLevel(logging.INFO)

default_handler = logging.StreamHandler(sys.stderr)
default_handler.setFormatter(logging.Formatter("%(message)s"))

# Create the logger
logger.addHandler(default_handler)


def log(fn):
    """A helper wrapper for."""

    @wraps(fn)
    def wrapper(*args, **kwargs):
        """."""
        resp = fn(*args, **kwargs)
        logger.info(
            {
                "client_ip": kwargs["request"].headers["X-Forwarded-For"],
                "request_time": kwargs["request"].request_context["requestTime"],
                "status": resp["statusCode"],
                "path": kwargs["request"].path,
                "http_user_agent": kwargs["request"].headers["User-Agent"],
                "http_method": kwargs["request"].http_method,
                "request_end": datetime.now().strftime("%d/%b/%Y:%H:%M:%S +0000"),
            }
        )

        return resp

    return wrapper
