#!/usr/bin/env python3
"""
Duplicate File Finder
Find duplicate files by size and optional SHA256 hash.
"""

import argparse
import os
import hashlib
from collections import defaultdict
from pathlib import Path


def file_hash(path, chunk_size=8192):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(chunk_size), b''):
            h.update(chunk)
    return h.hexdigest()


def find_duplicates(root, use_hash=True):
    sizes = defaultdict(list)
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            p = Path(dirpath) / fn
            try:
                sizes[p.stat().st_size].append(p)
            except OSError:
                continue
    duplicates = []
    for size, paths in sizes.items():
        if len(paths) < 2:
            continue
        if use_hash:
            by_hash = defaultdict(list)
            for p in paths:
                try:
                    h = file_hash(p)
                    by_hash[h].append(p)
                except OSError:
                    continue
            for h, ps in by_hash.items():
                if len(ps) > 1:
                    duplicates.append(ps)
        else:
            duplicates.append(paths)
    return duplicates


def main():
    p = argparse.ArgumentParser(description='Find duplicate files')
    p.add_argument('root')
    p.add_argument('--no-hash', action='store_true', help='Group by size only (faster, less accurate)')
    args = p.parse_args()
    dups = find_duplicates(args.root, use_hash=not args.no_hash)
    if not dups:
        print('No duplicates found')
        return
    for group in dups:
        print('\nDuplicate group:')
        for p in group:
            print(' ', p)


if __name__ == '__main__':
    main()
