from abc import ABC,abstractmethod
class shape(ABC):
    l=5
    b=4
    @abstractmethod
    def calc_area(self,length,bredth):
        pass
class rect(shape):
    def calc_area(self,length,bredth):
        self.l=length
        self.b=bredth
        area=self.l*self.b
        return area
class square(shape):
    def calc_area(self,length,bredth):
        self.l=length
        area=self.l**2
        return area
rec=rect()
sq=square()
print(f"{rec.calc_area(10,20)} is the area of the rectangle with dimensions 10 and 20")
print(f"{sq.calc_area(10,10)} is the area of the square with length 10 ")

