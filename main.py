"""Console interface for the Student Task Manager."""

from task_manager import TaskManager

MENU = """
===== Student Task Manager =====
1. Add task
2. Show tasks
3. Complete task
4. Delete task
5. Exit"""


def show_tasks(manager):
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        status = "x" if task["done"] else " "
        print(f"{task['id']}. [{status}] {task['title']}")


def handle_add(manager):
    title = input("Task title: ")
    task = manager.add_task(title)
    print(f"Added task {task['id']}.")


def handle_complete(manager):
    task_id = int(input("Task ID to complete: "))
    if manager.complete_task(task_id):
        print("Task marked as completed.")
    else:
        print("Task not found.")


def handle_delete(manager):
    raw = input("Task ID to delete: ").strip()
    if not raw.isdigit():
        print("Error: please enter a valid numeric task ID.")
        return
    task_id = int(raw)
    if manager.find_task(task_id) is None:
        print(f"Error: no task found with ID {task_id}.")
        return
    confirm = input(f"Delete task {task_id}? (y/n): ").strip().lower()
    if confirm != "y":
        print("Delete cancelled.")
        return
    task = manager.delete_task(task_id)
    print(f"Deleted task: {task['title']}")


def main():
    manager = TaskManager()
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            handle_add(manager)
        elif choice == "2":
            show_tasks(manager)
        elif choice == "3":
            handle_complete(manager)
        elif choice == "4":
            handle_delete(manager)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
