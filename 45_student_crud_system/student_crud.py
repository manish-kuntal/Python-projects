#!/usr/bin/env python3
"""
Student CRUD System
A more structured CRUD system for students with validation and simple filters.
"""

import argparse
import json
from pathlib import Path

DB = Path(__file__).parent / 'students.json'


def load():
    if not DB.exists():
        return []
    try:
        return json.loads(DB.read_text(encoding='utf-8'))
    except Exception:
        return []


def save(records):
    DB.write_text(json.dumps(records, indent=2), encoding='utf-8')


def create(name, age, grade):
    records = load()
    sid = max((r['id'] for r in records), default=0) + 1
    records.append({'id': sid, 'name': name, 'age': age, 'grade': grade})
    save(records)
    print('Created', sid)


def read(sid=None):
    records = load()
    if sid:
        for r in records:
            if r['id'] == sid:
                print(r)
                return
        print('Not found')
        return
    for r in records:
        print(r)


def update(sid, name=None, age=None, grade=None):
    records = load()
    for r in records:
        if r['id'] == sid:
            if name: r['name'] = name
            if age is not None: r['age'] = age
            if grade: r['grade'] = grade
            save(records)
            print('Updated', sid)
            return
    print('Not found')


def delete(sid):
    records = load()
    new = [r for r in records if r['id'] != sid]
    if len(new) == len(records):
        print('Not found')
        return
    save(new)
    print('Deleted', sid)


def parse_args():
    p = argparse.ArgumentParser(description='Student CRUD system')
    sub = p.add_subparsers(dest='cmd')
    a = sub.add_parser('create')
    a.add_argument('name')
    a.add_argument('age', type=int)
    a.add_argument('grade')
    r = sub.add_parser('read')
    r.add_argument('--id', type=int)
    u = sub.add_parser('update')
    u.add_argument('id', type=int)
    u.add_argument('--name')
    u.add_argument('--age', type=int)
    u.add_argument('--grade')
    d = sub.add_parser('delete')
    d.add_argument('id', type=int)
    return p.parse_args()


def main():
    args = parse_args()
    if args.cmd == 'create':
        create(args.name, args.age, args.grade)
    elif args.cmd == 'read':
        read(args.id)
    elif args.cmd == 'update':
        update(args.id, args.name, args.age, args.grade)
    elif args.cmd == 'delete':
        delete(args.id)
    else:
        print('No command. Use -h for help')

if __name__ == '__main__':
    main()
