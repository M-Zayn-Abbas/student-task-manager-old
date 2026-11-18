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

    def find_task(self, task_id):
        """Return the task with the given ID, or None if it does not exist."""
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    def complete_task(self, task_id):
        """Mark a task as completed."""
        task = self.find_task(task_id)
        if task is None:
            return False
        task["done"] = True
        return True

    def delete_task(self, task_id):
        """Remove a task from the list and return it.

        Raises ValueError if the ID is not a valid existing task ID.
        """
        if not isinstance(task_id, int) or task_id < 1:
            raise ValueError("Task ID must be a positive whole number.")
        task = self.find_task(task_id)
        if task is None:
            raise ValueError(f"No task found with ID {task_id}.")
        self.tasks.remove(task)
        return task
