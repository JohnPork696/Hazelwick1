# A hotel car park charges £4 per hour. If the car is electric, this price is halved to £2 per hour.
# Take as input the number of hours the user has parked and whether their car is electric or not​.
# Calculate and output the total price​.
# Repeat continually until the user enters 0 hours.​

hours = -1
while hours != 0:
    hours = int(input("Enter the number of hours parked (0 to exit): "))
    if hours == 0:
        break
    hours = hours * 4
    electric_car = input("Is your car electric? (yes or no): ")
    if electric_car.lower() == "yes":
        price = hours / 2
    elif electric_car.lower() == "no":
        price = hours
    print(f"The total price is £{price}")