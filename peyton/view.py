"""Base class for Views."""

from response import Response


class ViewBase:
    """Base class upon which all class based views are built upon."""

    def get(self, data):
        resp = Response(
            status_code=400, headers={}, body={"message": "Method not implemented"}
        )
        return resp.to_json()

    def post(self, data):
        resp = Response(
            status_code=400, headers={}, body={"message": "Method not implemented"}
        )
        return resp.to_json()

    def put(self, data):
        resp = Response(
            status_code=400, headers={}, body={"message": "Method not implemented"}
        )
        return resp.to_json()

    def patch(self, data):
        resp = Response(
            status_code=400, headers={}, body={"message": "Method not implemented"}
        )
        return resp.to_json()

    def delete(self, data):
        resp = Response(
            status_code=400, headers={}, body={"message": "Method not implemented"}
        )
        return resp.to_json()

    def dispatch(self, request_method, data):
        return getattr(self, request_method)(data)
