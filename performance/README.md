# Performance

Performance tests are run using [ab - The Apache HTTP server benchmarking tool](https://httpd.apache.org/docs/2.4/programs/ab.html#:~:text=ab%20%2D%20Apache%20HTTP%20server%20benchmarking%20tool,-Available%20Languages%3A%20en&text=ab%20is%20a%20tool%20for,installation%20is%20capable%20of%20serving)

---
Test Setup Code:
```
from peyton.view import ViewBase
from peyton.response import Response
from peyton.request import Request
from peyton.router import Router


router = Router()


@router.register(path="/foo/{foo_id}/bar/{bar_id}")
class AllBars(ViewBase):
    def get(self, foo_id, bar_id) -> dict:
        resp = Response(
            status_code=200,
            headers={},
            body={"foo_id": foo_id, "bar_id": bar_id, "message": "all bars by foo"},
        )

        return resp.to_json()


def lambda_handler(event, context):
    request = Request(event)
    return router.dispatch(request=request)

```

---

## Rest API

### Test 1

- Lambda with no provisioned concurrency
- Cold start
- 10 Concurrent Requests
- 1000 Total Requests
```
#!/bin/bash

ab -c 10 -n 1000 https://xxxx.execute-api.us-west-2.amazonaws.com/foo/2/bar/3

---

Document Length:        60 bytes

Concurrency Level:      10
Time taken for tests:   21.452 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      346000 bytes
HTML transferred:       60000 bytes
Requests per second:    46.62 [#/sec] (mean)
Time per request:       214.523 [ms] (mean)
Time per request:       21.452 [ms] (mean, across all concurrent requests)
Transfer rate:          15.75 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:      120  143  20.5    139     373
Processing:    49   67  24.6     61     302
Waiting:       49   66  23.1     61     302
Total:        175  210  33.8    203     515

Percentage of the requests served within a certain time (ms)
  50%    203
  66%    208
  75%    213
  80%    216
  90%    229
  95%    258
  98%    322
  99%    393
 100%    515 (longest request)
```

### Test 2

- Lambda with no provisioned concurrency
- No cold start
- 10 Concurrent Requests
- 1000 Total Requests
```
#!/bin/bash

ab -c 10 -n 1000 https://xxxx.execute-api.us-west-2.amazonaws.com/foo/2/bar/3

---

Document Length:        60 bytes

Concurrency Level:      10
Time taken for tests:   21.319 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      346000 bytes
HTML transferred:       60000 bytes
Requests per second:    46.91 [#/sec] (mean)
Time per request:       213.194 [ms] (mean)
Time per request:       21.319 [ms] (mean, across all concurrent requests)
Transfer rate:          15.85 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:      116  143  13.5    140     203
Processing:    50   67  14.9     65     216
Waiting:       50   66  14.0     63     216
Total:        174  210  20.3    207     362

Percentage of the requests served within a certain time (ms)
  50%    207
  66%    214
  75%    219
  80%    222
  90%    232
  95%    249
  98%    264
  99%    277
 100%    362 (longest request)
```

### Test 3
- Lambda with no provisioned concurrency
- No cold start
- 1 Concurrent Requests
- 50 Total Requests
```
#!/bin/bash

ab -c 10 -n 1000 https://xxxx.execute-api.us-west-2.amazonaws.com/foo/2/bar/3

---

Document Length:        60 bytes

Concurrency Level:      1
Time taken for tests:   9.482 seconds
Complete requests:      50
Failed requests:        0
Total transferred:      17300 bytes
HTML transferred:       3000 bytes
Requests per second:    5.27 [#/sec] (mean)
Time per request:       189.649 [ms] (mean)
Time per request:       189.649 [ms] (mean, across all concurrent requests)
Transfer rate:          1.78 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:      121  133   6.3    132     153
Processing:    52   56   4.0     56      69
Waiting:       52   56   4.0     56      69
Total:        174  189   7.2    188     210

Percentage of the requests served within a certain time (ms)
  50%    188
  66%    191
  75%    194
  80%    195
  90%    201
  95%    205
  98%    210
  99%    210
 100%    210 (longest request)
```

## HTTP API

### Test 1
- Lambda with no provisioned concurrency
- Cold start
- 10 Concurrent Requests
- 1000 Total Requests

```
#!/bin/bash

ab -c 10 -n 1000 https://xxxx.execute-api.us-west-2.amazonaws.com/foo/2/bar/3

---

Document Length:        60 bytes

Concurrency Level:      10
Time taken for tests:   20.715 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      231000 bytes
HTML transferred:       60000 bytes
Requests per second:    48.27 [#/sec] (mean)
Time per request:       207.150 [ms] (mean)
Time per request:       20.715 [ms] (mean, across all concurrent requests)
Transfer rate:          10.89 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:      119  143   9.1    143     193
Processing:    46   59  18.7     56     265
Waiting:       46   59  18.5     56     264
Total:        170  203  22.4    200     437

Percentage of the requests served within a certain time (ms)
  50%    200
  66%    204
  75%    206
  80%    208
  90%    213
  95%    219
  98%    236
  99%    257
 100%    437 (longest request)
```

### Test 2
- Lambda with no provisioned concurrency
- No cold start
- 10 Concurrent Requests
- 1000 Total Requests
```
#!/bin/bash

ab -c 10 -n 1000 https://xxxx.execute-api.us-west-2.amazonaws.com/foo/2/bar/3

---

Document Length:        60 bytes

Concurrency Level:      10
Time taken for tests:   20.243 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      231000 bytes
HTML transferred:       60000 bytes
Requests per second:    49.40 [#/sec] (mean)
Time per request:       202.433 [ms] (mean)
Time per request:       20.243 [ms] (mean, across all concurrent requests)
Transfer rate:          11.14 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:      120  138   9.3    137     185
Processing:    44   61   8.5     59     107
Waiting:       44   60   7.5     59      98
Total:        169  200  12.3    198     255

Percentage of the requests served within a certain time (ms)
  50%    198
  66%    203
  75%    207
  80%    209
  90%    216
  95%    222
  98%    232
  99%    236
 100%    255 (longest request)
```

### Test 3
- Lambda with no provisioned concurrency
- No cold start
- 1 Concurrent Requests
- 50 Total Requests
```
#!/bin/bash

ab -c 10 -n 1000 https://xxxx.execute-api.us-west-2.amazonaws.com/foo/2/bar/3

---

Document Length:        60 bytes

Concurrency Level:      1
Time taken for tests:   9.421 seconds
Complete requests:      50
Failed requests:        0
Total transferred:      11550 bytes
HTML transferred:       3000 bytes
Requests per second:    5.31 [#/sec] (mean)
Time per request:       188.429 [ms] (mean)
Time per request:       188.429 [ms] (mean, across all concurrent requests)
Transfer rate:          1.20 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:      122  132   5.9    132     155
Processing:    49   56   4.9     55      76
Waiting:       49   56   4.9     55      76
Total:        173  188   7.3    187     209

Percentage of the requests served within a certain time (ms)
  50%    187
  66%    191
  75%    192
  80%    193
  90%    198
  95%    200
  98%    209
  99%    209
 100%    209 (longest request)
```
