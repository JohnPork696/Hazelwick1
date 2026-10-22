# Print a 3 x 3 grid of numbers like this:​
# 1 1 1
# 2 2 2
# 3 3 3

row = 1

while row <= 3:
    col = 1
    while col <= 3:
        print(row, end=" ")
        col += 1
    print()
    row += 1