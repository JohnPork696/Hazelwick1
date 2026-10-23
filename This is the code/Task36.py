# Generate a random number between 1 and 100​.
# Ask the user to guess the number.​
# Let the user know if their guess was too high or too low.​
# End the loop when they either guess correct (win) or use up 10 attempts (lose).​
# Tell them if they won or lost.​

import random

number = random.randint(1, 100)
attempts = 0
guess = 0

while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    if guess != number:
        if guess < number:
            print("The number is too low!")
        else:
            print("The number is too high!")
    if guess == number:
        print(f"You correctly guessed {number} in {attempts} attempts!")