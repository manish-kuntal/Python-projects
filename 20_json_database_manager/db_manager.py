#!/usr/bin/env python3
"""
JSON Database Manager
Simple CRUD operations on a JSON file that stores a list of records (each with a unique id).
"""

import argparse
import json
from pathlib import Path
import sys

DB = Path(__file__).parent / 'db.json'


def load():
    if not DB.exists():
        return []
    try:
        return json.loads(DB.read_text(encoding='utf-8'))
    except json.JSONDecodeError:
        return []


def save(data):
    DB.write_text(json.dumps(data, indent=2), encoding='utf-8')


def create(record):
    data = load()
    rid = max((r['id'] for r in data), default=0) + 1
    record['id'] = rid
    data.append(record)
    save(data)
    print('Created', rid)


def list_all():
    for r in load():
        print(r)


def find(rid):
    for r in load():
        if r['id'] == rid:
            print(r)
            return
    print('Not found')


def update(rid, updates):
    data = load()
    for r in data:
        if r['id'] == rid:
            r.update(updates)
            save(data)
            print('Updated', rid)
            return
    print('Not found')


def delete(rid):
    data = load()
    new = [r for r in data if r['id'] != rid]
    if len(new) == len(data):
        print('Not found')
        return
    save(new)
    print('Deleted', rid)


def parse_args():
    p = argparse.ArgumentParser(description='JSON DB manager (list of records with id)')
    sub = p.add_subparsers(dest='cmd')
    c = sub.add_parser('create')
    c.add_argument('json', help='JSON string for the record')
    sub.add_parser('list')
    f = sub.add_parser('find')
    f.add_argument('id', type=int)
    u = sub.add_parser('update')
    u.add_argument('id', type=int)
    u.add_argument('json', help='JSON string with updates')
    d = sub.add_parser('delete')
    d.add_argument('id', type=int)
    return p.parse_args()


def main():
    args = parse_args()
    if args.cmd == 'create':
        try:
            rec = json.loads(args.json)
        except json.JSONDecodeError:
            print('Invalid JSON')
            sys.exit(2)
        create(rec)
    elif args.cmd == 'list':
        list_all()
    elif args.cmd == 'find':
        find(args.id)
    elif args.cmd == 'update':
        try:
            upd = json.loads(args.json)
        except json.JSONDecodeError:
            print('Invalid JSON')
            sys.exit(2)
        update(args.id, upd)
    elif args.cmd == 'delete':
        delete(args.id)
    else:
        print('No command. Use -h for help')


if __name__ == '__main__':
    main()
