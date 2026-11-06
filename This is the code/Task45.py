# Rewrite the Higher/Lower game so that it uses a FOR loop instead of a WHILE loop.

import random

v1 = random.randint(1, 100)
v2 = 10

for v3 in range (1, v2 + 1):
    v4 = int(input("Guess a number between 1 and 100: "))
    if v4 < v1:
        print("The number is too low!")
    elif v4 > v1:
        print("The number is too high!")
    if v4 == v1:
        print(f"You correctly guessed {v1} in {v3} attempts!")
        break
else:
    print(f"You ran out of attempts! The number was {v1}.")