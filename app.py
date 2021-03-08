#!/usr/bin/env python
import click
import datetime
import math
import random

@click.command()
@click.option("--low_num", default = 0)
@click.option("--high_num", default = 100)

def guessing_game(low_num = 0, high_num = 100):
    # Initialize values
    guess = 0
    correct_num = random.randint(low_num, high_num)
    correct = False

    # Ask for guess
    x = input(f'Guess a number between {low_num} and {high_num}. Type "exit" to stop playing. ')

    # Run loop
    while correct == False:
        if x.lower() == 'exit':
            correct = True
            break
        # Convert to integer
        x = int(x)
        # Check conditions
        if x == correct_num:
            guess += 1
            print(f'Congratulations! You correctly guessed {x} in {guess} guesses!')
            correct = True
        elif x < correct_num:
            print(f'Sorry your guess of {x} is too low! Try again.')
            x = input(f'Guess a number between {low_num} and {high_num}. Type "exit" to stop playing. ')
            guess += 1
        else:
            print(f'Sorry your guess of {x} is too high! Try again.')
            x = input(f'Guess a number between {low_num} and {high_num}. Type "exit" to stop playing. ')
            guess += 1

if __name__ == '__main__':
    guessing_game()