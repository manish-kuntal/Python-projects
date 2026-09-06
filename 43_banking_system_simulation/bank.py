#!/usr/bin/env python3
"""
Banking System Simulation
Simple account management with deposits, withdrawals and transaction history persisted to JSON.
"""

import json
from pathlib import Path
from datetime import datetime

DB = Path(__file__).parent / 'bank.json'


def load():
    if not DB.exists():
        return {'accounts': []}
    try:
        return json.loads(DB.read_text(encoding='utf-8'))
    except Exception:
        return {'accounts': []}


def save(data):
    DB.write_text(json.dumps(data, indent=2), encoding='utf-8')


def create_account(name):
    data = load()
    aid = max((a['id'] for a in data['accounts']), default=0) + 1
    account = {'id': aid, 'name': name, 'balance': 0.0, 'transactions': []}
    data['accounts'].append(account)
    save(data)
    print('Created account', aid)


def find_account(aid):
    data = load()
    return next((a for a in data['accounts'] if a['id']==aid), None)


def deposit(aid, amount):
    data = load()
    acc = next((a for a in data['accounts'] if a['id']==aid), None)
    if not acc:
        print('Account not found')
        return
    acc['balance'] += amount
    acc['transactions'].append({'type':'deposit','amount': amount, 'time': datetime.now().isoformat()})
    save(data)
    print('Deposited', amount)


def withdraw(aid, amount):
    data = load()
    acc = next((a for a in data['accounts'] if a['id']==aid), None)
    if not acc:
        print('Account not found')
        return
    if acc['balance'] < amount:
        print('Insufficient funds')
        return
    acc['balance'] -= amount
    acc['transactions'].append({'type':'withdraw','amount': amount, 'time': datetime.now().isoformat()})
    save(data)
    print('Withdrew', amount)


def statement(aid):
    acc = find_account(aid)
    if not acc:
        print('Account not found')
        return
    print(f"Account {acc['id']} - {acc['name']} - Balance: {acc['balance']}")
    for t in acc['transactions']:
        print(t)

if __name__ == '__main__':
    # Demo run
    create_account('Demo User')
    deposit(1, 100.0)
    withdraw(1, 30.0)
    statement(1)
