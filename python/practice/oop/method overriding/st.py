from abc import ABC,abstractmethod
class student(ABC):
    def __init__(self,name,roll,mark1,mark2):
        self.name=name
        self.roll=roll
        self.mark1=mark1
        self.mark2=mark2
    @abstractmethod
    def calculate(self):
        pass
    def show(self):
        print(f"Name:{self.name}\n Roll:{self.name}")
class BIM(student):
    def __init__(self,name,roll,mark1,mark2):
        super().__init__(name,roll,mark1,mark2)
    def calculate(self):
        score=self.mark1+self.mark2
        gpa=score/50
        return gpa
class BSC(student):
    def __init__(self,name,roll,mark1,mark2):
        super().__init__(name,roll,mark1,mark2)
    def calculate(self):
        score=self.mark1+self.mark2
        per=(score/200)*100
        return per
b1=BIM("Ujwal",39,67,89)
b2=BSC("Dipesh",21,98,67)
print(f"{b1.calculate()}")
print(f"{b2.calculate()}")