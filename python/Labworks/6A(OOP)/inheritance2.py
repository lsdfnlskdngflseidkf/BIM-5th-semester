class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def viewdetail(self):
        print(f"Name:{self.name}\nAge:{self.age}")

class father(person):
    def __init__(self,Id,name,age):
        self.id=Id
        super().__init__(name,age)
    def view(self):
        print(f"ID:{self.id}")

class child(father):
    def __init__(self,dob,Id,name,age):
        self.dob=dob
        super().__init__(Id,name,age)
    def show(self):
        print(f"DOB:{self.dob}")
c1=child("2023-6-25","F101","Noah",1)
# c1.setdob('2023-6-25')
# c1.setid("F101")
# c1.setdetail("Noah","1")
c1.show()
c1.view()
c1.viewdetail()
