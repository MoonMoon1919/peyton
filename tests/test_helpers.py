"""Module for testing utilities."""

import json
import sys
from os import path

from peyton.helpers import load_current_user

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


def retrieve_fixture():
    j = json.load(open("./tests/fixtures/request_context.json"))
    return j


def test_load_current_user():
    """Test loading the user from the authorizer field."""
    request_context = retrieve_fixture()
    current_user = load_current_user(request_context=request_context)

    assert current_user == "qqqqqqqq-wwww-eeee-rrrr-ttttttyyyyyy"


def test_load_current_user_no_authorizer():
    """Test to ensure an error isn't thrown if the authorizer field is not present."""
    request_context = retrieve_fixture()
    del request_context["authorizer"]
    current_user = load_current_user(request_context=request_context)

    assert current_user is None


def test_load_current_user_no_claims():
    """Test to ensure an error isn't thrown if the claims field is not present in authorizer."""
    request_context = retrieve_fixture()
    del request_context["authorizer"]["claims"]
    current_user = load_current_user(request_context=request_context)

    assert current_user is None
