## Task Manager REST API
A backend service in a REST-style for managing users and their tasks using `FastAPI`. This project demonstrates fundamental backend development concepts, such as:
- RESTful routing
- Layered architecture
- Request and response validation with Pydantic
- JSON-based persistence
- Basic relational logic (users and their tasks)
- HTTP status handling with FastAPI

This application allows creation of users and management of tasks associated with each user

## Stack
- Python
- FastAPI
- Pydantic
- Uvicorn

Dependencies managed using `requirements.txt`

## Project Structure
- `app.py` - API layer (HTTP routes and request/response handling)
- `services.py` - Business logic for users and tasks
- `storage.py` - JSON persistence layer for saving and loading data
- `models.py` - Domain entities (`User` and `Task`)
- `schemas.py` - Pydantic models for request validation
- `requirements.txt` - Dependencies

## Installation
##### Clone the repository: <br>
```git clone https://github.com/kevincontri/task-manager-api.git```
```cd task-manager-api```
##### Create and activate virtual environment:<br>
```python -m venv venv```<br>
```venv\Scripts\activate```
##### Install dependencies: <br>
```pip install -r requirements.txt```

## Run the server
```uvicorn app:app --reload```
##### Open interactive docs:
```http://127.0.0.1:8000/docs```

## API User Endpoints
### Create user
`POST /users`<br>
Request body:
```
{
  "username": "antony"
}
```
### Get all users
`GET /users`<br>
Response:
```
[
  {
    "id": "uuid",
    "username": "antony",
    "created_at": "timestamp"
  }
]
```
### Get a specific user
`GET /users/{user_id}`<br>
Returns user information.

### Delete a user
`DELETE /users/{user_id}`<br>
A user cannot be deleted if they still have tasks.<br>
Response:
```
{
  "message": "User deleted"
}
```

## API Task Endpoints
### Create task for a user
`POST /users/{user_id}/tasks` <br>
Request body:
```
{
  "title": "Study FastAPI",
  "description": "Learn how FastAPI handles request validation"
}
```

### Get all tasks of a user
`GET /users/{user_id}/tasks` <br>
Response:
```
[
  {
    "id": "uuid",
    "title": "Study Python",
    "description": "Learn how Python works",
    "completed": false,
    "user_id": "uuid",
    "created_at": "timestamp"
  }
]
```

### Edit a task
`PATCH /tasks/{task_id}` <br>
Request body (any combination of fields):
```
{
  "title": "Study Python deeply",
  "completed": true
}
```

### Delete a task
`DELETE /tasks/{task_id}` <br>
Response:
```
{
  "message": "Task deleted"
}
```

## Future Improvements
- Replace JSON storage with a SQL database (SQLite / PostgreSQL)
- Implement dependency injection for services
- Add authentication (JWT)
