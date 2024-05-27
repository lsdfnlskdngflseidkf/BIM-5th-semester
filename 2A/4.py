print("1.Login\n2.Forgot Password\n3.Signup")
choice=int(input("Enter a choice:"))
print(choice)
match(choice):
    case 1:
        print("You Chose to login")
    case 2:
        print("You chose Forgot password")
    case 3:
        print("You chose to sign up")
    case _:
        print("Invalid Choice")