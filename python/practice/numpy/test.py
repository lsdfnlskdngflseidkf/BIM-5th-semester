import numpy as np
lis=[1,23,4,5,6,7,8]
l=[1,2,4,5,6,7,8]
ins=[1,3,4,5,6,7,8]
ls=[1,0,4,5,6,7,8]
ar=np.array(lis)
print(ar)
print(type(ar))
#create an array with 10 zeros
arr=np.zeros(10)
print(arr)
#create an array with 10 ones
thisa=np.ones(10)
print(thisa)
#creating an array with custom values that is filled
ar3=np.full((4),5)
print(ar3)
#2d array
ar2d=np.zeros((2,3))
print(ar2d)

#array with range
first=np.arange(0,5,1)
print(first)
sec=np.arange(1,8,2)
print(sec)
thi=np.arange(-7,2,2)
print(thi)
fou=np.arange(0.4,1,0.15)
print(fou)

#random number ganerator
a4=np.random.rand(9)*5
print(a4)
