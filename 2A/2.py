#WAP that accepts year from a user and checks either it is leap year or not
year=int(input('Enter the year to check:'))
if(year%400==0):
    print("Leap year")
elif(year%100==0):
    print("Not a Leap Year")
elif(year%4==0):
    print("Leap year")
else:
    print("Not a Leap Year")
