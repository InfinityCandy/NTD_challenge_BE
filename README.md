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

## API Endpoints

All endpoints are prefixed by `/planets/`.

| Method | Endpoint         | Description                  |
| ------ | ---------------- | ---------------------------- |
| GET    | `/planets/`      | Retrieve list of all planets |
| GET    | `/planets/<id>/` | Retrieve a specific planet   |
| POST   | `/planets/`      | Create a new planet          |
| PUT    | `/planets/<id>/` | Replace a planet entry       |
| PATCH  | `/planets/<id>/` | Partially update a planet    |
| DELETE | `/planets/<id>/` | Delete a planet              |

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

## Request/Response Examples

### `GET /planets/`

```json
STATUS CODE 200

[
  {
    "id": 1,
    "name": "Tatooine",
    "population": 200000,
    "climates": "Arid",
    "terrains": "Desert"
  },
    {
    "id": 2,
    "name": "Alderaan",
    "population": 506000,
    "climates": "Rocks",
    "terrains": "Cold"
  },
  ...
]
```

### `GET /planets/<id>/`

```json
STATUS CODE 200

{
  "id": 1,
  "name": "Tatooine",
  "population": 200000,
  "climates": "arid",
  "terrains": "desert"
}
```

### `POST /planets/`

```json
{
  "name": "Mars",
  "population": 1000000,
  "terrains": "Rocks",
  "climates": "Super Dry"
}
```

```json
STATUS CODE 200

{
  "id": 64,
  "name": "Mars",
  "population": 1000000,
  "terrains": "Rocks",
  "climates": "Super Dry"
}
```

### `PUT /planets/`

```json
{
  "name": "Super Mars",
  "population": 1100000,
  "terrains": "Rocks",
  "climates": "Super Dry"
}
```

```json
STATUS CODE 200

{
  "id": 3,
  "name": "Super Mars",
  "population": 1100000,
  "terrains": "Rocks",
  "climates": "Super Dry"
}
```

### `PATCH /planets/`

```json
{
  "name": "Super Earth"
}
```

```json
STATUS CODE 200

{
  "id":1,
  "name": "Super Earth",
  "population": 80000000,
  "terrains": "Rock and mountains",
  "climates": "Dry"
}
```

### `DELETE /planets/`

```json
STATUS CODE 201
```

## Test API

Open an terminal an use the curl tool to send requests to the API while the Django server is up and running

- Test GET all method

```
$ curl -X GET http://localhost:8000/planets/
```

- Test GET single element method

```
$ curl -X GET http://localhost:8000/planets/1/
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

## Error Format & Status Codes

All API errors follow this structure:

```json
{
  "detail": "Error message describing the problem."
}
```

## External API Sync

The command python manage.py consume_data pulls planetary data from a third-party Star Wars API. It parses the API response and inserts planets into the local database using Django models. The sync handles:

- De-duplication: Planets already in the database are not duplicated.

- Resilience: Logs and skips planets with incomplete or invalid data.

You can re-run the command at any time to sync any new or updated data from the external source with:

```
$ python manage.py consume_data
```
