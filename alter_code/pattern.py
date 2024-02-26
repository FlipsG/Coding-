def generate_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print(i, end="")
        print()

# Taking user input for the number of rows
num_rows = int(input("Enter the number of rows: "))

# Generating the pattern
generate_pattern(num_rows)

