def trydiv():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        result = a / b
        print(f"The quotient of {a} / {b} is {result}")
    except ZeroDivisionError:
        print("Zero Division Error!")
        print("Cannot divide by zero")
    except ValueError:
        print("Not a valid number")
    else:
        print("Division successful!")

trydiv()
