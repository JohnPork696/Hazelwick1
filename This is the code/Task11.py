number = input("Enter the first number: ")
number1 = int(number)

number = input("Enter the second number: ")
number2 = int(number)

whole = number1 // number2
remainder = number1 % number2

print(f"{number2} goes into {number1} {whole} times with a remainder of {remainder}")