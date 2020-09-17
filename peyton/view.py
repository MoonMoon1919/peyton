"""Base class for Views."""

# Import our Response class
from peyton.response import Response, ResponseObject


class ViewBase:
    """Base class upon which all class based views are built upon.

    Usage:
        Subclass this class to create a view that contains your business logic.

        After creating your class and adding business logic you can register
        the class with the router you have created. When your lambda is invoked the event is
        loaded into a request object using the "resource" for path. The router calls its own dispatch method
        which will attempt to load a UrlRule. The UrlRule contains a reference to your class.
        From there the router dispatch method calls the View dispatch method, which, based on the HTTP method,
        will invoke the correct method containing your business logic.

    Returns:
        Dict: Returns the to_json() method of a response object (see response.py for all attributes)
              if a supported HTTP method verb does not exist
    """

    def get(self, **kwargs) -> ResponseObject:
        resp = Response(status_code=405, headers={}, body={"message": "Method not implemented"})
        return resp.to_json()

    def post(self, **kwargs) -> ResponseObject:
        resp = Response(status_code=405, headers={}, body={"message": "Method not implemented"})
        return resp.to_json()

    def put(self, **kwargs) -> ResponseObject:
        resp = Response(status_code=405, headers={}, body={"message": "Method not implemented"})
        return resp.to_json()

    def patch(self, **kwargs) -> ResponseObject:
        resp = Response(status_code=405, headers={}, body={"message": "Method not implemented"})
        return resp.to_json()

    def delete(self, **kwargs) -> ResponseObject:
        resp = Response(status_code=405, headers={}, body={"message": "Method not implemented"})
        return resp.to_json()

    def dispatch(self, http_method: str, **kwargs):
        # Lower the http_method because it is all caps from API Gateway event
        http_method = http_method.lower()

        func = getattr(self, http_method, None)

        # If a method is not implemented, return 405
        if func is None:
            return Response(status_code=405, headers={}, body={"message": "Method not implemented"}).to_json()

        return func(**kwargs)
