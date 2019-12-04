"""Base class for Views."""

# Import our Response class
from response import Response, ResponseObject


class ViewBase:
    """Base class upon which all class based views are built upon."""

    def get(self, data: dict) -> ResponseObject:
        resp = Response(
            status_code=405, headers={}, body={"message": "Method not implemented"}
        )
        return resp.to_json()

    def post(self, data: dict) -> ResponseObject:
        resp = Response(
            status_code=405, headers={}, body={"message": "Method not implemented"}
        )
        return resp.to_json()

    def put(self, data: dict) -> ResponseObject:
        resp = Response(
            status_code=405, headers={}, body={"message": "Method not implemented"}
        )
        return resp.to_json()

    def patch(self, data: dict) -> ResponseObject:
        resp = Response(
            status_code=405, headers={}, body={"message": "Method not implemented"}
        )
        return resp.to_json()

    def delete(self, data: dict) -> ResponseObject:
        resp = Response(
            status_code=405, headers={}, body={"message": "Method not implemented"}
        )
        return resp.to_json()

    def dispatch(self, http_method: str, **kwargs):
        # Lower the http_method because it is all caps from API Gateway event
        http_method = http_method.lower()

        return getattr(self, http_method)(**kwargs)
