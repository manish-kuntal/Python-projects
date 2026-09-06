# 20_json_database_manager

A tiny JSON "database" manager that stores a list of records, each with a unique `id` field.

Usage examples:
- Create: python db_manager.py create '{"name": "Alice", "age": 30}'
- List: python db_manager.py list
- Find: python db_manager.py find 1
- Update: python db_manager.py update 1 '{"age": 31}'
- Delete: python db_manager.py delete 1

Improvement suggestion:
- Add basic validation schemas and transaction-like write safety (temporary file + atomic replace).
