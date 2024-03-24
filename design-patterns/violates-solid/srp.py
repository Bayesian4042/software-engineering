class ToDoList:
    """
    This class handles multiple responsibilities: managing tasks, displaying tasks, and handling user input.
    Having multiple responsibilities in a single class makes it harder to maintain, understand and extend, as change in one area can impact the other.
    """
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        self.tasks.remove(task)

    def display_tasks(self):
        for task in self.tasks:
            print(task)

    def input_task(self):
        task = input("Enter task: ")
        self.add_task(task)