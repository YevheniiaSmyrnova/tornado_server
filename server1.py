import json
import tornado.ioloop
import tornado.web
import tornado.httpserver
import re
import requests
from lxml.html import fromstring
from tornado import httpclient
from tornado.httpclient import AsyncHTTPClient, HTTPClient


class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        f = open("upload.html")
        self.write(f.read())
        f.close()
        self.flush()
        self.finish()

    def post(self):
        self.set_header("Content-Type", "text/plain")
        http_client = HTTPClient()
        import pdb;pdb.set_trace()
        mes = self.get_argument('message')
        list_urls = re.findall(r'(https?://[^\s]+)', mes)
        list_urls_titles = []
        for i, elem in enumerate(list_urls):
            dict_url_title = {}
            if elem.endswith(('.', ',', '!', '?'), -1):
                list_urls[i] = elem[:-1]
            dict_url_title['url'] = list_urls[i]
            try:
                response = http_client.fetch(dict_url_title['url'])
                # response = http_client.fetch(dict_url_title['url'], handle_response)
                tree = fromstring(response.body)
                dict_url_title['title'] = tree.findtext('.//title')
            except httpclient.HTTPError as e:
                print("Error: " + str(e))
            except Exception as e:
                print("Error: " + str(e))
            list_urls_titles.append(dict_url_title)
        http_client.close()
        data = {'links': list_urls_titles}
        self.write(json.dumps(data))


def handle_response(response):
    if response.error:
        print "Error:", response.error
    # else:
        # print response.body


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    sock = tornado.netutil.bind_sockets(8888);
    server = tornado.httpserver.HTTPServer(make_app())
    server.add_sockets(sock)
    tornado.ioloop.IOLoop.current().start()
