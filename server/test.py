import json
import tornado
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.testing import AsyncTestCase


class MyTestCase(AsyncTestCase):
    def setUp(self):
        self.request_count = 1000
        self.maxDiff = None
        super(MyTestCase, self).setUp()

    @tornado.testing.gen_test(timeout=120)
    def test_http_fetch(self):
        client = AsyncHTTPClient(self.io_loop)
        request_body = json.dumps(
            {'message': 'Olympics are starting soon '
                        'http://www.nbcolympics.com. '
                        'See more at https://www.olympic.org'})
        response = yield [client.fetch(HTTPRequest(
            method='POST',
            url='http://127.0.0.1:8888',
            body=request_body,
            connect_timeout=120,
            request_timeout=120,)) for _ in range(self.request_count)]
        data = json.dumps({"links": [
            {"url": "http://www.nbcolympics.com",
             "title": "2018 PyeongChang Olympic Games | NBC Olympics"},
            {"url": "https://www.olympic.org",
             "title": "Olympics | Olympic Games, Medals, Results, News | IOC"}
        ]})
        for i in range(self.request_count):
            self.assertEqual(data, response[i].body)
