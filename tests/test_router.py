"""."""

import sys
from os import path
import json

from peyton.router import Router, UrlRule
from peyton.view import ViewBase
from peyton.response import Response
from peyton.request import Request

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


def retrieve_fixture():
    j = json.load(open("./tests/fixtures/example_json.json"))
    return j


def prepare_router():
    """Dummy helper for router tests"""
    router = Router()

    @router.register("/")
    class BasicIndex(ViewBase):
        def get(self):
            resp = Response(
                status_code=200, headers={}, body={"message": "received GET"}
            )

            return resp.to_json()

    @router.register("/foo/{foo_id}")
    class FooById(ViewBase):
        def put(self, foo_id):
            resp = Response(
                status_code=200, headers={}, body={"message": "received PUT"}
            )

            return resp.to_json()

        def post(self, foo_id):
            resp = Response(
                status_code=201,
                headers={},
                body={
                    "message": "received the following data %s"
                    % router.current_request.body
                },
            )

            return resp.to_json()

    @router.register("/foo/{foo_id}/bar/{bar_id}")
    class BarIdByFoo(ViewBase):
        def put(self, foo_id, bar_id):
            resp = Response(
                status_code=200, headers={}, body={"message": "received PUT"}
            )

            return resp.to_json()

    return router


def test_singleton():
    """Test that singleton for Router works."""
    r1 = Router()
    r2 = Router()

    assert r1 == r2


def test_class_registration():
    """Test route registration."""
    router = prepare_router()

    assert router.routes["/"].endpoint == "basicindex"
    assert router.routes["/"].view_cls.__name__ == "BasicIndex"

    assert router.routes["/foo/{foo_id}"].path_params == ["foo_id"]
    assert router.routes["/foo/{foo_id}"].path == "/foo/{foo_id}"


def test_route_execution():
    """Test execution of view class + http method."""
    router = prepare_router()

    assert router.routes["/"].view_cls().get()["body"] == '{"message": "received GET"}'
    assert (
        router.routes["/foo/{foo_id}"].view_cls().put(1)["body"]
        == '{"message": "received PUT"}'
    )


def test_route_does_not_exist():
    """Tests for a route that does not exist."""
    req = retrieve_fixture()
    req = Request(req)

    router = prepare_router()
    resp = router.dispatch(request=req)

    assert resp == {
        "statusCode": 404,
        "headers": {},
        "multiValueHeaders": {},
        "body": '{"message": "Endpoint not found"}',
        "isBase64Encoded": False,
    }


def test_dispatch():
    """Test dispatch method."""
    req = retrieve_fixture()
    req = Request(req)
    req.resource = "/"
    req.path = "/"

    router = prepare_router()
    resp = router.dispatch(request=req)

    assert resp == {
        "statusCode": 200,
        "headers": {},
        "multiValueHeaders": {},
        "body": '{"message": "received GET"}',
        "isBase64Encoded": False,
    }


def test_path_params():
    """Tests to ensure path params are created from path."""
    router = prepare_router()

    route = router.routes["/foo/{foo_id}/bar/{bar_id}"]
    assert route.path_params == ["foo_id", "bar_id"]


def test_dispatch_with_params():
    """Test dispatch method with parameters."""
    req = retrieve_fixture()

    # Modify the request object for scope of test
    req = Request(req)
    req.resource = "/foo/{foo_id}"
    req.path = "/foo/{foo_id}"
    req.path_parameters = {"foo_id": 2}
    req.http_method = "PUT"

    router = prepare_router()
    resp = router.dispatch(request=req)

    assert resp == {
        "statusCode": 200,
        "headers": {},
        "multiValueHeaders": {},
        "body": '{"message": "received PUT"}',
        "isBase64Encoded": False,
    }


def test_dispatch_with_body():
    req = retrieve_fixture()

    req = Request(req)
    req.resource = "/foo/{foo_id}"
    req.path = "/foo/{foo_id}"
    req.path_parameters = {"foo_id": 2}
    req.http_method = "POST"

    router = prepare_router()
    resp = router.dispatch(request=req)

    assert resp == {
        "body": "{\"message\": \"received the following data {'foo': 'bar'}\"}",
        "headers": {},
        "multiValueHeaders": {},
        "statusCode": 201,
        "isBase64Encoded": False,
    }
