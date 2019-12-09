"""Class for responses."""

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
        is_base64_encoded: bool = False,
    ):
        self.body = body
        self.headers = headers
        self.statusCode = status_code
        self.isBase64Encoded = is_base64_encoded

    def to_json(self) -> dict:
        """Generates responses."""
        # TO DO: make body json.dump() optional since just a regular string should be supported as well

        response = {
            "body": json.dumps(self.body),
            "headers": self.headers,
            "statusCode": self.statusCode,
            "isBase64Encoded": self.isBase64Encoded,
        }

        return response
