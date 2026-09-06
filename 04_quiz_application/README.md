# 04_quiz_application

A simple multiple-choice quiz application that reads questions from `questions.json`.

How it works:
- Questions are stored in `questions.json` as an array of objects with `question`, `options`, and `answer` (index).
- `quiz.py` loads the questions, shuffles them, and prompts the user for answers.
- A final score is shown.

How to run:
- python quiz.py

Suggestions for improvement:
- Add categories and allow selecting a category.
- Add timed questions or persist high scores.
