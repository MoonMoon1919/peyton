"""Class for responses."""

import base64
import json

# Import our type checkers
from peyton.type_checker import Dictionary, Integer, Boolean


class Response:
    """An object that represents a response from an API.

    Usage:
        After running your business logic and creating the body/message you want to return to your client
        Use this class to create a response object, then use to_json() to serialize the response

    Args:
        status_code: int = an HTTP Status Code
        headers: dict = a dictionary of headers
        body: dict = a dictionary, typically data
        base64_encode: bool = a flag that will base64 encode the body string passed in

    Raises:
        TypeError: If any objects type is incorrect according to class variable descriptors
    """

    body = Dictionary("body")
    headers = Dictionary("headers")
    multiValueHeaders = Dictionary("multiValueHeaders")
    statusCode = Integer("statusCode")
    isBase64Encoded = Boolean("isBase64Encoded")

    def __init__(
        self,
        status_code: int = 200,
        headers: dict = {},
        multiValueHeaders: dict = {},
        body: dict = {},
        base64_encode: bool = False,
    ):
        self.body = body
        self.headers = headers
        self.multiValueHeaders = multiValueHeaders
        self.statusCode = status_code
        self.isBase64Encoded = base64_encode

    def to_json(self) -> dict:
        """Generates responses."""
        resp_body = json.dumps(self.body)

        if self.isBase64Encoded:
            resp_body = base64.b64encode(resp_body.encode("ascii"))  # type: ignore

        response = {
            "body": resp_body,
            "headers": self.headers,
            "multiValueHeaders": self.multiValueHeaders,
            "statusCode": self.statusCode,
            "isBase64Encoded": self.isBase64Encoded,
        }

        return response
