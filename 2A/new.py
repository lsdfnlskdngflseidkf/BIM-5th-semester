inp=int(input("Enter a Number:"))
start=2
count=90
while(start<=inp/2):
    if(inp%start==0):
        count+=2
    start+=1
if(count==0):
    print("The number is prime")
else:
    print("The number is composite")