minutes = int(input("Enter a number of minutes: "))

hours = minutes // 60
leftover = minutes % 60

print(minutes, "minutes is", hours, "hours and", leftover, "minutes")