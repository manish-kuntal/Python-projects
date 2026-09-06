#!/usr/bin/env python3
"""
Currency Converter using exchangerate.host (no API key required)
"""

import sys

try:
    import requests
except Exception:
    print('Install requests: pip install requests')
    sys.exit(1)

API = 'https://api.exchangerate.host/convert'


def convert(amount: float, frm: str, to: str):
    params = {'from': frm.upper(), 'to': to.upper(), 'amount': amount}
    r = requests.get(API, params=params)
    r.raise_for_status()
    data = r.json()
    if not data.get('success'):
        raise ValueError('Conversion failed')
    return data.get('result')


def main():
    if len(sys.argv) != 4:
        print('Usage: python convert.py AMOUNT FROM TO\nExample: python convert.py 10 USD EUR')
        sys.exit(2)
    amt = float(sys.argv[1])
    frm = sys.argv[2]
    to = sys.argv[3]
    try:
        res = convert(amt, frm, to)
    except Exception as e:
        print('Error:', e)
        sys.exit(1)
    print(f"{amt} {frm.upper()} = {res} {to.upper()}")


if __name__ == '__main__':
    main()
