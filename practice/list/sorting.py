import random
lis=[1,2,3,4,5,6,7,8,9]
random.shuffle(lis)# shuffle a list (needs a specific class to be imported)
print(lis)
lis.sort() #sort a list (method 1)
print(lis)
random.shuffle(lis)# shuffle a list (needs a specific class to be imported)
sorted_lis=sorted(lis) #method 2 of sorting a list