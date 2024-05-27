inp=int(input("Enter a Number:"))
start=3
count=0
while(start<=inp/2):
    if(inp%start==0):
        print("The Number is Composite Number")
        exit();
    else:
        count=0
    start+=1
if(count==0):
    print("The number is prime")