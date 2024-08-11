class gold:
    def __init__(self,tola):
        self.tola=tola
    def __add__(one,two):
        return gold(one.tola+two.tola)
    def show(self):
        print(f"{self.tola} Tola of gold")
o1=gold(100)
o2=gold(40)
o3=o1+o2
o3.show()