"""Class for responses."""

import base64
from typing import TypedDict
import json

# Import our type checkers
from peyton.type_checker import Dictionary, Integer, Boolean


class ResponseObject(TypedDict):
    """
    This is here exclusively for type hinting for HTTP Verb function outputs.
    """

    body: str  # serialized string
    headers: dict
    status_code: int
    isBase64Encoded: bool


class Response:
    body = Dictionary("body")
    headers = Dictionary("headers")
    statusCode = Integer("statusCode")
    isBase64Encoded = Boolean("isBase64Encoded")

    def __init__(
        self,
        status_code: int = 200,
        headers: dict = {},
        body: dict = {},
        base64_encode: bool = False,
    ):
        self.body = body
        self.headers = headers
        self.statusCode = status_code
        self.isBase64Encoded = base64_encode

    def to_json(self) -> dict:
        """Generates responses."""
        # TO DO: make body json.dump() optional since just a regular string should be supported as well

        resp_body = json.dumps(self.body)

        if self.isBase64Encoded:
            resp_body = base64.b64encode(resp_body.encode("ascii"))

        response = {
            "body": resp_body,
            "headers": self.headers,
            "statusCode": self.statusCode,
            "isBase64Encoded": self.isBase64Encoded,
        }

        return response
