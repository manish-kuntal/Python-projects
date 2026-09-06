# 16_file_backup_utility

Copy files or directories to a timestamped backup folder.

Usage:
- python backup.py /path/to/file /other/path --dest /backups

What it does:
- Creates a destination folder if missing
- Creates a subfolder backup_YYYYMMDD_HHMMSS and copies files/dirs into it

Improvement suggestion:
- Add incremental backups (hard links) or exclude patterns.
