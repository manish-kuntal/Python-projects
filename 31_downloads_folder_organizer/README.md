# 31_downloads_folder_organizer

Organize a Downloads folder into subfolders by file type (Images, Documents, Archives, etc.).

Usage examples:
- Dry run: python organize_downloads.py --dry
- Organize a custom folder: python organize_downloads.py ~/my_downloads
- Undo last move: python organize_downloads.py --undo

Notes:
- The script writes `.last_move.json` to the target folder for a best-effort undo. Undo works only if files haven't been modified elsewhere.

Possible improvement:
- Add a UI to preview and selectively move files before applying changes.
