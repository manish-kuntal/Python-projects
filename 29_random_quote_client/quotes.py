#!/usr/bin/env python3
"""
Random Quote Client
Fetch random quotes from quotable.io and allow saving favorites locally.
"""

import sys
import json
from pathlib import Path

try:
    import requests
except Exception:
    print('Install requests: pip install requests')
    sys.exit(1)

API = 'https://api.quotable.io/random'
FAVS = Path(__file__).parent / 'favorites.json'


def fetch_quote():
    r = requests.get(API)
    r.raise_for_status()
    return r.json()


def save_favorite(quote):
    favs = []
    if FAVS.exists():
        try:
            favs = json.loads(FAVS.read_text(encoding='utf-8'))
        except json.JSONDecodeError:
            favs = []
    favs.append(quote)
    FAVS.write_text(json.dumps(favs, indent=2), encoding='utf-8')


def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'favorites':
        if not FAVS.exists():
            print('No favorites yet')
            return
        print(FAVS.read_text(encoding='utf-8'))
        return
    try:
        q = fetch_quote()
    except Exception as e:
        print('Error:', e)
        sys.exit(1)
    print(f"\"{q.get('content')}\" — {q.get('author')}")
    ans = input('Save to favorites? (y/N): ').strip().lower()
    if ans == 'y':
        save_favorite(q)
        print('Saved')


if __name__ == '__main__':
    main()
