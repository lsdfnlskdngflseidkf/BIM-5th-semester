from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Square(Shape):
    def __init__(self, length):
        self.l = length

    def area(self):
        return self.l ** 2

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.l = length
        self.b = breadth

    def area(self):
        return self.l * self.b

class Triangle(Shape):
    def __init__(self, base, height):
        self.b = base
        self.h = height

    def area(self):
        return (1/2) * self.b * self.h

print("Choose the shape:")
print("1. Square")
print("2. Rectangle")
print("3. Triangle")
choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    length = float(input("Enter the length of the square: "))
    shape = Square(length)
    print(f"The area of the square is: {shape.area()}")
elif choice == 2:
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    shape = Rectangle(length, breadth)
    print(f"The area of the rectangle is: {shape.area()}")
elif choice == 3:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    shape = Triangle(base, height)
    print(f"The area of the triangle is: {shape.area()}")
else:
    print("Please enter a valid choice.")
