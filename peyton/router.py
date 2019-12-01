"""Router module for Petyon."""

from threading import Lock, Thread
from typing import Optional


class Singleton(type):
    """Thread safe Singleton base class."""

    _instance: Optional["Router"] = None
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        """Checks to ensure there is ONLY ONE router class."""
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__call__(*args, **kwargs)

        return cls._instance


class Router(metaclass=Singleton):
    """Router class that handles view registration and request dispatching"""

    routes: dict = {}

    def register(self, path: str):
        """A decorator function that registers a class as a view."""

        def decorator(_cls):
            """Adds the path and class to the routes dictionary."""

            self.routes[path] = _cls()

        return decorator

    def dispatch(self, event: dict):
        """Handles dispatching all requests made."""

        return self.routes[event["path"]].dispatch(
            http_method=event["httpMethod"], data=event
        )
