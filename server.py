import json
import tornado.ioloop
import tornado.web
import tornado.httpserver
import re
from lxml.html import fromstring
from tornado import gen
from tornado.httpclient import AsyncHTTPClient


class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def post(self):
        self.set_header("Content-Type", "text/plain")
        http_client = AsyncHTTPClient()
        mes = json.loads(self.request.body)['message']

        list_urls = re.findall(r'(https?://[^\s]+)', mes)
        list_urls_titles = []

        for i, elem in enumerate(list_urls):
            dict_url_title = {}
            if elem.endswith(('.', ',', '!', '?'), -1):
                list_urls[i] = elem[:-1]
            dict_url_title['url'] = list_urls[i]

            response = yield http_client.fetch(dict_url_title['url'])
            tree = fromstring(response.body)
            dict_url_title['title'] = tree.findtext('.//title')

            list_urls_titles.append(dict_url_title)
        # http_client.close()
        data = {'links': list_urls_titles}
        self.write(json.dumps(data))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    sock = tornado.netutil.bind_sockets(8888);
    server = tornado.httpserver.HTTPServer(make_app())
    server.add_sockets(sock)
    tornado.ioloop.IOLoop.current().start()
