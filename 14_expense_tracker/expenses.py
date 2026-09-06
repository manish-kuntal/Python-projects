#!/usr/bin/env python3
"""
Expense Tracker
Simple expense tracker saving to CSV. Supports add, list, and summary by category.
"""

import argparse
import csv
from datetime import datetime
from pathlib import Path
import sys

CSV = Path(__file__).parent / 'expenses.csv'
FIELDNAMES = ['date','amount','category','note']


def add(amount, category, note=''):
    row = {'date': datetime.now().isoformat(), 'amount': f'{amount:.2f}', 'category': category, 'note': note}
    newfile = not CSV.exists()
    with CSV.open('a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        if newfile:
            writer.writeheader()
        writer.writerow(row)
    print('Added expense')


def list_all():
    if not CSV.exists():
        print('No expenses recorded')
        return
    with CSV.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            print(f"{r['date']}: {r['amount']} ({r['category']}) - {r['note']}")


def summary():
    if not CSV.exists():
        print('No expenses')
        return
    totals = {}
    total_all = 0.0
    with CSV.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            amt = float(r['amount'])
            cat = r['category']
            totals[cat] = totals.get(cat, 0.0) + amt
            total_all += amt
    print('Totals by category:')
    for cat, t in totals.items():
        print(f' {cat}: {t:.2f}')
    print(f'Total: {total_all:.2f}')


def parse_args():
    p = argparse.ArgumentParser(description='Expense tracker')
    sub = p.add_subparsers(dest='cmd')
    a = sub.add_parser('add')
    a.add_argument('amount', type=float)
    a.add_argument('category')
    a.add_argument('--note', default='')
    sub.add_parser('list')
    sub.add_parser('summary')
    return p.parse_args()


def main():
    args = parse_args()
    if args.cmd == 'add':
        add(args.amount, args.category, args.note)
    elif args.cmd == 'list':
        list_all()
    elif args.cmd == 'summary':
        summary()
    else:
        print('No command. Use -h for help')


if __name__ == '__main__':
    main()
