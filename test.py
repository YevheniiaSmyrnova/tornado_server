import os

import concurrent.futures
from threading import Lock
import requests

lock = Lock()
INPUT = "down.txt"
THREADS = 10


def download():
    r = requests.post("http://127.0.0.1:8888", data={'message': 'Olympics are starting soon http://www.nbcolympics.com. See more at https://www.olympic.org'})
    print(r.status_code, r.reason)
    with lock:
        print r
    #os.system(str(r))


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as ex:
        for i in range(THREADS):
            #with open(INPUT) as mes:
            c = ex.submit(download)
            print(c.result())


    [fetch(HttpRequest(url='', body='')) for _ in range(1000)]


##########

if __name__ == "__main__":
    main()
