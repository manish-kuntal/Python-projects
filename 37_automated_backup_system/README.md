# 37_automated_backup_system

Create timestamped backups and optionally remove backups older than a retention period. Intended to be run from cron.

Usage:
- python automated_backup.py /home/user/Documents --dest /backups --keep-days 14

Possible improvement:
- Add incremental backups (rsync) or use hard-links to save space.
