"""Class for responses."""

from typing import TypedDict
import json

# Import our type checkers
from type_checker import Dictionary, Integer


class ResponseObject(TypedDict):
    """
    This is here exclusively for type hinting for HTTP Verb function outputs.
    """

    body: dict
    headers: dict
    status_code: int


class Response:
    body = Dictionary("body")
    headers = Dictionary("headers")
    statusCode = Integer("statusCode")

    def __init__(
        self, status_code: int = None, headers: dict = None, body: dict = None
    ):
        self.body = body
        self.headers = headers
        self.statusCode = status_code

    def to_json(self) -> dict:
        """Generates responses."""
        response = {
            "body": json.dumps(self.body),
            "headers": self.headers,
            "statusCode": self.statusCode,
        }

        return response
