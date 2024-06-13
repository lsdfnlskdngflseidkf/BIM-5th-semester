from enum import Enum

class EnumType(Enum):
    STATIC = 1
    NUMBER = 2
    STRING = 3

def get_output(enum_value, second_arg):
    def print_pyramid(pyramid_value, max_rows=9):
        for i in range(1, max_rows, 2):
            spaces = int((max_rows - i) / 2)
            for j in range(spaces):
                print(" ", end='')
            for j in range(i):
                print(pyramid_value[j], end='')
            print()

    if enum_value == EnumType.STATIC:
        print_pyramid([second_arg] * 9)
    elif enum_value == EnumType.NUMBER:
        print_pyramid([str(second_arg + j) for j in range(9)])
    elif enum_value == EnumType.STRING:
        print_pyramid(list(second_arg))
    else:
        print("Invalid enumeration value.")

def main():
    while True:
        print("\nSelect an option:")
        print("1. Static character pyramid")
        print("2. Number pyramid")
        print("3. String pyramid")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '4':
            print("Exiting...")
            break

        try:
            enum_value = EnumType(int(choice))
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        if enum_value == EnumType.STATIC:
            char = input("Enter a character: ")
            get_output(enum_value, char)
        elif enum_value == EnumType.NUMBER:
            num = int(input("Enter a starting number: "))
            get_output(enum_value, num)
        elif enum_value == EnumType.STRING:
            string = input("Enter a string: ")
            get_output(enum_value, string)
        else:
            print("Invalid enumeration value.")

if __name__ == "__main__":
    main()