#!/usr/bin/env python3
"""
String Analyzer
Provide utilities: palindrome check, vowel count, reverse, duplicate character detection.
"""

import argparse
import sys
from collections import Counter


def is_palindrome(s: str) -> bool:
    filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
    return filtered == filtered[::-1]


def vowel_count(s: str) -> dict:
    vowels = 'aeiou'
    c = Counter(ch.lower() for ch in s if ch.lower() in vowels)
    return dict(c)


def reverse_string(s: str) -> str:
    return s[::-1]


def duplicate_chars(s: str) -> dict:
    c = Counter(s)
    return {ch: cnt for ch, cnt in c.items() if cnt > 1}


def parse_args():
    p = argparse.ArgumentParser(description='String analyzer utilities')
    p.add_argument('command', choices=['palindrome', 'vowels', 'reverse', 'duplicates'])
    p.add_argument('text', nargs='?', help='Text to analyze (if omitted, reads stdin)')
    return p.parse_args()


def main():
    args = parse_args()
    if args.text:
        text = args.text
    else:
        if sys.stdin.isatty():
            print('Enter text, then Ctrl-D/Ctrl-Z:')
        text = sys.stdin.read()
    if args.command == 'palindrome':
        print('Palindrome:' , is_palindrome(text))
    elif args.command == 'vowels':
        vc = vowel_count(text)
        print('Vowel counts:', vc)
    elif args.command == 'reverse':
        print('Reversed:', reverse_string(text))
    elif args.command == 'duplicates':
        print('Duplicate characters:', duplicate_chars(text))


if __name__ == '__main__':
    main()
