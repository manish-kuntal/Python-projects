#!/usr/bin/env python3
"""
Bulk File Renamer
Rename many files in a directory using a pattern with a counter.
Patterns supported:
 - prefix: text to prepend
 - suffix: text to append before extension
 - counter: starting number and padding
Dry-run mode shows proposed names.
"""

import argparse
from pathlib import Path


def rename_bulk(folder: Path, prefix: str, suffix: str, start: int, pad: int, dry: bool):
    files = [p for p in folder.iterdir() if p.is_file()]
    files.sort()
    n = start
    for p in files:
        stem = p.stem
        ext = p.suffix
        counter = str(n).zfill(pad)
        new_name = f"{prefix}{counter}{suffix}{ext}"
        dest = folder / new_name
        print(p.name, '->', new_name)
        if not dry:
            p.rename(dest)
        n += 1


def parse_args():
    p = argparse.ArgumentParser(description='Bulk file renamer')
    p.add_argument('folder')
    p.add_argument('--prefix', default='')
    p.add_argument('--suffix', default='')
    p.add_argument('--start', type=int, default=1)
    p.add_argument('--pad', type=int, default=3)
    p.add_argument('--dry', action='store_true')
    return p.parse_args()


def main():
    args = parse_args()
    folder = Path(args.folder).expanduser().resolve()
    if not folder.exists() or not folder.is_dir():
        print('Invalid folder')
        return
    rename_bulk(folder, args.prefix, args.suffix, args.start, args.pad, args.dry)


if __name__ == '__main__':
    main()
