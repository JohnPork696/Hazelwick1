# Ask the user to input the height of the rider, in centimetres.
# If needed, ask if they are riding with an adult.
# Outputs whether or not they are allowed to ride.
# Repeats this process until 8 people have been allowed to ride.
count = 0
while count <= 8:
    height = float(input("Enter your height: "))
    if height < 140 and height >= 120:
        ans = input(   )
        if ans == "yes":
            print("You can ride!")
            count = count + 1
        else:
            print("You can't ride.")
    elif height >= 140:
        print("You can ride!")
        count = count + 1
    else:
        print("You can't ride.")
