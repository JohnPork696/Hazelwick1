# Ask the user to enter a number.​
# Add the number to a running total.​
# Repeat the above steps until the total is 100 or more.​
# Output the final total.​

total = 0
while total < 100:
    num = int(input("Enter a whole number: "))
    total = num + total
    if total <= 100:
        print(f"You need {100 - total} more.")
    else:
        print("Total is 100 or more.")