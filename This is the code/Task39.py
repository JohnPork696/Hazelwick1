# Print a grid of coordinate pairs, which looks like this:​
# (1, 1) (1, 2) (1, 3)
# (2, 1) (2, 2) (2, 3)
# (3, 1) (3, 2) (3, 3)

row = 1

while row <= 3:
    col = 1
    while col <= 3:
        print(f"({row}, {col})", end=" ")
        col += 1
    print()
    row += 1