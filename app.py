from fastapi import FastAPI, HTTPException
from schemas import UserCreate, TaskCreate, TaskUpdate
from services import UserService, TaskService

app = FastAPI(
    title="Task Manager",
    version='1.0'
)

@app.post("/users")
def create_user(user: UserCreate):
    service = UserService()
    user = service.add_user(username=user.username)
    return user.to_dict()

@app.get("/users")
def get_all_users():
    service = UserService()
    if service.get_all():
        return [u.to_dict() for u in service.get_all()]
    else:
        return []

@app.get("/users/{user_id}")
def display_user(user_id: str):
    service = UserService()
    user = service.get_user(user_id)
    if user:
        return user.to_dict()
    else:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

@app.post("/users/{user_id}/tasks")
def create_task(user_id: str, data: TaskCreate):
    service = TaskService()
    task = service.add_task(
        data.title,
        user_id,
        data.description
    )
    if task:
        return task.to_dict()
    else:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

@app.get("/users/{user_id}/tasks")
def display_tasks(user_id: str):
    task_service = TaskService()
    user_service = UserService()
    user_exist = user_service.get_user(user_id)
    if user_exist:
        tasks = task_service.get_tasks(user_id)
        if tasks:
            return [t.to_dict() for t in tasks]
        else:
            return []
    else:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    service = UserService()
    deleted = service.delete_user(user_id)
    if deleted == 0:
        return {
            "message": "User deleted"
        }
    elif deleted == 1:
        raise HTTPException(
            status_code=400,
            detail="Must delete all user tasks first!"
        )
    else:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

@app.patch("/tasks/{task_id}")
def edit_task(task_id: str, data: TaskUpdate):
    service = TaskService()
    patched = service.update_task(
        task_id,
        data.title,
        data.description,
        data.completed
    )

    if patched:
        return {
            "message": "Task Updated"
        }

    else: raise HTTPException(
        status_code=404,
        detail="Task not found/Invalid Request Body"
    )

@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    service = TaskService()
    deleted = service.delete_task(task_id)
    if deleted:
        return {
            "message": "Task deleted"
        }
    else:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
