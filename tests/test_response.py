"""."""

import sys
from os import path
import json
import base64

import pytest

from peyton.response import Response

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


def test_response_obj():
    resp = Response(status_code=200, headers={}, body={"message": "received GET"})
    j = resp.to_json()

    assert resp.statusCode == 200
    assert type(resp.statusCode) == int

    assert resp.headers == {}
    assert type(resp.headers) == dict

    assert resp.isBase64Encoded == False
    assert type(resp.isBase64Encoded) == bool

    assert resp.body["message"] == "received GET"
    assert type(resp.body) == dict

    # Test output of to_json()
    assert type(j["body"]) == str


def test_body_type():
    """Tests that response object balks on improper type for body."""
    with pytest.raises(TypeError):
        resp = Response(status_code=200, headers={}, body="hello world")


def test_status_code_type():
    """Tests that response object balks on improper type for status_code."""
    with pytest.raises(TypeError):
        resp = Response(status_code="foo", headers={}, body={"message": "received GET"})


def test_base64_encoding():
    resp = Response(
        status_code=200,
        headers={},
        body={"message": "received GET"},
        base64_encode=True,
    )

    resp = resp.to_json()

    assert resp["body"] == b"eyJtZXNzYWdlIjogInJlY2VpdmVkIEdFVCJ9"
