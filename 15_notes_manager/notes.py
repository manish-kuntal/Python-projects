#!/usr/bin/env python3
"""
Notes Manager
Create, view, search, edit, and delete notes stored in notes.json.
Each note: id, title, content, tags
"""

import argparse
import json
from pathlib import Path
import sys
from datetime import datetime

DB = Path(__file__).parent / 'notes.json'


def load():
    if not DB.exists():
        return []
    try:
        return json.loads(DB.read_text(encoding='utf-8'))
    except json.JSONDecodeError:
        return []


def save(data):
    DB.write_text(json.dumps(data, indent=2), encoding='utf-8')


def add(title, content, tags):
    notes = load()
    nid = max((n['id'] for n in notes), default=0) + 1
    note = {'id': nid, 'title': title, 'content': content, 'tags': tags, 'created': datetime.now().isoformat()}
    notes.append(note)
    save(notes)
    print('Added note', nid)


def list_notes():
    for n in load():
        print(f"{n['id']}: {n['title']} [tags: {','.join(n.get('tags',[]))}]")


def find(term):
    term = term.lower()
    for n in load():
        if term in n['title'].lower() or term in n['content'].lower() or term in ','.join(n.get('tags',[])):
            print(n)


def delete(nid):
    notes = load()
    new = [n for n in notes if n['id'] != nid]
    if len(new) == len(notes):
        print('Not found')
        return
    save(new)
    print('Deleted', nid)


def edit(nid, title, content, tags):
    notes = load()
    for n in notes:
        if n['id'] == nid:
            if title:
                n['title'] = title
            if content:
                n['content'] = content
            if tags is not None:
                n['tags'] = tags
            save(notes)
            print('Updated', nid)
            return
    print('Not found')


def parse_args():
    p = argparse.ArgumentParser(description='Notes manager')
    sub = p.add_subparsers(dest='cmd')
    a = sub.add_parser('add')
    a.add_argument('title')
    a.add_argument('content')
    a.add_argument('--tags', default='')
    sub.add_parser('list')
    f = sub.add_parser('find')
    f.add_argument('term')
    d = sub.add_parser('delete')
    d.add_argument('id', type=int)
    e = sub.add_parser('edit')
    e.add_argument('id', type=int)
    e.add_argument('--title')
    e.add_argument('--content')
    e.add_argument('--tags')
    return p.parse_args()


def main():
    args = parse_args()
    if args.cmd == 'add':
        tags = [t.strip() for t in args.tags.split(',')] if args.tags else []
        add(args.title, args.content, tags)
    elif args.cmd == 'list':
        list_notes()
    elif args.cmd == 'find':
        find(args.term)
    elif args.cmd == 'delete':
        delete(args.id)
    elif args.cmd == 'edit':
        tags = [t.strip() for t in args.tags.split(',')] if args.tags is not None else None
        edit(args.id, args.title, args.content, tags)
    else:
        print('No command. Use -h for help')


if __name__ == '__main__':
    main()
