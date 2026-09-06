#!/usr/bin/env python3
"""
IP Information Lookup using ip-api.com (no API key)
"""

import sys

try:
    import requests
except Exception:
    print('Install requests: pip install requests')
    sys.exit(1)

API = 'http://ip-api.com/json/'


def lookup(ip_or_host: str):
    r = requests.get(API + ip_or_host)
    r.raise_for_status()
    return r.json()


def main():
    if len(sys.argv) < 2:
        print('Usage: python ip_lookup.py 8.8.8.8')
        sys.exit(2)
    target = sys.argv[1]
    try:
        info = lookup(target)
    except Exception as e:
        print('Error:', e)
        sys.exit(1)
    if info.get('status') != 'success':
        print('Lookup failed:', info.get('message'))
        sys.exit(1)
    keys = ['query','country','regionName','city','isp','org','lat','lon','timezone']
    for k in keys:
        print(f"{k}: {info.get(k)}")


if __name__ == '__main__':
    main()
