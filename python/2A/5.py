inp=int(input("Enter a Number:"))
start=3
flag=0
if(inp==1):
    print("The number is 1 which is not prime or composite")
while(start<=inp/2):
    if(inp%start==0):
        print("The Number is Composite Number")
        exit()
    else:
        flag=0
    start+=1
if(flag==0):
    print("The number is prime")