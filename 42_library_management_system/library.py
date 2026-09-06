#!/usr/bin/env python3
"""
Library Management System (OOP)
Manage books, members, borrowing and returns with simple JSON persistence.
"""

import json
from pathlib import Path
from datetime import datetime

DB = Path(__file__).parent / 'library.json'

class Book:
    def __init__(self, id, title, author, copies=1):
        self.id = id
        self.title = title
        self.author = author
        self.copies = copies

    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'author': self.author, 'copies': self.copies}

class Member:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {'id': self.id, 'name': self.name}

class Library:
    def __init__(self):
        self.data = {'books': [], 'members': [], 'loans': []}
        self.load()

    def load(self):
        if DB.exists():
            try:
                self.data = json.loads(DB.read_text(encoding='utf-8'))
            except Exception:
                self.data = {'books': [], 'members': [], 'loans': []}

    def save(self):
        DB.write_text(json.dumps(self.data, indent=2), encoding='utf-8')

    def add_book(self, title, author, copies=1):
        bid = max((b['id'] for b in self.data['books']), default=0) + 1
        self.data['books'].append({'id': bid, 'title': title, 'author': author, 'copies': copies})
        self.save()
        return bid

    def add_member(self, name):
        mid = max((m['id'] for m in self.data['members']), default=0) + 1
        self.data['members'].append({'id': mid, 'name': name})
        self.save()
        return mid

    def borrow(self, member_id, book_id):
        book = next((b for b in self.data['books'] if b['id'] == book_id), None)
        if not book or book['copies'] <= 0:
            raise ValueError('Book not available')
        book['copies'] -= 1
        self.data['loans'].append({'member_id': member_id, 'book_id': book_id, 'borrowed': datetime.now().isoformat(), 'returned': None})
        self.save()

    def return_book(self, member_id, book_id):
        loan = next((l for l in self.data['loans'] if l['member_id']==member_id and l['book_id']==book_id and l.get('returned') is None), None)
        if not loan:
            raise ValueError('Loan not found')
        loan['returned'] = datetime.now().isoformat()
        book = next((b for b in self.data['books'] if b['id'] == book_id), None)
        if book:
            book['copies'] += 1
        self.save()

if __name__ == '__main__':
    lib = Library()
    # small demo when run directly
    print('Books:', lib.data['books'])
    print('Members:', lib.data['members'])
    print('Loans:', lib.data['loans'])
