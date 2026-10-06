temperature = float(input("Enter a temperature in celsius: "))

if temperature < 0:
    print("It is freezing.")
elif temperature <= 20:
    print("It is cold.")
elif temperature <= 30:
    print("It is warm.")
elif temperature > 30:
    print("It is hot.")