#!/usr/bin/env python3
"""
Password Strength Analyzer
Reads a password (input hidden) and provides a concise strength report and suggestions.
"""

import re
import string
import math
import getpass
import sys

SPECIAL_CHARS = set(string.punctuation)


def estimate_entropy(length: int, pool_size: int) -> float:
    """Rudimentary entropy estimate in bits: length * log2(pool_size)"""
    if pool_size <= 1 or length <= 0:
        return 0.0
    return length * math.log2(pool_size)


def analyze(password: str) -> dict:
    report = {}
    length = len(password)
    report['length'] = length
    report['has_upper'] = bool(re.search(r'[A-Z]', password))
    report['has_lower'] = bool(re.search(r'[a-z]', password))
    report['has_digit'] = bool(re.search(r'\d', password))
    report['has_special'] = any(c in SPECIAL_CHARS for c in password)

    pool = 0
    if report['has_lower']:
        pool += 26
    if report['has_upper']:
        pool += 26
    if report['has_digit']:
        pool += 10
    if report['has_special']:
        pool += len(SPECIAL_CHARS)

    report['entropy_bits'] = round(estimate_entropy(length, pool), 1)

    # Simple scoring
    score = 0
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    if report['has_upper'] and report['has_lower']:
        score += 1
    if report['has_digit']:
        score += 1
    if report['has_special']:
        score += 1

    report['score'] = score  # 0-6 scale approx

    suggestions = []
    if length < 12:
        suggestions.append('Use at least 12 characters.')
    if not report['has_upper']:
        suggestions.append('Add uppercase letters.')
    if not report['has_lower']:
        suggestions.append('Add lowercase letters.')
    if not report['has_digit']:
        suggestions.append('Include digits.')
    if not report['has_special']:
        suggestions.append('Include special characters (e.g. !@#$%).')
    if 'password' in password.lower() or '123' in password:
        suggestions.append('Avoid common patterns like "password" or "123".')

    report['suggestions'] = suggestions
    return report


def print_report(report: dict):
    print('\nPassword analysis:')
    print(f" Length: {report['length']}")
    print(f" Has upper/lower: {report['has_upper']}/{report['has_lower']}")
    print(f" Has digits: {report['has_digit']}")
    print(f" Has special chars: {report['has_special']}")
    print(f" Estimated entropy (bits): {report['entropy_bits']}")
    print(f" Rough score (higher is better): {report['score']}/6")
    if report['suggestions']:
        print('\nSuggestions:')
        for s in report['suggestions']:
            print(' -', s)


def main():
    print('Password Strength Analyzer')
    try:
        pw = getpass.getpass('Enter password to analyze: ')
    except (KeyboardInterrupt, EOFError):
        print('\nExiting.')
        sys.exit(0)
    if not pw:
        print('No password entered.')
        return
    report = analyze(pw)
    print_report(report)


if __name__ == '__main__':
    main()
