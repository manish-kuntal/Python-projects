#!/usr/bin/env python3
"""
Quiz Application
Loads questions from questions.json and runs a multiple-choice quiz.
"""

import json
import random
import sys
from pathlib import Path

HERE = Path(__file__).parent
QUESTIONS_FILE = HERE / 'questions.json'


def load_questions(path: Path):
    try:
        with path.open('r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print('Questions file not found.')
        return []
    except json.JSONDecodeError:
        print('Invalid JSON in questions file.')
        return []


def run_quiz(questions):
    if not questions:
        print('No questions available.')
        return
    score = 0
    random.shuffle(questions)
    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        for idx, opt in enumerate(q['options'], start=1):
            print(f"  {idx}) {opt}")
        while True:
            ans = input('Your answer (number): ').strip()
            if ans.isdigit() and 1 <= int(ans) <= len(q['options']):
                break
            print('Please enter the option number.')
        if int(ans) - 1 == q.get('answer'):
            print('Correct!')
            score += 1
        else:
            correct_opt = q['options'][q.get('answer')]
            print('Incorrect. Correct answer:', correct_opt)
    print(f"\nQuiz complete. Score: {score}/{len(questions)}")


def main():
    questions = load_questions(QUESTIONS_FILE)
    run_quiz(questions)


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print('\nExiting.')
        sys.exit(0)
