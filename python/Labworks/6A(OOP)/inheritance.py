class person:
    def setdetail(self,name,age):
        self.name=name
        self.age=age
    def viewdetail(self):
        print(f"Name:{self.name}\n Age:{self.age}")

class father(person):
    def setid(self,Id):
        self.id=Id
    def view(self):
        print(f"ID:{self.id}")

class child(father):
    def setdob(self,dob):
        self.dob=dob
    def show(self):
        print(f"Age:{self.dob}")
c1=child()
c1.setdob('2023-16-25')
c1.setid("F101")
c1.setdetail("Noah","1")
c1.show()
c1.view()
c1.viewdetail()
