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

a5=np.linspace(1,10,7)
print(a5)

a6=array1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(a6)

a7=np.zeros((2, 3))
print(a7)

a8=np.zeros((3,3,6))
print(a8)


a9=np.full((5,5),9)
print(a9)

a10 = np.random.rand(2, 2, 2)
print(a10)

#ndim
print(a10.ndim)

#size
print(a10.size)

#dtype
print(a10.dtype)
#shape
print(a10.shape)
#itemsize
print(a10.itemsize)
#transpose
print(a10.transpose)

#array slicing
another=np.arange(0,11,1)
this=another[5:9]
print(this)

# array reversing using negative slicing
reverse=another[::-1]
print(reverse)


twodar=np.random.randint(10,size=(3,3))
print(twodar)

again=twodar[0:2,0:2]
print(again)

#copying array
on=np.arange(0,99,4) #original array
print(on)

copied=on.copy()
print(copied)

y=on.view()
print(on.base)
print(copied.base)
print(y.base)