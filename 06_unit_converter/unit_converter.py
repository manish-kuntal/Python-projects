#!/usr/bin/env python3
"""
Unit Converter
Supports temperature, length, weight, and time conversions via a simple CLI.
"""

import argparse
import sys
from typing import Tuple

# Conversion helpers

# Temperature conversions
def c_to_f(c: float) -> float:
    return c * 9 / 5 + 32

def f_to_c(f: float) -> float:
    return (f - 32) * 5 / 9

def c_to_k(c: float) -> float:
    return c + 273.15

def k_to_c(k: float) -> float:
    return k - 273.15

# Length conversions: convert to meters base
LENGTH_TO_M = {
    'm': 1.0,
    'km': 1000.0,
    'cm': 0.01,
    'mm': 0.001,
    'in': 0.0254,
    'ft': 0.3048,
    'yd': 0.9144,
    'mi': 1609.344,
}

# Weight conversions: base kilogram
WEIGHT_TO_KG = {
    'kg': 1.0,
    'g': 0.001,
    'mg': 0.000001,
    'lb': 0.45359237,
    'oz': 0.028349523125,
}

# Time conversions: base seconds
TIME_TO_S = {
    's': 1.0,
    'sec': 1.0,
    'min': 60.0,
    'h': 3600.0,
    'hr': 3600.0,
    'd': 86400.0,
}


def convert_length(value: float, src: str, dst: str) -> float:
    try:
        m = value * LENGTH_TO_M[src]
        return m / LENGTH_TO_M[dst]
    except KeyError:
        raise ValueError('Unsupported length unit')


def convert_weight(value: float, src: str, dst: str) -> float:
    try:
        kg = value * WEIGHT_TO_KG[src]
        return kg / WEIGHT_TO_KG[dst]
    except KeyError:
        raise ValueError('Unsupported weight unit')


def convert_time(value: float, src: str, dst: str) -> float:
    try:
        s = value * TIME_TO_S[src]
        return s / TIME_TO_S[dst]
    except KeyError:
        raise ValueError('Unsupported time unit')


def convert_temperature(value: float, src: str, dst: str) -> float:
    src = src.lower()
    dst = dst.lower()
    if src == dst:
        return value
    # Normalize to Celsius then convert
    if src in ('c', 'celsius'):
        c = value
    elif src in ('f', 'fahrenheit'):
        c = f_to_c(value)
    elif src in ('k', 'kelvin'):
        c = k_to_c(value)
    else:
        raise ValueError('Unsupported temperature unit')

    if dst in ('c', 'celsius'):
        return c
    if dst in ('f', 'fahrenheit'):
        return c_to_f(c)
    if dst in ('k', 'kelvin'):
        return c_to_k(c)
    raise ValueError('Unsupported temperature unit')


def parse_args():
    p = argparse.ArgumentParser(description='Unit converter: temperature, length, weight, time')
    sub = p.add_subparsers(dest='kind', required=True)

    t = sub.add_parser('temp', help='Temperature conversion')
    t.add_argument('value', type=float)
    t.add_argument('src', type=str)
    t.add_argument('dst', type=str)

    l = sub.add_parser('length', help='Length conversion')
    l.add_argument('value', type=float)
    l.add_argument('src', type=str)
    l.add_argument('dst', type=str)

    w = sub.add_parser('weight', help='Weight conversion')
    w.add_argument('value', type=float)
    w.add_argument('src', type=str)
    w.add_argument('dst', type=str)

    tm = sub.add_parser('time', help='Time conversion')
    tm.add_argument('value', type=float)
    tm.add_argument('src', type=str)
    tm.add_argument('dst', type=str)

    return p.parse_args()


def main():
    args = parse_args()
    try:
        if args.kind == 'temp':
            out = convert_temperature(args.value, args.src, args.dst)
        elif args.kind == 'length':
            out = convert_length(args.value, args.src, args.dst)
        elif args.kind == 'weight':
            out = convert_weight(args.value, args.src, args.dst)
        elif args.kind == 'time':
            out = convert_time(args.value, args.src, args.dst)
        else:
            raise ValueError('Unknown conversion type')
    except ValueError as e:
        print('Error:', e)
        sys.exit(2)
    print(f"{args.value} {args.src} = {out} {args.dst}")


if __name__ == '__main__':
    main()
