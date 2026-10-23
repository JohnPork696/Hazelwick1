# Start the loop using 'while True'
# Generate a random number between 1 and 100​.
# Ask the user to guess the number.​
# Use the break command to end the loop if they win or lose.
# Tell them if they won or lost.​

while True:
    import random
    number = random.randint(1, 100)
    guess = 0

    if guess != number:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < number:
            print("The number is too low!")
            break
        elif guess > number:
            print("The number is too high!")
            break
        else:
            print(f"You correctly guessed {number}!")
            break