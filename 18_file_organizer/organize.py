#!/usr/bin/env python3
"""
File Organizer
Move files from a directory into subfolders based on file extension.
"""

import argparse
from pathlib import Path
import shutil


DEFAULT_MAP = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.md'],
    'Archives': ['.zip', '.tar', '.gz', '.rar'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Video': ['.mp4', '.mov', '.mkv'],
}


def organize(folder: Path, dry=False):
    if not folder.exists() or not folder.is_dir():
        print('Invalid folder')
        return
    for p in folder.iterdir():
        if p.is_dir():
            continue
        ext = p.suffix.lower()
        dest_dir = None
        for name, exts in DEFAULT_MAP.items():
            if ext in exts:
                dest_dir = folder / name
                break
        if dest_dir is None:
            dest_dir = folder / 'Others'
        dest_dir.mkdir(exist_ok=True)
        dest = dest_dir / p.name
        if dry:
            print('Would move', p, '->', dest)
        else:
            shutil.move(str(p), str(dest))
            print('Moved', p, '->', dest)


def main():
    parser = argparse.ArgumentParser(description='Organize files by extension')
    parser.add_argument('folder')
    parser.add_argument('--dry', action='store_true')
    args = parser.parse_args()
    organize(Path(args.folder), dry=args.dry)


if __name__ == '__main__':
    main()
