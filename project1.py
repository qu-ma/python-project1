#!/usr/bin/python3

# Import the random module, crayons, and art
import random
import crayons
from art import *

# Docstring sharing some information about the Python script
""" Guess the number game! """

# Define the main function
def main():

    # Print out some welcome text, and some instructions on how to play the game
    print(f"{crayons.magenta('Welcome to Guess the Number Game!', bold = True)}")
    print(f"{crayons.yellow('How to play:')}")
    print(f"\t{crayons.green('➜')} {crayons.blue('Guess a number from 1 to 10.')}")
    print(f"\t{crayons.green('➜')} {crayons.blue('Input must be a numeric digit. Characters are not allowed.')}\n")

    # Generate a random number, convert it to a string, save it in the variable 'target'
    target = str(random.randrange(1, 11))

    # Keep track of number of guesses
    number_of_guesses = 0

    # Loop until user has finished guessing 5 times
    while number_of_guesses != 5:
        # Ask for user input
        guess = input("Guess a number from 1 - 10: ")

        # Increase number of guesses by 1
        number_of_guesses += 1

        # Check if number of guesses is 5 and the guess is not equal to the target number
        if number_of_guesses == 5 and guess != target:
            # print(f"You've guessed {number_of_guesses} times and didn't guess correctly. Game Over!")\
            tprint("GAME OVER!", font = "tarty1")

            colors = ["red", "green", "yellow", "blue", "black", "magenta", "cyan", "white"]
            randColor = random.randrange(0, len(colors))
        
        # Check if guess is not a digit
        elif not guess.isdigit():
            print("Please enter a number\n")

        # Check if guess is correct
        elif guess == target:
            print(f"Congratulations, your guess of {guess} is correct!")
            break
        
        # If guess is incorrect, then prompt to guess again
        else:
            print(f"{crayons.red('Incorrect, please guess again')}\n")

# If conditional that calls the main function
if __name__ == "__main__":
    main()





