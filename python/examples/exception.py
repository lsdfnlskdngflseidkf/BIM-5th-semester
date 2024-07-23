first=int(input("Enter the first number"))
sec=int(input("Enter the second number"))
try:
    third=first/sec
except:
    print("divide by zero exception occured")
else:
    print(f"The quotient of dividing {first} by {sec} is {third}")