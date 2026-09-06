#!/usr/bin/env python3
"""
Crypto Price Tracker using CoinGecko API (no API key)
"""

import sys

try:
    import requests
except Exception:
    print('Install requests: pip install requests')
    sys.exit(1)

API = 'https://api.coingecko.com/api/v3/simple/price'


def get_prices(ids: list, vs_currency='usd'):
    params = {'ids': ','.join(ids), 'vs_currencies': vs_currency}
    r = requests.get(API, params=params)
    r.raise_for_status()
    return r.json()


def main():
    if len(sys.argv) < 2:
        print('Usage: python crypto.py bitcoin ethereum')
        sys.exit(2)
    ids = sys.argv[1:]
    try:
        prices = get_prices(ids)
    except Exception as e:
        print('Error:', e)
        sys.exit(1)
    for coin in ids:
        p = prices.get(coin, {})
        print(f"{coin}: {p.get('usd', 'N/A')} USD")


if __name__ == '__main__':
    main()
