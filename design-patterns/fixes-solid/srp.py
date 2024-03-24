class TaskManager:
    """
    TaskManager class is responsible for managing tasks.
    """
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        self.tasks.remove(task)

class TaskDisplayer:
    """
    TaskDisplayer class is responsible for displaying tasks.
    """
    @staticmethod
    def display_tasks(tasks):
        for task in tasks:
            print(task)

class TaskInput:
    """
    TaskInput class is responsible for handling user input.
    """
    @staticmethod
    def input_task():
        task = input("Enter task: ")
        return task