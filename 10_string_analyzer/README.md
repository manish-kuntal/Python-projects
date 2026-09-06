# 10_string_analyzer

Simple string utilities: palindrome check, vowel counts, reverse, and duplicate character detection.

Usage examples:
- Palindrome check: python analyzer.py palindrome "A man a plan" 
- Vowel counts: python analyzer.py vowels "Hello World"
- Reverse: python analyzer.py reverse "Hello"
- Duplicates from stdin: echo "banana" | python analyzer.py duplicates

Project architecture:
- Single script `analyzer.py` providing small helper functions: is_palindrome, vowel_count, reverse_string, duplicate_chars.

Python concepts used:
- argparse, collections.Counter, simple string processing.

Possible improvement:
- Add normalization options (case-insensitive, ignore punctuation) as flags.
