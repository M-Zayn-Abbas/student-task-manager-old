"""Core logic for the Student Task Manager."""


class TaskManager:
    """Keeps the list of tasks in memory."""

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        """Create a new task and return it."""
        task = {"id": self.next_id, "title": title, "done": False}
        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self):
        """Return all tasks."""
        return self.tasks
