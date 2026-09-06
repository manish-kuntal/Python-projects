#!/usr/bin/env python3
"""
Student Record Manager
Simple file-backed (JSON) CRUD for student records.
Fields: id, name, age, grade
"""

import argparse
import json
from pathlib import Path
import sys

DB = Path(__file__).parent / 'students.json'


def load():
    if not DB.exists():
        return []
    try:
        return json.loads(DB.read_text(encoding='utf-8'))
    except json.JSONDecodeError:
        return []


def save(records):
    DB.write_text(json.dumps(records, indent=2), encoding='utf-8')


def add(name, age, grade):
    records = load()
    next_id = max((r['id'] for r in records), default=0) + 1
    rec = {'id': next_id, 'name': name, 'age': age, 'grade': grade}
    records.append(rec)
    save(records)
    print('Added student', next_id)


def list_all():
    for r in load():
        print(f"{r['id']}: {r['name']}, age {r['age']}, grade {r['grade']}")


def find(student_id):
    for r in load():
        if r['id'] == student_id:
            print(r)
            return
    print('Not found')


def delete(student_id):
    records = load()
    new = [r for r in records if r['id'] != student_id]
    if len(new) == len(records):
        print('Not found')
        return
    save(new)
    print('Deleted', student_id)


def update(student_id, name, age, grade):
    records = load()
    for r in records:
        if r['id'] == student_id:
            if name:
                r['name'] = name
            if age is not None:
                r['age'] = age
            if grade:
                r['grade'] = grade
            save(records)
            print('Updated', student_id)
            return
    print('Not found')


def parse_args():
    p = argparse.ArgumentParser(description='Student record manager')
    sub = p.add_subparsers(dest='cmd')
    a = sub.add_parser('add')
    a.add_argument('name')
    a.add_argument('age', type=int)
    a.add_argument('grade')
    sub.add_parser('list')
    f = sub.add_parser('find')
    f.add_argument('id', type=int)
    d = sub.add_parser('delete')
    d.add_argument('id', type=int)
    u = sub.add_parser('update')
    u.add_argument('id', type=int)
    u.add_argument('--name')
    u.add_argument('--age', type=int)
    u.add_argument('--grade')
    return p.parse_args()


def main():
    args = parse_args()
    if args.cmd == 'add':
        add(args.name, args.age, args.grade)
    elif args.cmd == 'list':
        list_all()
    elif args.cmd == 'find':
        find(args.id)
    elif args.cmd == 'delete':
        delete(args.id)
    elif args.cmd == 'update':
        update(args.id, args.name, args.age, args.grade)
    else:
        print('No command. Use -h for help')


if __name__ == '__main__':
    main()
