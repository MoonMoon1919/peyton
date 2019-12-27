"""Module for testing Request module."""

import sys
from os import path
import json

from peyton.request import Request

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


def retrieve_fixture():
    j = json.load(open("./tests/fixtures/example_json.json"))
    return j


def snake_to_camel(snake_str):
    comp = snake_str.split("_")
    return comp[0] + "".join(x.title() for x in comp[1:])


def test_request_obj():
    """test request object."""
    data = retrieve_fixture()
    req = Request(data)

    assert req.body["foo"] == "bar"
    assert req.http_method == "GET"
    assert type(req.http_method) == str
    assert type(req.headers) == dict

    converted_dict = {}

    # Convert snake to camel case
    for k, v in req.__dict__.items():
        k = snake_to_camel(k)

        converted_dict[k] = v

    assert converted_dict == data