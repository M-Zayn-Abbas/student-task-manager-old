# User Guide: Student Task Manager

## Starting the program

Open a terminal in the project folder and run:

```bash
python main.py
```

The main menu appears:

```
===== Student Task Manager =====
1. Add task
2. Show tasks
3. Complete task
4. Delete task
5. Exit
Choose an option:
```

## 1. Add a task

Choose `1` and type the task title, for example `Submit DevOps lab 4`.
The program confirms with the new task's ID. An empty title is rejected
with the message `Error: Task title cannot be empty.`

## 2. Show tasks

Choose `2` to list all tasks:

```
1. [x] Submit DevOps lab 4
2. [ ] Prepare for viva
```

`[x]` means the task is completed and `[ ]` means it is still pending.

## 3. Complete a task

Choose `3`. The program lists pending tasks; type the ID of the task you
finished. If the ID does not exist you get an error, and if the task is
already completed you are told so.

## 4. Delete a task

Choose `4` and type the task ID. The ID must be a number of an existing
task. Type `y` to confirm, or anything else to cancel.

## 5. Exit

Choose `5` to close the program.

> Note: tasks are kept in memory, so they are cleared when the program exits.
