"""Class for responses."""

from types import Dictionary, Integer


class Response:
    body = Dictionary("body")
    headers = Dictionary("headers")
    status_code = Integer("status_code")

    def __init__(self, status_code=None, headers=None, body=None):
        self.body = body
        self.headers = headers
        self.status_code = status_code

    def to_json(self):
        """Generates responses."""
        response = {
            "body": self.body,
            "headers": self.headers,
            "status_code": self.status_code,
        }

        return response
