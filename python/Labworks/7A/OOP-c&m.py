'''Create a class car that has:
class attribute: country=Nepal
Initialize a instance method 'setdetail' that accepts b and m as attributes and sets brand = b and model = m
Define a instance method 'changecountry' that accepts 'c' and sets the country = c for the particular object.
Define a class method 'chgcoun' that modifies the country attribute for all the objects as 'USA'.
Write a function 'show' to display the country, brand, model of an object.
Create an object car1 and car2.
Set the brand and model of car1 to 'BMW' and 'coupe' respectively and display them
Repeat step 7 for car2 also.
Change the country of car2 to Germany and display it.
Change the country variable of all the objects to USA and print both car1 and car2'''
class Car:
    country = "Nepal"

    def setdetail(self, b, m):
        self.brand = b
        self.model = m

    def changecountry(self, c):
        Car.country = c  # Change the class attribute, not the instance attribute

    @classmethod
    def chgcoun(cls):
        cls.country = "USA"

    def show(self):
        print(f"Country: {self.country}\nBrand: {self.brand}\nModel: {self.model}\n\n")

# Create car1 and car2
car1 = Car()
car2 = Car()

# Set details for car1 and car2
car1.setdetail("BMW", "Coupe")
car1.show()

car2.setdetail("BMW", "Coupe")
car2.show()

# Change country of car1
car1.changecountry("Germany")
car1.show()

# Change country for all instances
Car.chgcoun()
print("After changing country:")
car1.show()
car2.show()
