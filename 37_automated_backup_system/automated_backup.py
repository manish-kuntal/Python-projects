#!/usr/bin/env python3
"""
Automated Backup System
Create timestamped backups and optionally remove backups older than a retention period.
Designed to be run from cron or a scheduled task.
"""

import argparse
from pathlib import Path
from datetime import datetime, timedelta
import shutil
import os


def create_backup(sources, dest):
    dest = Path(dest).expanduser().resolve()
    dest.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    root = dest / f'backup_{ts}'
    root.mkdir()
    for s in sources:
        src = Path(s)
        if not src.exists():
            print('Skipping missing:', src)
            continue
        target = root / src.name
        if src.is_dir():
            shutil.copytree(src, target)
        else:
            shutil.copy2(src, target)
        print('Backed up', src)
    return root


def cleanup_backups(dest, keep_days):
    dest = Path(dest).expanduser().resolve()
    if not dest.exists():
        return
    cutoff = datetime.now() - timedelta(days=keep_days)
    for p in dest.iterdir():
        if p.is_dir() and p.name.startswith('backup_'):
            # parse timestamp
            try:
                ts = datetime.strptime(p.name.replace('backup_', ''), '%Y%m%d_%H%M%S')
            except Exception:
                continue
            if ts < cutoff:
                print('Removing old backup', p)
                shutil.rmtree(p)


def parse_args():
    p = argparse.ArgumentParser(description='Automated backup utility')
    p.add_argument('sources', nargs='+', help='Files or directories to back up')
    p.add_argument('--dest', required=True, help='Backup root destination')
    p.add_argument('--keep-days', type=int, default=30, help='Remove backups older than this')
    return p.parse_args()


def main():
    args = parse_args()
    root = create_backup(args.sources, args.dest)
    print('Created backup at', root)
    if args.keep_days > 0:
        cleanup_backups(args.dest, args.keep_days)


if __name__ == '__main__':
    main()
