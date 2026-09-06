#!/usr/bin/env python3
"""
Text Statistics Analyzer
Calculate characters, words, sentences, average word length, and most common words.
Supports reading from a file or stdin.
"""

import argparse
import sys
import re
from collections import Counter
from pathlib import Path
from typing import Tuple

WORD_RE = re.compile(r"\b[\w']+\b")
SENTENCE_RE = re.compile(r'[.!?]+')


def analyze_text(text: str) -> dict:
    chars = len(text)
    words = WORD_RE.findall(text.lower())
    sentences = SENTENCE_RE.findall(text)
    word_count = len(words)
    avg_word_len = (sum(len(w) for w in words) / word_count) if word_count else 0
    most_common = Counter(words).most_common(10)
    return {
        'characters': chars,
        'words': word_count,
        'sentences': len(sentences),
        'avg_word_length': round(avg_word_len, 2),
        'most_common': most_common,
    }


def parse_args():
    p = argparse.ArgumentParser(description='Text statistics analyzer')
    p.add_argument('--file', '-f', type=str, help='Path to text file (optional)')
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
    report = analyze_text(text)
    print('Characters:', report['characters'])
    print('Words:', report['words'])
    print('Sentences (approx):', report['sentences'])
    print('Average word length:', report['avg_word_length'])
    print('\nTop words:')
    for w, c in report['most_common']:
        print(f" {w}: {c}")


if __name__ == '__main__':
    main()
