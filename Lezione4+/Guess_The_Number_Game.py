# Gioele Amendola
# 23/04/2024

# Create a function that generates a random number within a range specified by the user.
# Prompt the user to guess the number within a specified maximum number of attempts.
# Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
# Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.

import random

def generate_number() -> int:
    start_number: int = int(input("\nInsert the start of the range of numbers: "))
    end_number: int = int(input("Insert the end of the range of numbers: "))+1

    return random.randrange(start_number,end_number)

def guessing(number: int = generate_number()):
    max_attempts: int = 3
    guessed: int = 0
    while max_attempts > 0:
        print(f"\nMax attempts: {max_attempts}")
        guessed = int(input("\n\tGuess the number: "))
        if guessed == number:
            print("\nYou Guessed Correctly!\n")
            break
        elif guessed > number+10:
            print("\n\tToo high! (<<)")
        elif guessed > number:
            print("\n\tAlmost! (<)")
        elif guessed < number-10:
            print("\n\tToo low! (>>)")
        else:
            print("\n\tAlmost! (>)")
        max_attempts -= 1
    if max_attempts == 0:
        print("\nYou didn't guess the number!\n")

guessing()

