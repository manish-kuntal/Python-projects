#!/usr/bin/env python3
"""
URL Status Checker
Check multiple URLs and report HTTP status and response time.
"""

import sys
import time

try:
    import requests
except Exception:
    print('Install requests: pip install requests')
    sys.exit(1)


def check(url: str, timeout=10):
    start = time.time()
    r = requests.get(url, timeout=timeout)
    elapsed = (time.time() - start) * 1000.0
    return r.status_code, elapsed


def main():
    if len(sys.argv) < 2:
        print('Usage: python checker.py url1 url2 ...')
        sys.exit(2)
    for url in sys.argv[1:]:
        try:
            status, ms = check(url)
            print(f"{url}: {status} ({ms:.0f} ms)")
        except Exception as e:
            print(f"{url}: Error: {e}")


if __name__ == '__main__':
    main()
