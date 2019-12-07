"""Peyton main entrypoint."""

"""
# Example:
from view import ViewBase
from response import Response, ResponseObject
from request import Request
from router import Router
from request import Request
import json

# Singleton
router = Router()


@router.register(path="/api-gateway-test/{id}/foo/{foo_id}")
class Index(ViewBase):
    def get(self, id, foo_id) -> ResponseObject:
        resp = Response(status_code=200, headers={}, body={"message": "received GET"},)

        return resp.to_json()

    def put(self, id, foo_id) -> ResponseObject:
        resp = Response(status_code=201, headers={}, body={"message": "received PUT"})

        return resp.to_json()

    def post(self, id, foo_id) -> ResponseObject:
        resp = Response(status_code=201, headers={}, body={"message": "received POST"})

        return resp.to_json()


# In this example, we're loading the event from a file
request = json.load(open("../example_json.json"))
request = Request(request)

print(router.dispatch(request))
"""
