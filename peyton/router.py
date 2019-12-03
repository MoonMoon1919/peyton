"""Router module for Petyon."""

from helpers import Singleton


class Router(metaclass=Singleton):
    """Router class that handles view registration and request dispatching"""

    routes: dict = {}

    def register(self, path: str):
        """A decorator function that registers a class as a view."""

        def decorator(_cls):
            """Adds the path and class to the routes dictionary."""

            self.routes[path] = _cls()

        return decorator

    def dispatch(self, request: dict):
        """Handles dispatching all requests made."""

        return self.routes[request.path].dispatch(
            http_method=request.http_method, data=request
        )
