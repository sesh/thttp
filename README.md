# thttp

An incredibly lightweight wrapper around urllib.

I can't remember _why_ I originally wrote this, but I think it may have been to use in an AWS Lambda.

I keep pulling it into projects, so it's seen a couple of updates over the last few years.

## Running the tests

```sh
> python3 -m unittest thttp.py
```

## Basic Usage

See the tests for examples of usage, but, effectively it's as simple as:

```python
from thttp import request

response = request('https://httpbin.org/get', params={'library': 'tiny-request'})
print(response._fields)
# ('request', 'content', 'json', 'status', 'url', 'headers')
```
