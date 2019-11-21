# tiny-request

An incredibly lightweight wrapper around urllib.

I can't remember _why_ I originally wrote this, but I think it may have been to use in an AWS Lambda.

Putting it here because I might have another play with this idea in the future.

## Running the tests

```sh
> python3 -m unittest tiny_request.py
```

## Basic Usage

See the tests for examples of usage, but, effectively it's as simple as:

```python
from tiny_request import request

response = request('https://httpbin.org/get', params={'library': 'tiny-request'})
print(response._fields)
# ('request', 'content', 'json', 'status', 'url', 'headers')
```
