# create a class person that has a instance method setname tat accepts and sets the name given by the user and also a method to display the name
#create another class studend that has an instance method setdetail that accepts age and class and sets the respective variables
class person:
    # this is the first class
    def setname(self,name):
        self.name=name
    def getall1(self):
        print(f"Name:{self.name}")


class student(person):
    # this is the child class
    def setdetail(self,age,cl):
        self.age=age
        self.cl=cl
    def getall(self):
        print(f"Age:{self.age}\nClass:{self.cl}")
object1=student()
object1.setname("Ujwal")
object1.setdetail(20,"BIM")
object1.getall1();
object1.getall()


