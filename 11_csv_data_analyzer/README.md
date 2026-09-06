# 11_csv_data_analyzer

Simple CSV data analyzer that prints basic summaries for columns.

Usage:
- python csv_analyzer.py data.csv

What it does:
- Prints number of rows
- For each column: guesses type (numeric/text/empty), counts missing values
- For numeric columns: prints count, mean, min, max
- For text columns: prints a small sample

Improvement suggestion:
- Add histogram plots (matplotlib) and better type inference (dates, booleans).
