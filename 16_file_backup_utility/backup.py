#!/usr/bin/env python3
"""
File Backup Utility
Copy selected files or folders to a backup location safely. Creates timestamped backup directories.
"""

import argparse
import shutil
from pathlib import Path
from datetime import datetime
import sys


def backup(paths, dest):
    dest = Path(dest)
    if not dest.exists():
        dest.mkdir(parents=True)
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    root = dest / f'backup_{ts}'
    root.mkdir()
    for p in paths:
        src = Path(p)
        if not src.exists():
            print('Skipping missing:', src)
            continue
        try:
            if src.is_dir():
                shutil.copytree(src, root / src.name)
            else:
                shutil.copy2(src, root / src.name)
            print('Backed up', src)
        except Exception as e:
            print('Failed to back up', src, e)


def parse_args():
    p = argparse.ArgumentParser(description='Backup files/folders to destination')
    p.add_argument('paths', nargs='+', help='Files or dirs to back up')
    p.add_argument('--dest', required=True, help='Backup destination directory')
    return p.parse_args()


def main():
    args = parse_args()
    backup(args.paths, args.dest)


if __name__ == '__main__':
    main()
