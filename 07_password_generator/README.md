# 07_password_generator

Generate secure passwords using Python's `secrets` module.

Usage:
- python generator.py --length 20
- python generator.py --no-special --no-upper

Project architecture:
- Single script `generator.py` with `generate()` as the main function.

Python concepts used:
- secrets, argparse, string constants, input validation.

Possible improvement:
- Add an option to copy generated password to clipboard (pyperclip) when available.
