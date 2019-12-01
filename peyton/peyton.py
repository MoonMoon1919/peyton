"""Peyton main entrypoint."""

from router import Router


# Singleton
router = Router()

"""
Example:

from view import ViewBase
from response import Response


@router.register(path="/")
class Index(ViewBase):
    def get(self, data):
        resp = Response(status_code=200, headers={}, body={"message": "Stuff!"})

        return resp.to_json()

    def put(self, data):
        print("put from index")

    def post(self, data):
        print("post from index")


# a very basic stripped down event
event = {"httpMethod": "GET", "path": "/"}

print(router.dispatch(event))
"""
