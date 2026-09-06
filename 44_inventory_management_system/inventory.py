#!/usr/bin/env python3
"""
Inventory Management System
Manage products, quantities, and low-stock alerts with JSON persistence.
"""

import json
from pathlib import Path

DB = Path(__file__).parent / 'inventory.json'
LOW_STOCK_THRESHOLD = 5


def load():
    if not DB.exists():
        return []
    return json.loads(DB.read_text(encoding='utf-8'))


def save(products):
    DB.write_text(json.dumps(products, indent=2), encoding='utf-8')


def add_product(name, qty):
    products = load()
    pid = max((p['id'] for p in products), default=0) + 1
    products.append({'id': pid, 'name': name, 'qty': qty})
    save(products)
    print('Added', pid)


def update_stock(pid, qty):
    products = load()
    for p in products:
        if p['id'] == pid:
            p['qty'] = qty
            save(products)
            print('Updated', pid)
            return
    print('Not found')


def list_products():
    for p in load():
        status = 'LOW' if p['qty'] <= LOW_STOCK_THRESHOLD else 'OK'
        print(f"{p['id']}: {p['name']} - {p['qty']} ({status})")

if __name__ == '__main__':
    add_product('Widget', 10)
    add_product('Gadget', 3)
    list_products()
