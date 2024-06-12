string="Coronavirus"
for i in range(1, 10, 2):
    spaces = int((9 - i) / 2)  # Calculate spaces before asterisks
    for j in range(spaces):
        print(" ", end='')
    for j in range(i):
        print(f"{string[j]}", end='')
    print("")