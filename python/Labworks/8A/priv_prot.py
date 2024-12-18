class Person:
    def __init__(self, name, age):
        self._name = name  # Protected attribute
        self.__age = age   # Private attribute

    def display(self):
        print(f"Name: {self._name}")
        print(f"Age: {self.__age}")

class Student(Person):
    def __init__(self, name, age, ID):
        super().__init__(name, age)
        self.SID = ID

    def display(self):
        print(f"Student ID: {self.SID}")
        print(f"Name (from parent class): {self._name}")
        try:
            print(f"Age (protected variable): {self._age}")
        except AttributeError:
            print("Cannot access private data member from child class")

# Object creation and method calls
p1 = Person("Ujwal", 20)
p1.display()

s1 = Student("Anil", 21, 101)
s1.display()
