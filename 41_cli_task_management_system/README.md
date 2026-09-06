# 41_cli_task_management_system

A slightly more feature-rich CLI task manager with priorities and filters.

Usage examples:
- Add: python task_manager.py add "Finish report" --priority high --due 2026-09-10T17:00
- List: python task_manager.py list
- Filter: python task_manager.py list-filter --priority high
- Mark done: python task_manager.py complete 1

Main concepts:
- JSON persistence, argparse subcommands, date handling, simple filtering.

Improvement suggestion:
- Add recurring tasks and export to calendar formats (ics).
