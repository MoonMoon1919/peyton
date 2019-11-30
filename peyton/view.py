"""Base class for Views."""

# Import our Response class
from response import Response, ResponseObject


class ViewBase:
    """Base class upon which all class based views are built upon."""

    def get(self, data: dict) -> ResponseObject:
        resp = Response(
            status_code=400, headers={}, body={"message": "Method not implemented"}
        )
        return resp.to_json()

    def post(self, data: dict) -> ResponseObject:
        resp = Response(
            status_code=400, headers={}, body={"message": "Method not implemented"}
        )
        return resp.to_json()

    def put(self, data: dict) -> ResponseObject:
        resp = Response(
            status_code=400, headers={}, body={"message": "Method not implemented"}
        )
        return resp.to_json()

    def patch(self, data: dict) -> ResponseObject:
        resp = Response(
            status_code=400, headers={}, body={"message": "Method not implemented"}
        )
        return resp.to_json()

    def delete(self, data: dict) -> ResponseObject:
        resp = Response(
            status_code=400, headers={}, body={"message": "Method not implemented"}
        )
        return resp.to_json()

    def dispatch(self, request_method, data):
        return getattr(self, request_method)(data)
