# SERVER
A web service that given a request with plain text containing urls returns json with urls' titles:

# Installation
To install:
```
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

#RUN
```
cd server
python server.py
```

# TEST
To run tornado test:
```
cd server
python -m tornado.testing server.test
```
