def add(*args):
    for a in args:
        sum+=a
    return a
n=int(input("Enter the number of numbers to be added"))
print("Enter the numbers")
z=[]
for i in range(n):
    val=int(input(''))
    z.append(val)
m=tuple(f for f in z)
add(m)