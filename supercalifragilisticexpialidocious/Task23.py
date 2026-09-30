score = 0

answer = int(input("What is 7 + 5? "))
if answer == 12:
    print("Correct")
    score = score + 1
else:
    print("Wrong, it was 12")

answer = int(input("What is 15 - 8? "))
if answer == 7:
    print("Correct")
    score = score + 1
else:
    print("Wrong, it was 7")

answer = int(input("What is 6 * 4? "))
if answer == 24:
    print("Correct")
    score = score + 1
else:
    print("Wrong, it was 24")

answer = int(input("What is 20 / 5? "))
if answer == 4:
    print("Correct")
    score = score + 1
else:
    print("Wrong, it was 4")

print("You scored", score, "out of 4")