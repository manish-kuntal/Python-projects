#!/usr/bin/env python3
"""
Password Generator
Generate secure random passwords with configurable length and character sets.
"""

import secrets
import string
import argparse
import sys


def generate(length: int, upper: bool, lower: bool, digits: bool, special: bool) -> str:
    if length <= 0:
        raise ValueError('Length must be positive')
    pool = ''
    if lower:
        pool += string.ascii_lowercase
    if upper:
        pool += string.ascii_uppercase
    if digits:
        pool += string.digits
    if special:
        pool += string.punctuation
    if not pool:
        raise ValueError('At least one character set must be enabled')

    # Ensure at least one character from each chosen class for better entropy
    password_chars = []
    if lower:
        password_chars.append(secrets.choice(string.ascii_lowercase))
    if upper:
        password_chars.append(secrets.choice(string.ascii_uppercase))
    if digits:
        password_chars.append(secrets.choice(string.digits))
    if special:
        password_chars.append(secrets.choice(string.punctuation))

    while len(password_chars) < length:
        password_chars.append(secrets.choice(pool))

    # Shuffle using secrets-level randomness by creating new list
    secrets.SystemRandom().shuffle(password_chars)
    return ''.join(password_chars)


def parse_args():
    p = argparse.ArgumentParser(description='Secure password generator')
    p.add_argument('-n', '--length', type=int, default=16, help='Password length')
    p.add_argument('--no-upper', action='store_true', help='Exclude uppercase')
    p.add_argument('--no-lower', action='store_true', help='Exclude lowercase')
    p.add_argument('--no-digits', action='store_true', help='Exclude digits')
    p.add_argument('--no-special', action='store_true', help='Exclude special characters')
    return p.parse_args()


def main():
    args = parse_args()
    try:
        pwd = generate(
            args.length,
            upper=not args.no_upper,
            lower=not args.no_lower,
            digits=not args.no_digits,
            special=not args.no_special,
        )
    except ValueError as e:
        print('Error:', e)
        sys.exit(2)
    print(pwd)


if __name__ == '__main__':
    main()
