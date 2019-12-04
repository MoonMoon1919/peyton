"""Router module for Petyon."""

from helpers import Singleton


class Router(metaclass=Singleton):
    """Router class that handles view registration and request dispatching"""

    routes: dict = {}

    def register(self, path: str):
        """A decorator function that registers a class as a view."""

        def decorator(_cls):
            """Adds the path and class to the routes dictionary."""
            self.routes[path] = {}

            remove = ["{", "}"]
            path_params = []

            path_splitter = path.split("/")
            for param in path_splitter[1:]:
                param = list(param)
                if param[1] and param[-1] in remove:

                    path_params.append("".join(param[1:-1]))

            self.routes[path]["func"] = _cls()
            self.routes[path]["path_params"] = path_params

        return decorator

    def dispatch(self, request: dict):
        """Handles dispatching all requests made."""
        resource = self.routes[request.resource]
        kwargs = {}

        # TO DO: Find a more efficient way to handle this
        for item in resource["path_params"]:
            kwargs[item] = request.path_parameters[item]

        return resource["func"].dispatch(http_method=request.http_method, **kwargs)
