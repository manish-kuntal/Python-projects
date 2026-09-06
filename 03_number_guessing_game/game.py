#!/usr/bin/env python3
"""
Number Guessing Game
Interactive game with difficulty levels and attempt tracking.
"""

import random
import sys

DIFFICULTIES = {
    'easy': (1, 10, 6),
    'medium': (1, 50, 8),
    'hard': (1, 100, 10),
}


def play(lower: int, upper: int, max_attempts: int):
    target = random.randint(lower, upper)
    attempts = 0
    print(f"I'm thinking of a number between {lower} and {upper}. You have {max_attempts} attempts.")
    while attempts < max_attempts:
        attempts += 1
        try:
            guess = int(input(f"Attempt {attempts}/{max_attempts} - Your guess: "))
        except ValueError:
            print('Please enter an integer.')
            attempts -= 1
            continue
        if guess == target:
            print(f'Correct! You guessed it in {attempts} attempts.')
            return True
        if guess < target:
            print('Too low.')
        else:
            print('Too high.')
    print(f'Sorry — you ran out of attempts. The number was {target}.')
    return False


def choose_difficulty():
    print('Choose difficulty: easy, medium, hard')
    while True:
        choice = input('Difficulty: ').strip().lower()
        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]
        print('Invalid choice. Pick easy, medium, or hard.')


def main():
    print('Number Guessing Game')
    while True:
        lower, upper, attempts = choose_difficulty()
        play(lower, upper, attempts)
        again = input('Play again? (y/n): ').strip().lower()
        if again != 'y':
            print('Thanks for playing!')
            return


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print('\nExiting.')
        sys.exit(0)
