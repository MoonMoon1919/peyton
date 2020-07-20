"""Module containing helper classes and functions for Peyton."""

from threading import Lock, Thread
from typing import Optional


class Singleton(type):
    """Thread safe Singleton base class."""

    _instance: Optional["Router"] = None
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        """Checks to ensure there is only one router instance."""
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__call__(*args, **kwargs)

        return cls._instance
