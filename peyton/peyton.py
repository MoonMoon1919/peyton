"""Peyton main entrypoint."""

from router import Router


# Singleton
router = Router()

"""
Example:

from peyton.view import ViewBase

@router.register(path="/")
class Index(ViewBase):
    def get(self, data):
        print("get from index")

    def put(self, data):
        print("put from index")

    def post(self, data):
        print("post from index")


# a very basic stripped down event
event = {"httpMethod": "DELETE", "path": "/"}

print(router.dispatch(event))
"""
