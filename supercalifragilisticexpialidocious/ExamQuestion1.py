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
