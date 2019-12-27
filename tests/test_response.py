"""."""

import sys
from os import path
import json

from peyton.response import Response

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


def test_response_obj():
    resp = Response(status_code=200, headers={}, body={"message": "received GET"})
    j = resp.to_json()

    assert resp.statusCode == 200
    assert resp.headers == {}
    assert resp.isBase64Encoded == False
    assert resp.body["message"] == "received GET"
    assert type(j["body"]) == str
