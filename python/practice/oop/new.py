class car:
    country="Nepal"
    def setdetail(self,b,m):
        self.brand=b
        self.model=m

    def changecountry(self,c):
        self.country=c
    @classmethod
    def chgcoun(cls):
        cls.country="USA"
    def show(self):
        print(f"Country:{self.country}\nBrand:{self.brand}\nModel:{self.model}\n\n")

car1=car()
car2=car()
car1.setdetail("BMW","Coupe")
car1.show()
car2.setdetail("BMW","coupe")
car2.show()
car1.changecountry("Germany")
car1.show()
car.chgcoun()
car1.show()
car2.show()