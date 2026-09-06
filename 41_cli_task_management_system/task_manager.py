#!/usr/bin/env python3
"""
CLI Task Management System
Tasks with id, title, priority, due, status; support add/list/update/complete/delete/filter
"""

import argparse
import json
from datetime import datetime
from pathlib import Path
import sys

DB = Path(__file__).parent / 'tasks.json'

PRIORITIES = ['low','medium','high']


def load():
    if not DB.exists():
        return []
    try:
        return json.loads(DB.read_text(encoding='utf-8'))
    except Exception:
        return []


def save(tasks):
    DB.write_text(json.dumps(tasks, indent=2), encoding='utf-8')


def add(title, priority='medium', due=None):
    if priority not in PRIORITIES:
        raise ValueError('Invalid priority')
    tasks = load()
    nid = max((t['id'] for t in tasks), default=0) + 1
    tasks.append({'id': nid, 'title': title, 'priority': priority, 'due': due, 'done': False, 'created': datetime.now().isoformat()})
    save(tasks)
    print('Added', nid)


def list_tasks(show_all=False, priority=None, overdue=False):
    tasks = load()
    now = datetime.now()
    for t in tasks:
        if not show_all and t['done']:
            continue
        if priority and t['priority'] != priority:
            continue
        if overdue and t.get('due'):
            try:
                if datetime.fromisoformat(t['due']) > now:
                    continue
            except Exception:
                continue
        status = 'Done' if t['done'] else 'Overdue' if t.get('due') and datetime.fromisoformat(t['due']) < now else 'Pending'
        print(f"{t['id']}: [{t['priority']}] {t['title']} - due: {t.get('due')} - {status}")


def complete(nid):
    tasks = load()
    for t in tasks:
        if t['id'] == nid:
            t['done'] = True
            save(tasks)
            print('Completed', nid)
            return
    print('Not found')


def update(nid, title=None, priority=None, due=None):
    tasks = load()
    for t in tasks:
        if t['id'] == nid:
            if title:
                t['title'] = title
            if priority:
                if priority not in PRIORITIES:
                    print('Invalid priority')
                    return
                t['priority'] = priority
            if due is not None:
                t['due'] = due
            save(tasks)
            print('Updated', nid)
            return
    print('Not found')


def delete(nid):
    tasks = load()
    new = [t for t in tasks if t['id'] != nid]
    if len(new) == len(tasks):
        print('Not found')
        return
    save(new)
    print('Deleted', nid)


def parse_args():
    p = argparse.ArgumentParser(description='CLI Task Management System')
    sub = p.add_subparsers(dest='cmd')
    a = sub.add_parser('add')
    a.add_argument('title')
    a.add_argument('--priority', choices=PRIORITIES, default='medium')
    a.add_argument('--due', help='ISO date e.g. 2026-09-10T12:00')
    sub.add_parser('list')
    l = sub.add_parser('list-filter')
    l.add_argument('--priority', choices=PRIORITIES)
    l.add_argument('--overdue', action='store_true')
    c = sub.add_parser('complete')
    c.add_argument('id', type=int)
    u = sub.add_parser('update')
    u.add_argument('id', type=int)
    u.add_argument('--title')
    u.add_argument('--priority', choices=PRIORITIES)
    u.add_argument('--due')
    d = sub.add_parser('delete')
    d.add_argument('id', type=int)
    return p.parse_args()


def main():
    args = parse_args()
    if args.cmd == 'add':
        add(args.title, args.priority, args.due)
    elif args.cmd == 'list':
        list_tasks()
    elif args.cmd == 'list-filter':
        list_tasks(show_all=True, priority=args.priority, overdue=args.overdue)
    elif args.cmd == 'complete':
        complete(args.id)
    elif args.cmd == 'update':
        update(args.id, args.title, args.priority, args.due)
    elif args.cmd == 'delete':
        delete(args.id)
    else:
        print('No command. Use -h for help')


if __name__ == '__main__':
    main()
