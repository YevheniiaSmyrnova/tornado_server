# SERVER
A web service which for a given request with plain text, containing urls, returns json with urls' titles.

**Example:**

Request:

"Olympics are starting soon; http://www.nbcolympics.com. See more at https://www.olympic.org"

Response:

{

  "links": [

    {

      "url": "http://www.nbcolympics.com",

      "title": "2018 Rio Olympic Games | NBC Olympics"

    },

    {

      "url": "https://www.olympic.org",

      "title": "Olympics | Olympic Games, Medals, Results, News | IOC"

    }

  ]

}

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
