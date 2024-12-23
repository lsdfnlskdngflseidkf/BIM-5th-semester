while True:
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    print("Enter the action you want to perform(1 for add and so on)",end=":")
    print("\n1. Add\n2.Subtract\n3.divide\n4.multiply\n5.exit")
    c=int(input())
    match c:
        case 1:
            print(f"The sum of the numbers is {a+b}")
        case 2:
            print(f"The difference of the numbers is {a-b}")
        case 3:
            print(f"The quotient of the number {a}/{b} is {a/b}")
        case 4:
            print(f"The product of the numbers is {a*b}")
        case 5:
            print("Exiting............")
            break
        case _:
            print("Please enter a valid choice")
            continue
