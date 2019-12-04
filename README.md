# Peyton

A lightweight framework for AWS Lambda for building Rest APIs

![](https://media.giphy.com/media/PkFupNjqc4hpe/giphy.gif)

---
## How To
```python

from peyton import router
from peyton.view import ViewBase
from peyton.response import Response, ResponseObject
from peyton.request import Request


@router.register(path="/")
class Index(ViewBase):
    def get(self) -> ResponseObject:
        resp = Response(status_code=200, headers={}, body={"message": "hello world!"})

        return resp.to_json()


@router.register(path="/foo/{id}/bar/{foo_id}")
class AllBarsByFoo(ViewBase):
    def get(self, id, foo_id) -> ResponseObject:
        resp = Response(status_code=200, headers={}, body={"message": "received GET"},)

        return resp.to_json()

    def delete(self, id, foo_id) -> ResponseObject:
        resp = Response(status_code=202, headers={}, body={"message": "received PUT"})

        return resp.to_json()

    def post(self, id, foo_id) -> ResponseObject:
        resp = Response(status_code=201, headers={}, body={"message": "received POST"})

        return resp.to_json()


def handler(event, context):
    request = Request(request)
    return router.dispatch(request)
```

---

MVP:
- [x] Class based views
- [x] Dispatched HTTP verbs
- [x] Ability to specify path per view
- [x] Serialized responses to json
- [x] Include HTTP Status Code + Headers in response
- [x] Class that turns API Gateway event into python object
- [x] Ability to specify variables for endpoints
- [x] Class for URL rules
- [ ] In-Line Documentation
- [ ] Unit Tests
- [ ] Integration Tests
- [ ] Style double check
- [ ] Documentation
- [ ] Readme Refresh
