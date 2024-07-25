class distance:
    def __init__(self,km,m):
        self.km=km
        self.m=m

    def __lt__(one,two):
        return True if one.km<two.km else False

    def __mul__(one,two):
        return distance(one.km*two.km,one.m*two.m)

    def show(self):
        print(f"{self.km} kms and {self.m} meters")
d1=distance(10,1)
d2=distance(20,2)
d3=d1*d2
d3.show( )
if(d1<d2):
    print("d1 is smaller than d2")
else:
    print("d2 is smaller than d1")