"""Base class for Views."""

# Import our Response class
from peyton.response import Response, ResponseObject


class ViewBase:
    """Base class upon which all class based views are built upon."""

    def get(self, **kwargs) -> ResponseObject:
        resp = Response(
            status_code=405, headers={}, body={"message": "Method not implemented"}
        )
        return resp.to_json()

    def post(self, **kwargs) -> ResponseObject:
        resp = Response(
            status_code=405, headers={}, body={"message": "Method not implemented"}
        )
        return resp.to_json()

    def put(self, **kwargs) -> ResponseObject:
        resp = Response(
            status_code=405, headers={}, body={"message": "Method not implemented"}
        )
        return resp.to_json()

    def patch(self, **kwargs) -> ResponseObject:
        resp = Response(
            status_code=405, headers={}, body={"message": "Method not implemented"}
        )
        return resp.to_json()

    def delete(self, **kwargs) -> ResponseObject:
        resp = Response(
            status_code=405, headers={}, body={"message": "Method not implemented"}
        )
        return resp.to_json()

    def dispatch(self, http_method: str, **kwargs):
        # Lower the http_method because it is all caps from API Gateway event
        http_method = http_method.lower()

        func = getattr(self, http_method, None)

        # If a method is not implemented, return 405
        if func is None:
            return Response(
                status_code=405, headers={}, body={"message": "Method not implemented"}
            ).to_json()

        return func(**kwargs)
