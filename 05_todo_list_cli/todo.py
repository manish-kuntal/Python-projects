#!/usr/bin/env python3
"""
To-Do List CLI
Simple file-backed to-do list using JSON storage.
Supports: add, list, complete, update, delete
"""

import argparse
import json
from pathlib import Path
import sys
from typing import List, Dict

DB = Path(__file__).parent / 'tasks.json'


def load_tasks() -> List[Dict]:
    if not DB.exists():
        return []
    try:
        return json.loads(DB.read_text(encoding='utf-8'))
    except json.JSONDecodeError:
        return []


def save_tasks(tasks: List[Dict]):
    DB.write_text(json.dumps(tasks, indent=2), encoding='utf-8')


def add_task(title: str, note: str = ''):
    tasks = load_tasks()
    next_id = max((t['id'] for t in tasks), default=0) + 1
    task = {'id': next_id, 'title': title, 'note': note, 'done': False}
    tasks.append(task)
    save_tasks(tasks)
    print('Added task', next_id)


def list_tasks(show_all: bool = False):
    tasks = load_tasks()
    if not tasks:
        print('No tasks found.')
        return
    for t in tasks:
        if not show_all and t['done']:
            continue
        status = '✓' if t['done'] else ' ' 
        print(f"[{status}] {t['id']}: {t['title']}" + (f" - {t['note']}" if t.get('note') else ''))


def complete_task(task_id: int):
    tasks = load_tasks()
    for t in tasks:
        if t['id'] == task_id:
            t['done'] = True
            save_tasks(tasks)
            print('Marked done:', task_id)
            return
    print('Task not found:', task_id)


def delete_task(task_id: int):
    tasks = load_tasks()
    new = [t for t in tasks if t['id'] != task_id]
    if len(new) == len(tasks):
        print('Task not found:', task_id)
        return
    save_tasks(new)
    print('Deleted task:', task_id)


def update_task(task_id: int, title: str = None, note: str = None):
    tasks = load_tasks()
    for t in tasks:
        if t['id'] == task_id:
            if title is not None:
                t['title'] = title
            if note is not None:
                t['note'] = note
            save_tasks(tasks)
            print('Updated task:', task_id)
            return
    print('Task not found:', task_id)


def parse_args():
    p = argparse.ArgumentParser(description='Simple to-do list CLI')
    sub = p.add_subparsers(dest='cmd')

    a = sub.add_parser('add')
    a.add_argument('title')
    a.add_argument('--note', default='')

    l = sub.add_parser('list')
    l.add_argument('--all', action='store_true', help='Show completed tasks')

    c = sub.add_parser('complete')
    c.add_argument('id', type=int)

    d = sub.add_parser('delete')
    d.add_argument('id', type=int)

    u = sub.add_parser('update')
    u.add_argument('id', type=int)
    u.add_argument('--title')
    u.add_argument('--note')

    return p.parse_args()


def main():
    args = parse_args()
    if args.cmd == 'add':
        add_task(args.title, args.note)
    elif args.cmd == 'list':
        list_tasks(args.all)
    elif args.cmd == 'complete':
        complete_task(args.id)
    elif args.cmd == 'delete':
        delete_task(args.id)
    elif args.cmd == 'update':
        update_task(args.id, args.title, args.note)
    else:
        print('No command given. Use -h for help.')


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print('\nExiting.')
        sys.exit(0)
