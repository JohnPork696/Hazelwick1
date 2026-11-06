# Rewrite the number grid program so that it uses a FOR loop instead of a WHILE loop.

v1 = 1

while v1 <= 3:
    v2 = 1
    while v2 <= 3:
        print(v2, end=" ")
        v2 += 1
    print()
    v1 += 1