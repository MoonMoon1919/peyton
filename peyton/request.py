"""Module that contains classes for turning a request event into a python object."""

from functools import reduce
import base64
import json

# Import our type checkers
from peyton.type_checker import String, List, Dictionary, Boolean


class Request:
    # TO DO: Figure out how to handle multiple types for these..
    body = Dictionary("body")
    resource = String("resource")
    path = String("path")
    http_method = String("http_method")
    is_base64_encoded = Boolean("is_base64_encoded")
    query_string_parameters = Dictionary("query_string_parameters")
    multi_value_query_string_parameters = Dictionary(
        "multi_value_query_string_parameters"
    )
    path_parameters = Dictionary("path_parameters")
    stage_variables = Dictionary("stage_variables")
    headers = Dictionary("headers")
    multi_value_headers = Dictionary("multi_value_headers")
    request_context = Dictionary("request_context")

    def __init__(self, event):
        # Automatically decode the body if its base64 encoded
        # We do this before variable assignment to prevent type errors
        # First we check if the element exists
        if event.get("isBase64Encoded", False):
            if event["isBase64Encoded"]:
                event["body"] = json.loads(
                    base64.b64decode(event["body"]).decode("utf-8")
                )

        for k, v in event.items():
            k = reduce(lambda x, y: x + ("_" if y.isupper() else "") + y, k).lower()
            setattr(self, k, v)
