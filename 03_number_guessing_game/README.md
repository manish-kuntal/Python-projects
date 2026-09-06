# 03_number_guessing_game

Interactive number guessing game with three difficulty levels.

Features:
- Difficulty levels: easy (1-10), medium (1-50), hard (1-100).
- Attempt tracking and feedback for each guess.
- Simple and interactive CLI.

How to run:
- python game.py

Project architecture:
- Single script `game.py`.
- `play(lower, upper, max_attempts)` handles the guessing loop.
- `choose_difficulty()` requests difficulty from the user.

Python concepts used:
- Random number generation, input validation, loops and control flow.

Possible improvement:
- Add a scoring system that persists best scores to a file.
