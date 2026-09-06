# 39_task_reminder

Simple task reminder storing tasks with ISO-format due dates in `tasks.json`.

Usage:
- Add: python task_reminder.py add "Pay rent" --due 2026-09-05T09:00
- List: python task_reminder.py list
- Complete: python task_reminder.py complete 1

Improvement suggestion:
- Add notifications (desktop or email) for overdue tasks when run as a scheduled job.
