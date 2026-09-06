#!/usr/bin/env python3
"""
API Response Analyzer
Analyze JSON responses (from URL or file) and summarize structure: keys, types, depth.
"""

import sys
import json
from collections import Counter
from pathlib import Path

try:
    import requests
except Exception:
    print('Install requests: pip install requests')
    sys.exit(1)


def walk(obj, depth=0, types=None, max_depth=0):
    if types is None:
        types = Counter()
    types[type(obj).__name__] += 1
    max_depth = max(max_depth, depth)
    if isinstance(obj, dict):
        for v in obj.values():
            max_depth = max(max_depth, walk(v, depth+1, types, max_depth))
    elif isinstance(obj, list):
        for v in obj:
            max_depth = max(max_depth, walk(v, depth+1, types, max_depth))
    return max_depth


def analyze(data):
    types = Counter()
    max_depth = walk(data, 0, types, 0)
    print('Top-level type:', type(data).__name__)
    print('Element type counts:')
    for t, c in types.most_common():
        print(f' {t}: {c}')
    print('Max nesting depth:', max_depth)


def main():
    if len(sys.argv) < 2:
        print('Usage: python analyzer.py <url-or-file>')
        sys.exit(2)
    src = sys.argv[1]
    try:
        if src.startswith('http://') or src.startswith('https://'):
            r = requests.get(src)
            r.raise_for_status()
            data = r.json()
        else:
            data = json.loads(Path(src).read_text(encoding='utf-8'))
    except Exception as e:
        print('Error loading JSON:', e)
        sys.exit(1)
    analyze(data)


if __name__ == '__main__':
    main()
