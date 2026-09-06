#!/usr/bin/env python3
"""
Image Metadata Viewer
Show basic image info (format, size) and EXIF data when available (uses Pillow).
"""

import sys
from pathlib import Path

try:
    from PIL import Image
    from PIL.ExifTags import TAGS
except Exception:
    Image = None


def exif_dict(img):
    raw = img._getexif()
    if not raw:
        return {}
    out = {}
    for k, v in raw.items():
        name = TAGS.get(k, k)
        out[name] = v
    return out


def analyze(path: Path):
    if Image is None:
        raise RuntimeError('Pillow not installed (pip install Pillow)')
    img = Image.open(path)
    print('Format:', img.format)
    print('Size:', img.size)
    print('Mode:', img.mode)
    ex = exif_dict(img)
    if ex:
        print('\nEXIF data:')
        for k, v in ex.items():
            print(f' {k}: {v}')
    else:
        print('\nNo EXIF data found')


def main():
    if len(sys.argv) < 2:
        print('Usage: python image_meta.py image.jpg')
        return
    path = Path(sys.argv[1])
    if not path.exists():
        print('File not found')
        return
    try:
        analyze(path)
    except Exception as e:
        print('Error:', e)


if __name__ == '__main__':
    main()
