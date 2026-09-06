# 02_password_strength_analyzer

Analyze password strength and provide actionable feedback.

Features:
- Checks for length, uppercase, lowercase, digits, and special characters.
- Provides a simple entropy estimate and suggestions to improve the password.
- Uses hidden input (getpass) so typed passwords are not shown on the terminal.

How to run:
1. From this folder run: python analyzer.py
2. Enter the password when prompted (input is hidden).

Project architecture:
- Single script `analyzer.py`.
- `analyze(password)` returns a dictionary with properties and suggestions.
- `print_report(report)` displays a human-friendly summary.

Python concepts used:
- Regular expressions (re), string utilities, math for entropy estimate.
- Simple scoring heuristics and input handling.

Possible small improvement you can try:
- Add a command-line option to analyze multiple passwords from a file.
