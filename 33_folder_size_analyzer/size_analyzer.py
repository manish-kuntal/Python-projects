#!/usr/bin/env python3
"""
Folder Size Analyzer
Compute folder sizes and list the top N largest files and subfolders.
"""

import argparse
from pathlib import Path
import os


def human(n):
    for unit in ['B','KB','MB','GB','TB']:
        if n < 1024:
            return f"{n:.1f}{unit}"
        n /= 1024
    return f"{n:.1f}PB"


def folder_size(path: Path):
    total = 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            try:
                fp = Path(dirpath) / f
                total += fp.stat().st_size
            except Exception:
                pass
    return total


def top_files(path: Path, n=10):
    files = []
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            fp = Path(dirpath) / f
            try:
                files.append((fp.stat().st_size, fp))
            except Exception:
                pass
    files.sort(reverse=True)
    return files[:n]


def main():
    p = argparse.ArgumentParser(description='Folder size analyzer')
    p.add_argument('folder')
    p.add_argument('--top', type=int, default=10)
    args = p.parse_args()
    folder = Path(args.folder).expanduser().resolve()
    if not folder.exists():
        print('Folder not found')
        return
    total = folder_size(folder)
    print('Total size:', human(total))
    print('\nTop files:')
    for size, fp in top_files(folder, args.top):
        print(human(size), fp)


if __name__ == '__main__':
    main()
