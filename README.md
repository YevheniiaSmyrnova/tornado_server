# SERVER
A web service which for a given request with plain text, containing urls, returns json with urls' titles.

**Example:**

Request:
```
"Olympics are starting soon; http://www.nbcolympics.com. See more at https://www.olympic.org"
```

Response:
```
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
```

# Technologies

* Language: Python 2.7
* Frameworks: Tornado

# Installation
```
git clone https://github.com/YevheniiaSmyrnova/tornado_server.git
cd tornado_server
docker-compose up
```

# TEST
```
docker exec server_python_1 bash -c "cd server; python -m tornado.testing test"
```
