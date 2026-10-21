print("Make sure you type a whole number!")
length1 = int(input("Enter the first side: "))
length2 = int(input("Enter the second side: "))
length3 = int(input("Enter the base: "))

if length1 == length2 and length2 == length3:
    print("Your triangle is an equilateral.")
elif length1 == length2:
    print("Your triangle is an isosceles.")
elif length1 != length2:
    print("Your triangle is a scalene.")