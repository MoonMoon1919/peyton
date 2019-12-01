"""Class for responses."""

from typing import TypedDict

# Import our type checkers
from type_checker import Dictionary, Integer


class ResponseObject(TypedDict):
    body: dict
    headers: dict
    status_code: int


class Response:
    body = Dictionary("body")
    headers = Dictionary("headers")
    status_code = Integer("status_code")

    def __init__(
        self, status_code: int = None, headers: dict = None, body: dict = None
    ):
        self.body = body
        self.headers = headers
        self.status_code = status_code

    def to_json(self) -> dict:
        """Generates responses."""
        response = {
            "body": self.body,
            "headers": self.headers,
            "status_code": self.status_code,
        }

        return response
