#!/usr/bin/env python3
"""
Downloads Folder Organizer
Move files from a downloads directory into categorized subfolders.
Creates a small JSON `.last_move.json` mapping for a simple undo.
"""

import argparse
import json
from pathlib import Path
import shutil
from typing import Dict

CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.md', '.odt'],
    'Archives': ['.zip', '.tar', '.gz', '.rar', '.7z'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Video': ['.mp4', '.mkv', '.mov', '.avi'],
    'Programs': ['.exe', '.msi', '.AppImage'],
}

LAST_MAP = '.last_move.json'


def categorize(path: Path) -> str:
    ext = path.suffix.lower()
    for name, exts in CATEGORIES.items():
        if ext in exts:
            return name
    return 'Others'


def organize(folder: Path, dry: bool = False) -> Dict[str, str]:
    mapping = {}
    folder = folder.expanduser().resolve()
    if not folder.exists() or not folder.is_dir():
        raise ValueError('Folder does not exist')
    for p in folder.iterdir():
        if p.is_dir() or p.name == LAST_MAP:
            continue
        cat = categorize(p)
        dest_dir = folder / cat
        dest_dir.mkdir(exist_ok=True)
        dest = dest_dir / p.name
        mapping[str(p)] = str(dest)
        if dry:
            print('Would move', p, '->', dest)
        else:
            shutil.move(str(p), str(dest))
            print('Moved', p.name, '->', dest_dir.name)
    return mapping


def save_map(folder: Path, mapping: Dict[str, str]):
    (folder / LAST_MAP).write_text(json.dumps(mapping, indent=2), encoding='utf-8')


def load_map(folder: Path):
    f = folder / LAST_MAP
    if not f.exists():
        return {}
    try:
        return json.loads(f.read_text(encoding='utf-8'))
    except Exception:
        return {}


def undo(folder: Path):
    mapping = load_map(folder)
    if not mapping:
        print('No last move map found')
        return
    for src, dst in mapping.items():
        src_p = Path(src)
        dst_p = Path(dst)
        # if destination exists and original doesn't, move back
        if dst_p.exists() and not src_p.exists():
            dst_p.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(dst_p), str(src_p))
            print('Moved back', dst_p.name)
    (folder / LAST_MAP).unlink(missing_ok=True)
    print('Undo complete')


def parse_args():
    p = argparse.ArgumentParser(description='Organize Downloads folder into categories')
    p.add_argument('folder', nargs='?', default='~/Downloads')
    p.add_argument('--dry', action='store_true', help='Show what would be done')
    p.add_argument('--undo', action='store_true', help='Undo last organize (best-effort)')
    return p.parse_args()


def main():
    args = parse_args()
    folder = Path(args.folder).expanduser().resolve()
    if args.undo:
        undo(folder)
        return
    mapping = organize(folder, dry=args.dry)
    if not args.dry and mapping:
        save_map(folder, mapping)


if __name__ == '__main__':
    main()
