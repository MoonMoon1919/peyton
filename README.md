# Peyton

A lightweight framework for AWS Lambda for building Rest APIs

![](https://media.giphy.com/media/PkFupNjqc4hpe/giphy.gif)

---
## How To
```python

from peyton.view import ViewBase
from peyton.response import Response, ResponseObject
from peyton.request import Request
from peyton.router import Router

router = Router()


@router.register(path="/")
class Index(ViewBase):
    def get(self) -> ResponseObject:
        resp = Response(status_code=200, headers={}, body={"message": "received GET to index"},)

        return resp.to_json()

    def put(self) -> ResponseObject:
        resp = Response(status_code=201, headers={}, body={"message": "received PUT to index"})

        return resp.to_json()

    def post(self) -> ResponseObject:
        resp = Response(status_code=201, headers={}, body={"message": "received POST to index"})

        return resp.to_json()

@router.register(path="/foo/{foo_id}/bar/{bar_id}")
class AllBars(ViewBase):
    def get(self, foo_id, bar_id) -> ResponseObject:
        resp = Response(status_code=200, headers={}, body={"foo_id": foo_id, "bar_id": bar_id, "message": "all bars by foo"},)

        return resp.to_json()

    def put(self, foo_id, bar_id) -> ResponseObject:
        resp = Response(status_code=201, headers={}, body={"message": "received PUT to index"})

        return resp.to_json()

    def post(self, foo_id, bar_id) -> ResponseObject:
        resp = Response(status_code=201, headers={}, body={"message": "received POST to index"})

        return resp.to_json()


def lambda_handler(event, context):
    request = Request(event)
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
- [ ] Re-implement url map to use radix trie
- [ ] Logging
- [ ] In-Line Documentation
- [ ] Unit Tests
- [x] Integration Tests
- [ ] Style double check
- [ ] Documentation

---

Logging:
- Log all requests with the following:
 - Requesting IP
 - Request Method
 - Endpoint
 - Request Time
 - URL
 - Message
 - HTTP Method
