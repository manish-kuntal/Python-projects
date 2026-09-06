# 05_todo_list_cli

A small CLI to-do list with persistent JSON storage.

Features:
- Add, list, complete, update, and delete tasks.
- Stores tasks in `tasks.json` inside the project folder.
- Uses simple integer IDs for tasks.

Usage examples:
- Add a task: python todo.py add "Buy milk" --note "2 liters"
- List tasks: python todo.py list
- Show all (including done): python todo.py list --all
- Complete a task: python todo.py complete 1
- Update a task: python todo.py update 1 --title "Buy bread"
- Delete a task: python todo.py delete 1

Project architecture:
- `todo.py` provides small helper functions: load_tasks, save_tasks, add_task, list_tasks, complete_task, delete_task, update_task.
- CLI parsing is done with argparse and subcommands.

Python concepts used:
- File I/O with pathlib, JSON serialization, argparse for CLI, and basic list/dict manipulation.

Possible improvement:
- Add due dates and filtering by priority or due date.
