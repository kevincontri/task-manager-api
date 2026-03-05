import uuid
from datetime import datetime

class User:

    def __init__ (self, username):
        self.id = str(uuid.uuid4())
        self.username = username
        self.created_at = datetime.now().isoformat()

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "username": self.username,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        new_user = cls(
            data["username"]
        )
        new_user.id = data["id"]
        new_user.created_at = data["created_at"]

        return new_user


class Task:

    def __init__(self, title, user_id, description=None, completed=False):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.completed = completed
        self.user_id = user_id
        self.created_at = datetime.now().isoformat()

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "user_id": self.user_id,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        new_task = cls(
            title=data["title"],
            description=data["description"],
            completed=data["completed"],
            user_id=data["user_id"]
        )

        new_task.id = data["id"]
        new_task.created_at = data["created_at"]

        return new_task


