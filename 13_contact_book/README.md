# 13_contact_book

A minimal contact book with JSON persistence and optional CSV import/export.

Usage examples:
- Add: python contacts.py add "Alice" 555-1234 --email alice@example.com
- List: python contacts.py list
- Search: python contacts.py search Alice
- Update: python contacts.py update 1 --phone 555-5678
- Import CSV: python contacts.py import contacts.csv
- Export CSV: python contacts.py export out.csv

Improvement suggestion:
- Encrypt the stored contacts using a password-derived key.
