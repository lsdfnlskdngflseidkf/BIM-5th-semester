#WAP to calculate the factorial of a number
print("\nto calculate the factorial of a number")
def factorial(var):
    fact=1
    if var==0 or var==1:
        return 1
    for i in range(1,var+1):
        fact*=i
    return fact

inp=int(input("Enter the number to calculate the factorial of:"))
print(factorial(inp))