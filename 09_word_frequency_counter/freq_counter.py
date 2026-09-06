#!/usr/bin/env python3
"""
Word Frequency Counter
Counts word frequency from a file or stdin and prints a sorted list.
"""

import argparse
import sys
import re
from collections import Counter
from pathlib import Path

WORD_RE = re.compile(r"\b[\w']+\b")


def count_words(text: str):
    words = WORD_RE.findall(text.lower())
    return Counter(words)


def parse_args():
    p = argparse.ArgumentParser(description='Word frequency counter')
    p.add_argument('--file', '-f', type=str, help='Path to text file')
    p.add_argument('--top', '-n', type=int, default=50, help='How many top words to show')
    return p.parse_args()


def main():
    args = parse_args()
    if args.file:
        path = Path(args.file)
        if not path.exists():
            print('File not found')
            sys.exit(2)
        text = path.read_text(encoding='utf-8')
    else:
        if sys.stdin.isatty():
            print('Enter/paste text, then Ctrl-D (Unix) or Ctrl-Z (Windows) to finish:')
        text = sys.stdin.read()
    counts = count_words(text)
    for word, cnt in counts.most_common(args.top):
        print(f"{word}\t{cnt}")


if __name__ == '__main__':
    main()
