#!/usr/bin/env python3
"""
Data Visualization Project
Load a CSV, compute a couple insights, and generate charts with matplotlib and pandas.
"""

import sys
from pathlib import Path

try:
    import pandas as pd
    import matplotlib.pyplot as plt
except Exception:
    print('Install: pip install pandas matplotlib')
    sys.exit(1)


def analyze(csv_path):
    df = pd.read_csv(csv_path)
    print('Rows:', len(df))
    print('Columns:', df.columns.tolist())
    numeric = df.select_dtypes(include='number')
    print('Numeric columns:', numeric.columns.tolist())
    if not numeric.empty:
        desc = numeric.describe()
        print(desc)
        for col in numeric.columns[:2]:
            plt.figure()
            df[col].hist()
            plt.title(col)
            out = Path(csv_path).with_suffix(f'.{col}.png')
            plt.savefig(out)
            print('Saved chart to', out)


def main():
    if len(sys.argv) < 2:
        print('Usage: python visualize.py data.csv')
        sys.exit(2)
    analyze(sys.argv[1])

if __name__ == '__main__':
    main()
