# thttp

`thttp` is a single file, lightweight, well-tested wrapper around urllib that's intended to be copied directly into your project.

Features:

- Making GET, POST, PATCH, PUT, HEAD and OPTIONS requests
- Sending query parameters with your request
- Encoding JSON payloads for POST, PATCH and PUT requests
- Enconding form-encoded payloads for POST, PATCH and PUT request
- Sending custom headers with any request
- Disabling SSL certificate verification for local testing / corporate proxies
- Following (or not following) redirects
- Sending through a CookieJar object that can be reused between requests
- HTTP basic auth
- Specifying a custom timeout for your request
- Decompressing gzipped content in the response
- Loading JSON from the response
- Returning error responses instead of throwing exceptions from urllib

Future features:

- Better detection of JSON responses
- `pretty()` function for printing responses
- Improve handling of non-utf-8 requests
- Improve handling of non-utf-8 responses

_Note: this project is not intended to solve all use cases that can be achieved with urllib, requests or other HTTP libraries. The intent is to provide a lightweight tool that simplifies some of the most common use cases for developers._


## Installation

copy `thttp.py` directly into your project:

```
curl https://raw.githubusercontent.com/sesh/thttp/main/thttp.py > thttp.py
```

Or, install with `pip`:

```
python3 -m pip install thttp
```


## Basic Usage

See the tests for examples of usage, but, effectively it's as simple as:

```python
from thttp import request

response = request("https://httpbingo.org/get", params={"data": "empty"})

response.json
# {'args': {'data': ['empty']}, 'headers': {'Accept-Encoding': ['identity'], 'Fly-Client-Ip': ['45.76.105.111'], 'Fly-Forwarded-Port': ['443'], 'Fly-Forwarded-Proto': ['https'], 'Fly-Forwarded-Ssl': ['on'], 'Fly-Region': ['hkg'], 'Fly-Request-Id': ['01F6P2WQAY1NGPRDCXV9H60XW5'], 'Host': ['httpbingo.org'], 'User-Agent': ['Python-urllib/3.8'], 'Via': ['1.1 fly.io'], 'X-Forwarded-For': ['45.76.105.111, 77.83.142.42'], 'X-Forwarded-Port': ['443'], 'X-Forwarded-Proto': ['https'], 'X-Forwarded-Ssl': ['on'], 'X-Request-Start': ['t=1622091390302198']}, 'origin': '45.76.105.111, 77.83.142.42', 'url': 'https://httpbingo.org/get?data=empty'}

response.status
# 200
```


## Running the tests

```sh
> python3 -m unittest thttp.py
```

And to check the coverage:

```sh
> coverage run -m unittest thttp.py
> coverage html && open htmlcov/index.html
```

Run `black` before committing any changes.

```sh
> black thttp.py
```

## Packaging for release

```
python3 -m build
python3 -m twine upload dist/*
```
