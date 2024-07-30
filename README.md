# Data Storage API

Implement a small HTTP service to store objects organized by repository.
Clients of this service should be able to GET, PUT, and DELETE objects.

## General Requirements

* The service should de-duplicate data objects by repository.
* The service should listen on port `8282`.
* The data can be persisted in memory, on disk, or wherever you like.
* The service must implement the API as described below.

## Quickstart

### Setup

```sh
$ poetry install
$ poetry shell
$ export FLASK_APP=data_storage_api.apps.http:create_app
$ export FLASK_ENV=development  # or production
```

### Run

```sh
$ poetry run flask run  -h 0.0.0.0 -p 8282
```

### Testing

```sh
$ pytest
```

## API

### Upload an Object

**The repositories are created when performing a request against to the url containing the name of the repository.**

e.g.

**ending a request to /data/test-repo/ will create `test-repo` repo in case it doesn't exist yet.**

```
PUT /data/{repository}
```

#### Response

```
Status: 201 Created
{
  "oid": "2845f5a412dbdfacf95193f296dd0f5b2a16920da5a7ffa4c5832f223b03de96",
  "size": 1234
}
```

### Download an Object

```
GET /data/{repository}/{objectID}
```

#### Response

```
Status: 200 OK
{object data}
```

Objects that are not on the server will return a `404 Not Found`.

### Delete an Object

```
DELETE /data/{repository}/{objectID}
```

#### Response

```
Status: 200 OK
```

