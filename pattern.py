def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, rows - i + 1):
            print(" ", end="")
        for k in range(1, i + 1):
            print("*", end=" ")
        print()
n = int(input("Enter range :" ))
rows = n
print_pattern(rows)
