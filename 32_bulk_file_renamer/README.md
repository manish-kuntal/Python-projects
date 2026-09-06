# 32_bulk_file_renamer

Rename many files in a directory using a predictable pattern.

Usage examples:
- Preview: python renamer.py ./photos --prefix img_ --start 1 --pad 4 --dry
- Apply: python renamer.py ./photos --prefix img_ --start 1 --pad 4

Possible improvement:
- Add pattern tokens (date, original name) and safety checks for name collisions.
