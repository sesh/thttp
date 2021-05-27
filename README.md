# thttp

A lightweight wrapper around urllib for Python 3.

I can't remember _why_ I originally wrote this, but I think it may have been to use in an AWS Lambda where I didn't want to add [requests](https://github.com/psf/requests) as a dependency.

I keep pulling it into projects, so it's seen a couple of updates over the last few years.

## Running the tests

```sh
> python3 -m unittest thttp.py
```

And to check the coverage:

```sh
> coverage run -m unittest thttp.py
> coverage html && open htmlcov/index.html
```

## Basic Usage

See the tests for examples of usage, but, effectively it's as simple as:

```python
from thttp import request

response = request("https://httpbingo.org/get", params={"data": "empty"})

print(response.json)
# {'args': {'data': ['empty']}, 'headers': {'Accept-Encoding': ['identity'], 'Fly-Client-Ip': ['45.76.105.111'], 'Fly-Forwarded-Port': ['443'], 'Fly-Forwarded-Proto': ['https'], 'Fly-Forwarded-Ssl': ['on'], 'Fly-Region': ['hkg'], 'Fly-Request-Id': ['01F6P2WQAY1NGPRDCXV9H60XW5'], 'Host': ['httpbingo.org'], 'User-Agent': ['Python-urllib/3.8'], 'Via': ['1.1 fly.io'], 'X-Forwarded-For': ['45.76.105.111, 77.83.142.42'], 'X-Forwarded-Port': ['443'], 'X-Forwarded-Proto': ['https'], 'X-Forwarded-Ssl': ['on'], 'X-Request-Start': ['t=1622091390302198']}, 'origin': '45.76.105.111, 77.83.142.42', 'url': 'https://httpbingo.org/get?data=empty'}

print(response._fields)
#('request', 'content', 'json', 'status', 'url', 'headers', 'cookiejar')
```
