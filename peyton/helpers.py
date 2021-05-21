"""Module containing helper classes and functions for Peyton."""

from threading import Lock
from typing import Optional


class Singleton(type):
    """Thread safe Singleton base class."""

    # Ignore typing and flake issues here because of circular imports
    _instance: Optional["Router"] = None  # type: ignore # noqa
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        """Checks to ensure there is only one router instance."""
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__call__(*args, **kwargs)

        return cls._instance


def load_current_user(request_context) -> Optional[str]:
    """Load the current user from the request."""

    if (authorizer := request_context.get("authorizer")) is not None:
        claims = authorizer.get("claims", {})

        return claims.get("sub")

    return None
