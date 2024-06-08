a = int(input('Enter the first Number: '))
b = int(input('Enter the second Number: '))
c = int(input('Enter the third Number: '))

if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

print(f"The smallest number is: {smallest}")