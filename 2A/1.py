#WAP to accept two numbers from user and find the greatest amonf them
a=int(input('Enter the first Number:'))
b=int(input("Enter the Second number:"))
if(a>b):
    print(a,end=' ')
    print("is the greatest number")
elif(b>a):
    print(b,end=' ')
    print("is the greatest number")
else:
    print("The numbers are equal")