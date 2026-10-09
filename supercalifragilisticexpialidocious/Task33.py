import random

score = 0

for i in range(5):
    number = random.randint(0, 100)
    guess = int(input("Round " + str(i + 1) + " - guess a number between 0 and 100: "))

    difference = abs(guess - number)

    if difference == 0:
        print("Bang-on! It was", number)
        score += 10
    elif difference <= 5:
        print("Close! It was", number)
        score += 5
    elif difference <= 10:
        print("Okay! It was", number)
        score += 2
    else:
        print("Way off! It was", number)

print("Your final score is", score, "out of 50")