"""."""

import json
import sys
from os import path

from peyton.response import Response
from peyton.router import Router
from peyton.view import ViewBase

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


def prepare_router():
    """Dummy helper for router tests"""
    router = Router()

    @router.register("/")
    class BasicIndex(ViewBase):
        def get(self):
            resp = Response(status_code=200, headers={}, body={"message": "received GET"})

            return resp.to_json()

    @router.register("/foo/{foo_id}")
    class FooById(ViewBase):
        def put(self, foo_id):
            resp = Response(status_code=200, headers={}, body={"message": "received PUT"})

            return resp.to_json()

    return router


def test_2xx_view_dispatch():
    """Checks for 200 response from dispatched HTTP method named methods."""
    router = prepare_router()
    view_cls = router.routes["/"]
    view_cls = view_cls.view_cls()

    resp = view_cls.dispatch("GET")

    assert resp == {
        "statusCode": 200,
        "headers": {},
        "multiValueHeaders": {},
        "body": '{"message": "received GET"}',
        "isBase64Encoded": False,
    }


def test_405_view_dispatch():
    """Checks for 405 response from dispatched HTTP method named methods where they dont exist."""
    router = prepare_router()
    view_cls = router.routes["/"]
    view_cls = view_cls.view_cls()

    resp = view_cls.dispatch("DELETE")

    assert resp == {
        "statusCode": 405,
        "headers": {},
        "multiValueHeaders": {},
        "body": '{"message": "Method not implemented"}',
        "isBase64Encoded": False,
    }
