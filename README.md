## Project Setup

Each one of the steps described below contains the commands that need to be run in order to complete the configuration step.

1. Navigate to project's root folder

```
$ cd NTD_challenge_BE
```

2. Create a new virtual environment

```
$ python -m venv .venv
```

4. Install project dependencies

```
$ pip install -r requirements.txt
```

5. Run migrations

```
$ python manage.py migrate
```

6. Create Django admin superuser

```
$ python manage.py createsuperuser
```

7. Pull data from third party API and insert it in the DB

```
$ python manage.py consume_data
```

8. Run Django server

```
$ python manage.py runserver
```

## Test API

Open an terminal an use the curl tool to send requests to the API while the Django server is up and running

- Test GET all method

```
$ curl -X GET http://localhost:8000/planets/
```

- Test GET single element method

```
$ curl -X GET http://localhost:8000/planets/1
```

- Test POST method

```
$ curl -X POST http://localhost:8000/planets/ \
    -H "Content-Type: application/json" \
    -d '{"name": "Mars", "population": 1000000, "terrains": "Rocks", "climates": "Super Dry"}'
```

- Test PUT method

```
$ curl -X PUT http://localhost:8000/planets/61/ \
    -H "Content-Type: application/json" \
    -d '{"name": "Mars", "population": 1000000, "terrains": "Rocks", "climates": "Super Duper Dry"}'
```

- Test PATCH method

```
$ curl -X PATCH http://localhost:8000/planets/1/ \
    -H "Content-Type: application/json" \
    -d '{"name": "Super Earth"}'
```

- Test DELETE method

```
$ curl -X DELETE http://localhost:8000/planets/61/
```
