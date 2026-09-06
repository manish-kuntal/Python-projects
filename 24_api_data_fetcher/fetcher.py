#!/usr/bin/env python3
"""
API Data Fetcher
Reusable script to fetch JSON from an API endpoint and pretty-print it.
"""

import sys
import json

try:
    import requests
except Exception:
    print('Install requests: pip install requests')
    sys.exit(1)


def fetch(url: str):
    r = requests.get(url)
    r.raise_for_status()
    try:
        return r.json()
    except ValueError:
        raise ValueError('Response was not valid JSON')


def main():
    if len(sys.argv) < 2:
        print('Usage: python fetcher.py <url>')
        sys.exit(2)
    url = sys.argv[1]
    try:
        data = fetch(url)
    except Exception as e:
        print('Error:', e)
        sys.exit(1)
    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
