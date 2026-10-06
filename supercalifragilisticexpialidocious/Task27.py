grade = int(input("Enter a number between 0 and 100: "))

if grade >= 90:
    print("Your grade is A.")
elif grade >= 80:
    print("Your grade is B.")
elif grade >= 70:
    print("Your grade is C.")
elif grade >= 60:
    print("Your grade is D.")
elif grade < 60:
    print("You fail.")