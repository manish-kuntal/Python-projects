#!/usr/bin/env python3
"""
PDF Information Extractor
Extract metadata and a small text sample from a PDF using pypdf.
"""

import sys
from pathlib import Path

try:
    from pypdf import PdfReader
except Exception:
    PdfReader = None


def analyze(path: Path):
    if PdfReader is None:
        raise RuntimeError('pypdf not installed (pip install pypdf)')
    reader = PdfReader(str(path))
    info = reader.metadata
    print('Pages:', len(reader.pages))
    print('Metadata:')
    for k, v in info.items():
        print(f' {k}: {v}')
    if len(reader.pages) > 0:
        page = reader.pages[0]
        try:
            text = page.extract_text() or ''
            print('\nText sample (first 500 chars):')
            print(text[:500])
        except Exception:
            print('Could not extract page text')


def main():
    if len(sys.argv) < 2:
        print('Usage: python pdf_info.py file.pdf')
        sys.exit(2)
    p = Path(sys.argv[1])
    if not p.exists():
        print('File not found')
        sys.exit(2)
    try:
        analyze(p)
    except Exception as e:
        print('Error:', e)
        sys.exit(1)


if __name__ == '__main__':
    main()
