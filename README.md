# Peyton

A lightweight framework for AWS Lambda for building Rest APIs.

Peyton is designed to be as small as possible, with no requirements outside of the standard python library. It allows developers to create and deploy serverless applications easily.

[![Codefresh build status]( https://g.codefresh.io/api/badges/pipeline/moonmoon1919/peyton%2Ftest?key=eyJhbGciOiJIUzI1NiJ9.NWIyYThiMjYzYmFlOGEwMDAxY2RiZWZh.5h81Od2ooleQPSDJ1tUbMIrDYzxsRi3ovMy-NHkYNdY&type=cf-2)]( https%3A%2F%2Fg.codefresh.io%2Fpipelines%2Ftest%2Fbuilds%3Ffilter%3Dtrigger%3Abuild~Build%3Bpipeline%3A5e0699826e1ebef7fcd37bf6~test)

![](https://media.giphy.com/media/PkFupNjqc4hpe/giphy.gif)

Currently Peyton supports
[v1.0 of the API Gateway Payload format](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html#http-api-develop-integrations-lambda.proxy-format) and has been tested with both HTTP and REST APIs.


Peyton is being used in pre-production and is stable. However, the project is in it's pre-1.0 state and may change quickly. The author(s) will note breaking changes for releases, when necessary.

---

## Dependencies

Peyton has no dependencies outside of the Python standard library.

<sup>Note: Pipenv is used for local development and CI only.</sup>

---

## How To

At this time Peyton only supports class based views, using HTTP verbs as method names. In practice class based views prove to be generally easy to reason about and encourage organization within a codebase.

At a minimum you must do three things to use Peyton:
- Instantiate the `Router` class
- Define a new class that subclasses Peyton's `ViewClass`
- Add the `register` decorator to the class, specifying the path to be used

Below is a simple example of an API definition with two views (routes).

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

# Performance

Performance is a top priority of this project. The total code package is designed to be as small as possible with no dependencies outside of the standard library. There will be continuous work being done to increase the speed of the code.

It is important to recognize when performing benchmarks when running APIs on lambda and observing the benchmarks below that using (or increasing) [Provisioned Concurrency](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html) will reduce concurrent request times dramatically.

You can see benchmarks [here](performance/README.md)

---

## Inspiration

Peyton was inspired by [Flask](https://github.com/pallets/flask) and [Chalice](https://github.com/aws/chalice). Please check out those great projects in addition to Peyton.
