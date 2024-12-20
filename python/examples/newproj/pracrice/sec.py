# #1

# # er=input("Enter a string of text")
# # print(er.upper())
# # print(er.lower())
# # print(er.capitalize())
# #2

# # lis=['meh',1,'i',True,'zehahah']
# # print(lis[1:4])
# #3

# # name=input("Enter your name:")
# # age=int(input("Enter your age:"))
# # print("Hello,{} You are {} years old".format(name,age))

# #4

# # num=int(input("Enter a number:"))
# # if num>0:
# #     if num%2==0:
# #         print("even it is")
# #     elif num%2!=0:
# #         print("odd it is")
# # elif num<0:
# #     if num%2==0:
# #         print("even it is")
# #     elif num%2!=0:
# #         print("odd it is")
# # else:
# #     print("zero it is")

# 5
# li=[]
# print("Number\tSquare")
# for i in range(1,6):
#     li.append(i)
#     print(f"{i}\t{i**2}")

# #6

# # number=11
# # while number>10:
# #     print("The number is greater than 10")
# #     number=int(input("Enter another number:"))

# #7

# # li=[x for x in range(1,11)]
# # li.append(11)
# # print(li)
# # li.pop(1)
# # print(li)
# # #8

# # tu=(1,2,3,4)
# # num1,num2,num3,num4=tu
# # print(num1)
# # print(num2)
# # print(num3)
# # print(num4)

# # #9

# # di={
# #     'name':'ujwal',
# #     'age':'20'
# # }
# # def fun(**dict,name):
# #     for i in di.values()
# # #idk how to

# #10

# # def sum(one,two=0):
# #     return one+two
# # print(sum(10))

# #11

# # def sqc(num):
# #     return num**2,num**3
# # num=5
# # sq,cu=sqc(num)
# # print(f"The squares of number {num} is {sq},{cu}")

# # #12

# # x=lambda a,b:a*b
# # print(x(5,6))

# #13
# class person:
#     name="blah"
#     age=12
#     def greet(cls):
#         print(f"Hello {cls.name}")
# # ob=person()
# # ob.greet()

# class student(person):
#     stdid=101
#     def greet(cls):
#         print(f"Hello {cls.name} with id {cls.stdid}")
#     def display_info(cls):
#         print(f"name:{cls.name}\n age:{cls.age}\nID:{cls.stdid}")

# boo=student()
# boo.display_info()
# boo.greet()
di = {
    'name': 'ujwal',
    'age': 20
}

def get_age(dict_data, name):
    return dict_data.get('age')

print(get_age(di, 'age'))
