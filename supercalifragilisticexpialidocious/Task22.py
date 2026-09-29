age = input("Enter your age: ")
ageint = int(age)
if ageint >= 17:
    print("You are old enough to drive.")
else:
    print(f"You can drive in {17-ageint} years.")