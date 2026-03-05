from models import User, Task
from storage import UserStorage, TaskStorage

class UserService:
    def __init__(self):
        self.storage = UserStorage("users.json")
        self.all_users = self.storage.load_users()

    def add_user(self, username: str):
        new_user = User(username)
        self.all_users.append(new_user)
        self.storage.save_users(self.all_users)
        return new_user

    def get_all(self):
        return self.all_users

    def get_user(self, user_id):
        for user in self.all_users:
            if user.id == user_id:
                return user
        return None

    def delete_user(self, user_id):
        task_service = TaskService()
        for index, user in enumerate(self.all_users):
            if user.id == user_id:
                for task in task_service.all_tasks:
                    if task.user_id == user_id:
                        return 1

                self.all_users.pop(index)
                self.storage.save_users(self.all_users)
                return 0
        return None



class TaskService:
    def __init__(self):
        self.storage = TaskStorage("tasks.json")
        self.all_tasks = self.storage.load_tasks()

    def add_task(self, title: str, user_id: str, description:str="Undefined"):
        user_service = UserService()
        if user_service.get_user(user_id):
            new_task = Task(title, user_id, description)
            self.all_tasks.append(new_task)
            self.storage.save_tasks(self.all_tasks)
            return new_task

        return None

    def get_tasks(self, user_id: str):
        tasks_found = []
        for task in self.all_tasks:
            if task.user_id == user_id:
                tasks_found.append(task)
        return tasks_found

    def update_task(self, task_id, title, description, completed):
        edited = False
        for task in self.all_tasks:
            if task.id == task_id:

                if title is not None:
                    task.title = title
                    edited = True

                if description is not None:
                    task.description = description
                    edited = True

                if completed is not None:
                    task.completed = completed
                    edited = True

                self.storage.save_tasks(self.all_tasks)

                return edited
        return edited

    def delete_task(self, task_id):
        deleted = False
        for index, task in enumerate(self.all_tasks):
            if task.id == task_id:
                self.all_tasks.pop(index)
                deleted = True
                self.storage.save_tasks(self.all_tasks)
                return deleted
        return deleted