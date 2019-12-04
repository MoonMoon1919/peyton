"""Peyton main entrypoint."""

from router import Router
from request import Request


# Singleton
router = Router()
"""
# Example:

from view import ViewBase
from response import Response
from request import Request
import json
from base64 import b64decode


@router.register(path="/api-gateway-test/{id}/foo/{foo_id}")
class Index(ViewBase):
    def get(self, data):
        resp = Response(status_code=200, headers={}, body={"message": data.body},)

        return resp.to_json()

    def put(self, id, foo_id):
        resp = Response(status_code=201, headers={}, body={"message": "received"})

        return resp.to_json()

    def post(self, id, foo_id):
        resp = Response(status_code=201, headers={}, body={"message": "received"})

        return resp.to_json()


# In this example, we're loading the event from a file
request = json.load(open("../example_json.json"))
request = Request(request)

print(router.dispatch(request))
"""
