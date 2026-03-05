from models import User, Task
import os
import json

class UserStorage:
    def __init__(self, filename: str):
        self.filename = filename

    def save_users(self, users: list[User]) -> None:
        data = [t.to_dict() for t in users]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_users(self):
        if not os.path.exists(self.filename):
            return []

        with open(self.filename, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return []

        return [User.from_dict(item) for item in data]

class TaskStorage:
    def __init__(self, filename: str):
        self.filename = filename

    def save_tasks(self, tasks: list[Task]) -> None:
        data = [t.to_dict() for t in tasks]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []

        with open(self.filename, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return []

        return [Task.from_dict(item) for item in data]

