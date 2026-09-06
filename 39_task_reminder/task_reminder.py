#!/usr/bin/env python3
"""
Task Reminder
Create tasks with due dates and show pending or overdue reminders.
"""

import argparse
import json
from datetime import datetime
from pathlib import Path
import sys

DB = Path(__file__).parent / 'tasks.json'


def load():
    if not DB.exists():
        return []
    try:
        return json.loads(DB.read_text(encoding='utf-8'))
    except Exception:
        return []


def save(tasks):
    DB.write_text(json.dumps(tasks, indent=2), encoding='utf-8')


def add(title, due):
    tasks = load()
    nid = max((t['id'] for t in tasks), default=0) + 1
    tasks.append({'id': nid, 'title': title, 'due': due, 'done': False})
    save(tasks)
    print('Added task', nid)


def list_tasks(show_all=False):
    now = datetime.now()
    for t in load():
        due = datetime.fromisoformat(t['due']) if t.get('due') else None
        status = 'Done' if t.get('done') else ('Overdue' if due and due < now else 'Pending')
        if not show_all and t.get('done'):
            continue
        print(f"{t['id']}: {t['title']} - due: {t.get('due')} - {status}")


def complete(nid):
    tasks = load()
    for t in tasks:
        if t['id'] == nid:
            t['done'] = True
            save(tasks)
            print('Completed', nid)
            return
    print('Not found')


def parse_args():
    p = argparse.ArgumentParser(description='Task reminder')
    sub = p.add_subparsers(dest='cmd')
    a = sub.add_parser('add')
    a.add_argument('title')
    a.add_argument('--due', help='Due date in ISO format e.g. 2026-09-10T14:30')
    sub.add_parser('list')
    c = sub.add_parser('complete')
    c.add_argument('id', type=int)
    return p.parse_args()


def main():
    args = parse_args()
    if args.cmd == 'add':
        add(args.title, args.due)
    elif args.cmd == 'list':
        list_tasks()
    elif args.cmd == 'complete':
        complete(args.id)
    else:
        print('No command. Use -h for help')


if __name__ == '__main__':
    main()
