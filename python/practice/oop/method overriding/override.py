'''Write a base class Person with a method introduce() that prints "Hi, I'm a person." Create a subclass Student that overrides introduce() to print "Hi, I'm a student" but also calls the introduce() method from the Person class using super(). Instantiate the Student class and call introduce().
'''
class person:
    def introduce(self):
        print("Hi, I'm a person")
class student(person):
    def introduce(self):
        print("Hi, I'm a student")
        super().introduce()
ob1=student()
ob1.introduce()