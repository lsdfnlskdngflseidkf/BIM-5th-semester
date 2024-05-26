a=int(input('Enter the first Number:'))
b=int(input("Enter the Second number:"))
c=int(input("Enter the Third number:"))
if(a>b):
    if(a>c):
        print(a)
    elif(c>a):
        print(c)
elif(b>a):
    if(b>c):
        print(b)
    elif(c>b):
        print(c)