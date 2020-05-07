# Peyton

A lightweight framework for AWS Lambda for building Rest APIs

[![Codefresh build status]( https://g.codefresh.io/api/badges/pipeline/moonmoon1919/peyton%2Ftest?key=eyJhbGciOiJIUzI1NiJ9.NWIyYThiMjYzYmFlOGEwMDAxY2RiZWZh.5h81Od2ooleQPSDJ1tUbMIrDYzxsRi3ovMy-NHkYNdY&type=cf-2)]( https%3A%2F%2Fg.codefresh.io%2Fpipelines%2Ftest%2Fbuilds%3Ffilter%3Dtrigger%3Abuild~Build%3Bpipeline%3A5e0699826e1ebef7fcd37bf6~test)

![](https://media.giphy.com/media/PkFupNjqc4hpe/giphy.gif)

Currently Peyton supports
[v1.0 of the API Gateway Payload format](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html#http-api-develop-integrations-lambda.proxy-format) and has been tested with both HTTP and REST APIs.

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
        # Retrieve the body from the request
        body = router.current_request.body

        # Do something with the body

        resp = Response(status_code=201, headers={}, body={"message": "received PUT to index"})

        return resp.to_json()

    def post(self) -> ResponseObject:
        # Retrieve the body from the request
        body = router.current_request.body

        # Do something with the body

        resp = Response(status_code=201, headers={}, body={"message": "received POST to index"})

        return resp.to_json()

@router.register(path="/foo/{foo_id}/bar/{bar_id}")
class AllBars(ViewBase):
    def get(self, foo_id, bar_id) -> ResponseObject:
        resp = Response(status_code=200, headers={}, body={"foo_id": foo_id, "bar_id": bar_id, "message": "all bars by foo"},)

        return resp.to_json()

    def put(self, foo_id, bar_id) -> ResponseObject:
        # Retrieve the body from the request
        body = router.current_request.body

        # Do something with the body

        resp = Response(status_code=201, headers={}, body={"message": "received PUT to index"})

        return resp.to_json()

    def post(self, foo_id, bar_id) -> ResponseObject:
        # Retrieve the body from the request
        body = router.current_request.body

        # Do something with the body

        resp = Response(status_code=201, headers={}, body={"message": "received POST to index"})

        return resp.to_json()


def lambda_handler(event, context):
    request = Request(event)
    return router.dispatch(request=request)
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
- [x] Automatically decode base64 encoded input
- [x] Logging
- [x] In-Line Documentation
- [x] Unit Tests
- [x] Integration Tests
- [x] Style double check

---

Roadmap:
- [ ] Add support for Lambda behind ALB
