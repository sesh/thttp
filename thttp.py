import json as json_lib
import ssl
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from collections import namedtuple


Response = namedtuple('Response', 'request content json status url headers')

def request(url, params={}, json=None, data=None, headers={}, method='GET', verify=True):
    """
    Returns a (named)tuple with the following properties:
        - request
        - content
        - json (dict; or None)
        - headers (dict; all lowercase keys)
            - https://stackoverflow.com/questions/5258977/are-http-headers-case-sensitive
        - status
        - url (final url, after any redirects)
    """
    method = method.upper()
    headers = { k.lower(): v for k, v in headers.items() }  # lowecase headers

    if params: url += '?' + urlencode(params)  # build URL from params
    if json and data: raise Exception('Cannot provide both json and data parameters')
    if method not in ['POST', 'PATCH', 'PUT'] and (json or data): raise Exception('Request method must POST, PATCH or PUT if json or data is provided')

    if json:  # if we have json, stringify and put it in our data variable
        headers['content-type'] = 'application/json'
        data = json_lib.dumps(json).encode('utf-8')

    ctx = ssl.create_default_context()
    if not verify:  # ignore ssl errors
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

    req = Request(url, data=data, headers=headers, method=method)

    try:
        with urlopen(req, context=ctx) as resp:
            status, content, resp_url = (resp.getcode(), resp.read(), resp.geturl())
            headers = {k.lower(): v for k, v in list(resp.info().items())}
            json = json_lib.loads(content) if 'application/json' in headers.get('content-type', '').lower() else None
    except HTTPError as e:
        status, content, resp_url = (e.code, e.read(), e.geturl())
        headers = {k.lower(): v for k, v in list(e.headers.items())}
        json = json_lib.loads(content) if 'application/json' in headers.get('content-type', '').lower() else None

    return Response(req, content, json, status, resp_url, headers)


import unittest

class RequestTestCase(unittest.TestCase):

    def test_cannot_provide_json_and_data(self):
        with self.assertRaises(Exception):
            request('https://httpbin.org/post', json={'name': 'Brenton'}, data="This is some form data")

    def test_should_fail_if_json_or_data_and_not_p_method(self):
        with self.assertRaises(Exception):
            request('https://httpbin.org/post', json={'name': 'Brenton'})

        with self.assertRaises(Exception):
            request('https://httpbin.org/post', json={'name': 'Brenton'}, method='HEAD')

    def test_should_set_content_type_for_json_request(self):
        response = request('https://httpbin.org/post', json={'name': 'Brenton'}, method='POST')
        self.assertEqual(response.request.headers['Content-type'], 'application/json')

    def test_should_work(self):
        response = request('https://httpbin.org/get')
        self.assertEqual(response.status, 200)

    def test_should_create_url_from_params(self):
        response = request('https://httpbin.org/get', params={'name': 'brenton', 'library': 'tiny-request'})
        self.assertEqual(response.url, 'https://httpbin.org/get?name=brenton&library=tiny-request')

    def test_should_return_headers(self):
        response = request('https://httpbin.org/response-headers', params={'Test-Header': 'value'})
        self.assertEqual(response.headers['test-header'], 'value')

    def test_should_populate_json(self):
        response = request('https://httpbin.org/json')
        self.assertTrue('slideshow' in response.json)

    def test_should_return_response_for_404(self):
        response = request('https://httpbin.org/404')
        self.assertEqual(response.status, 404)
        self.assertEqual(response.headers['content-type'], 'text/html')

    def test_should_fail_with_bad_ssl(self):
        with self.assertRaises(URLError):
            response = request('https://expired.badssl.com/')

    def test_should_load_bad_ssl_with_verify_false(self):
        response = request('https://expired.badssl.com/', verify=False)
        self.assertEqual(response.status, 200)