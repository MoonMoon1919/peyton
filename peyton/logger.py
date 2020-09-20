"""Logging module for Peyton."""

from functools import wraps
import logging

logger = logging.getLogger("peyton")
logger.setLevel(logging.INFO)


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
                "request_id": kwargs["request"].request_context["requestId"],
                "extended_request_id": kwargs["request"].request_context["extendedRequestId"],
            }
        )

        return resp

    return wrapper
