# Student Task Manager

A simple Python console application for students to manage their tasks.

Project status: In Development (testing in progress)

![Tests](https://github.com/M-Zayn-Abbas/student-task-manager/actions/workflows/tests.yml/badge.svg)

## Features

- **Add tasks**: empty or blank titles are rejected.
- **Show tasks**: lists every task with its ID and status (`[x]` = done).
- **Complete tasks**: shows pending tasks and marks the selected one as done.
- **Delete tasks**: deletes a task by its ID after validation and confirmation.
- **Automated tests** with Python `unittest`, run on GitHub Actions.

## Project structure

```
student-task-manager/
├── main.py                  # console menu (user interface)
├── task_manager.py          # TaskManager class (core logic)
├── tests/
│   └── test_task_manager.py # unit tests
├── docs/
│   └── user-guide.md        # short user guide
├── .github/workflows/
│   └── tests.yml            # GitHub Actions workflow
├── lab-evidence/            # screenshots for the lab
├── LAB-REPORT.md
└── LICENSE
```

## Setup

Requirements: Python 3.8 or newer. No extra packages are needed.

```bash
git clone https://github.com/M-Zayn-Abbas/student-task-manager.git
cd student-task-manager
```

## Usage

```bash
python main.py
```

Choose an option from the menu:

```
===== Student Task Manager =====
1. Add task
2. Show tasks
3. Complete task
4. Delete task
5. Exit
```

See [docs/user-guide.md](docs/user-guide.md) for a step-by-step guide.

## Running the tests

```bash
python -m unittest discover -s tests -v
```

The same command runs automatically on GitHub Actions for every push to
`main` and every pull request to `main`.

## License

This project is licensed under the [MIT License](LICENSE).
