# 17_duplicate_file_finder

Detect duplicate files under a directory. By default uses SHA256 hashing (accurate) after grouping by file size.

Usage:
- python dups.py /path/to/search
- python dups.py /path --no-hash  (faster: groups by size only)

Improvement suggestion:
- Add an interactive mode to delete or move duplicates safely after confirmation.
