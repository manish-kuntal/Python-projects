#!/usr/bin/env python3
"""
Duplicate Folder Cleaner
Identify duplicate files (by size+hash) under a folder and write a report for review.
"""

import argparse
from pathlib import Path
import os
import hashlib
from collections import defaultdict
import json


def file_hash(path, chunk_size=8192):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(chunk_size), b''):
            h.update(chunk)
    return h.hexdigest()


def find_duplicates(root):
    sizes = defaultdict(list)
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            p = Path(dirpath) / fn
            try:
                sizes[p.stat().st_size].append(p)
            except Exception:
                continue
    report = []
    for size, paths in sizes.items():
        if len(paths) < 2:
            continue
        by_hash = defaultdict(list)
        for p in paths:
            try:
                h = file_hash(p)
                by_hash[h].append(str(p))
            except Exception:
                continue
        for h, group in by_hash.items():
            if len(group) > 1:
                report.append(group)
    return report


def main():
    p = argparse.ArgumentParser(description='Find duplicate files and write a JSON report')
    p.add_argument('root')
    p.add_argument('--out', default='duplicates_report.json')
    args = p.parse_args()
    groups = find_duplicates(args.root)
    Path(args.out).write_text(json.dumps(groups, indent=2), encoding='utf-8')
    print(f'Wrote report with {len(groups)} duplicate groups to', args.out)


if __name__ == '__main__':
    main()
