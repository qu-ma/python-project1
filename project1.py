#!/usr/bin/python3

# Import the random module
import random

# Docstring sharing some information about the Python script
""" Guess the number game! """

# Define the main function
def main():

    # Print out some welcome text, and some instructions on how to play the game
    print("Welcome to Guess the Number Game!")
    print("Guess a number from 1 to 100.")
    print("Input must be a numeric digit. Characters are not allowed.\n")

    # Generate a random number, convert it to a string, save it in the variable 'target'
    target = str(random.randrange(1, 101))

    # Keep track of number of guesses
    number_of_guesses = 0

    # Loop until user has finished guessing 5 times
    while number_of_guesses != 5:
        # Ask for user input
        guess = input("Guess a number from 1 - 100: ")

        # Increase number of guesses by 1
        number_of_guesses += 1

        # Check if number of guesses is 5 and the guess is not equal to the target number
        if number_of_guesses == 5 and guess != target:
            print(f"You've guessed {number_of_guesses} times and didn't guess correctly. Game Over!")
            break
        
        # Check if guess is not a digit
        elif not guess.isdigit():
            print("Please enter a number")

        # Check if guess is correct
        elif guess == target:
            print(f"Congratulations, your guess of {guess} is correct!")
            break
        
        # If guess is incorrect, then prompt to guess again
        else:
            print("Incorrect, please guess again")

# If conditional that calls the main function
if __name__ == "__main__":
    main()





