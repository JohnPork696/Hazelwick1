# Print a 3 x 3 grid of numbers like this:​
# 1 2 3
# 1 2 3
# 1 2 3

row = 1

while row <= 3:
    col = 1
    while col <= 3:
        print(col, end=" ")
        col += 1
    print()
    row += 1