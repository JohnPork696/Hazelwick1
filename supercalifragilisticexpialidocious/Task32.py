number = int(input("Enter a number: "))

if number % 3 == 0:
    print("Divisible by 3.")
if number % 5 == 0:
    print("Divisible by 5.")
if number % 7 == 0:
    print("Divisible by 7.")
if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
    print("Not divisible by 3, 5 or 7.")