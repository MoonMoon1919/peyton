"""Router module for Petyon."""

from peyton.helpers import Singleton
from peyton.logger import log
from peyton.response import Response


class Router(metaclass=Singleton):
    """Router object that handles view registration and request dispatching.

    Usage:
        The most common usage is to create a router object then use the register method
        to register classes to a path

        router = Router()

        @router.register("/")
        class BasicIndex(ViewBase):
            def get(self):
                resp = Response(
                    status_code=200, headers={}, body={"message": "received GET"}
                )

                return resp.to_json()

        When a request is received, load the request into a Request object (see request.py)
        then pass it into the dispatch method of the router to call the class and specific verb based method
        req = Request(event)

        resp = router.dispatch(req)

        return resp
    Args:
        None

    Raises:
        None
    """

    routes: dict = {}

    def __init__(self):
        self.current_request = None

    def register(self, path: str):
        """A decorator function that registers a class as a view."""

        def decorator(_cls):
            """Adds the path and class to the routes dictionary."""
            self.routes[path] = UrlRule(path, _cls)

        return decorator

    @log
    def dispatch(self, request: dict = None):
        """Handles dispatching all requests made."""
        self.current_request = request

        resource = self.routes.get(request.resource, None)

        # Account for the possibility of a resource not being registered
        if resource is None:
            return Response(status_code=404, headers={}, body={"message": "Endpoint not found"}).to_json()

        # Create an empty dict for kwargs
        # TO DO: Test the speed of this, it might be slow
        kwargs = {}

        # Dont iterate if there are no path parameters
        if resource.path_params:
            for item in resource.path_params:
                kwargs[item] = request.path_parameters[item]

        # Instantiate the view class
        # This is done here to ensure each request has it's own instance
        view = resource.view_cls()

        # Call the dispatch method of the view class
        # This method is defined in view.py
        return view.dispatch(http_method=request.http_method, **kwargs)


class UrlRule:
    """Class that defines URL rules."""

    def __init__(self, path=None, view_cls=None):
        self.path = path
        self.endpoint = view_cls.__name__.lower()
        self.view_cls = view_cls
        self.path_params = self._parse_path_params()

    def _parse_path_params(self) -> list:
        """
        Helper method to create a list of path_params.
        The path_params are used when a url is called to retrieve the values from the request object.
        See request.py to see how this is populated
        """
        remove = ["{", "}"]
        path_params = []

        # Split the path to parse params
        path_splitter = self.path.split("/")

        # Account for index views on "/" where split returns ["", ""]
        if all(item == "" for item in path_splitter):
            return path_params

        # Parse all params and append
        for param in path_splitter[1:]:
            param = list(param)
            if param[1] and param[-1] in remove:

                path_params.append("".join(param[1:-1]))

        return path_params
