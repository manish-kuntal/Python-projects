#!/usr/bin/env python3
"""
Contact Book
Persistent contacts stored as JSON. Support add/search/update/delete and optional CSV import/export.
"""

import argparse
import json
from pathlib import Path
import sys
import csv

DB = Path(__file__).parent / 'contacts.json'


def load():
    if not DB.exists():
        return []
    try:
        return json.loads(DB.read_text(encoding='utf-8'))
    except json.JSONDecodeError:
        return []


def save(data):
    DB.write_text(json.dumps(data, indent=2), encoding='utf-8')


def add(name, phone, email=''):
    data = load()
    next_id = max((c['id'] for c in data), default=0) + 1
    contact = {'id': next_id, 'name': name, 'phone': phone, 'email': email}
    data.append(contact)
    save(data)
    print('Added contact', next_id)


def list_all():
    for c in load():
        print(f"{c['id']}: {c['name']} - {c['phone']} {('<'+c['email']+'>') if c.get('email') else ''}")


def search(term):
    term = term.lower()
    results = [c for c in load() if term in c['name'].lower() or term in c.get('phone','') or term in c.get('email','')]
    for c in results:
        print(c)


def delete(cid):
    data = load()
    new = [c for c in data if c['id'] != cid]
    if len(new) == len(data):
        print('Contact not found')
        return
    save(new)
    print('Deleted', cid)


def update(cid, name, phone, email):
    data = load()
    for c in data:
        if c['id'] == cid:
            if name:
                c['name'] = name
            if phone:
                c['phone'] = phone
            if email is not None:
                c['email'] = email
            save(data)
            print('Updated', cid)
            return
    print('Not found')


def import_csv(path):
    path = Path(path)
    if not path.exists():
        print('CSV not found')
        return
    data = load()
    next_id = max((c['id'] for c in data), default=0) + 1
    with path.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            contact = {'id': next_id, 'name': row.get('name','').strip(), 'phone': row.get('phone','').strip(), 'email': row.get('email','').strip()}
            data.append(contact)
            next_id += 1
    save(data)
    print('Imported')


def export_csv(path):
    data = load()
    if not data:
        print('No contacts to export')
        return
    path = Path(path)
    with path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['id','name','phone','email'])
        writer.writeheader()
        for c in data:
            writer.writerow(c)
    print('Exported to', path)


def parse_args():
    p = argparse.ArgumentParser(description='Contact book')
    sub = p.add_subparsers(dest='cmd')
    a = sub.add_parser('add')
    a.add_argument('name')
    a.add_argument('phone')
    a.add_argument('--email', default='')
    sub.add_parser('list')
    s = sub.add_parser('search')
    s.add_argument('term')
    d = sub.add_parser('delete')
    d.add_argument('id', type=int)
    u = sub.add_parser('update')
    u.add_argument('id', type=int)
    u.add_argument('--name')
    u.add_argument('--phone')
    u.add_argument('--email')
    imp = sub.add_parser('import')
    imp.add_argument('csv')
    exp = sub.add_parser('export')
    exp.add_argument('csv')
    return p.parse_args()


def main():
    args = parse_args()
    if args.cmd == 'add':
        add(args.name, args.phone, args.email)
    elif args.cmd == 'list':
        list_all()
    elif args.cmd == 'search':
        search(args.term)
    elif args.cmd == 'delete':
        delete(args.id)
    elif args.cmd == 'update':
        update(args.id, args.name, args.phone, args.email)
    elif args.cmd == 'import':
        import_csv(args.csv)
    elif args.cmd == 'export':
        export_csv(args.csv)
    else:
        print('No command. Use -h for help')


if __name__ == '__main__':
    main()
