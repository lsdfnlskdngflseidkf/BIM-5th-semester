class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def viewdetail(self):
        print(f"Name:{self.name}\nAge:{self.age}")
p1=person("Ujwal",20)
p1.show()