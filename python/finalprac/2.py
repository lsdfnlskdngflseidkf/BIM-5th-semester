from tkinter.constants import W
class Time:
    def __init__(self,hour,minute,second):
        if(second>60):
            minute+=second//60
            second=second%60
        if(minute>60):
            hour+=minute//60
            minute=minute%60
        self.hour=hour
        self.minute=minute
        self.second=second
    def __add__(self,ob):
        news=self.second+ob.second
        newm=self.minute+ob.minute
        newh=self.hour+ob.hour
        return Time(newh,newm,news)
    def show(self):
        print(f"{self.hour} hours" )
        print(f"{self.minute} minutes" )
        print(f"{self.second} seconds" )
t1=Time(1,20,40)
t2=Time(2,50,30)
t3=t1+t2
print("First Object")
t1.show()
print("Second Object")
t2.show()
print("Resulting Object")
t3.show()
