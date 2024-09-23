# from abc import ABC,abstractmethod
# class Talents(ABC):
#     def p(self,this):
#         print(this)
#     @abstractmethod
#     def abm():
#         pass
# class talented(Talents):
#     def abm(self):
#         print("Hello World!")

# obj=talented()
# obj.abm()
# obj.p('that')

# with open('filename.txt','r') as this:
#     that=this.read()
#     print(that)

# import os
# folder="/home/nullproj/Documents/BIM-5th-semester/python/afolder"
# os.mkdir(folder)
# thsi=os.getcwd()
# print(thsi)
# os.chdir(folder)
# thsi=os.getcwd()
# print(thsi)



first=38
sec=26
def add(a,b):
    return (a%10)+ (b%10)
val=add(first,sec)
print(f"The sum of {first} and {sec} is {val}")
