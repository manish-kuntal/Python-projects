#!/usr/bin/env python3
"""
CSV Data Analyzer
Read a CSV file and provide simple summaries: row count, column types, missing values, and basic numeric stats.
"""
import csv
import sys
from collections import defaultdict
from statistics import mean
from pathlib import Path


def sniff_type(values):
    # Determine if column is numeric (ints/floats) or string
    num_vals = []
    non_empty = 0
    for v in values:
        if v == "":
            continue
        non_empty += 1
        try:
            num_vals.append(float(v))
        except ValueError:
            return 'text'
    return 'numeric' if non_empty else 'empty'


def analyze(path: Path):
    if not path.exists():
        print('File not found')
        return
    with path.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        cols = reader.fieldnames or []
        samples = defaultdict(list)
        missing = defaultdict(int)
        row_count = 0
        for row in reader:
            row_count += 1
            for c in cols:
                val = (row.get(c) or '').strip()
                if val == '':
                    missing[c] += 1
                else:
                    samples[c].append(val)
        print(f'Rows: {row_count}')
        print('Columns:')
        for c in cols:
            col_type = sniff_type(samples[c])
            print(f' - {c}: type={col_type}, missing={missing[c]}')
            if col_type == 'numeric' and samples[c]:
                nums = [float(v) for v in samples[c]]
                print(f"   count={len(nums)}, mean={mean(nums):.3f}, min={min(nums)}, max={max(nums)}")
            elif samples[c]:
                sample_values = samples[c][:5]
                print(f'   sample: {sample_values}')


def main():
    if len(sys.argv) < 2:
        print('Usage: python csv_analyzer.py data.csv')
        sys.exit(2)
    analyze(Path(sys.argv[1]))


if __name__ == '__main__':
    main()
