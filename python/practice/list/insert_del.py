lis=[1,2,3,4,5,6,7,8,9]
list2=list((1,2,3,4,5,6,7,8,9))
lis.append(10)
# print(lis) #append a single item at the end of the list 
lis.insert(11,34) # add item into the list at a specifi pos with insert
# print(lis)
lis.remove(34) #remove the item from the list using it's value
# print(lis)
lis.pop(1) # remove the last n items from  the list
# print(lis)
del lis[1] # used to remove an item from a specific position in the list 
# print(lis)
# del can be used to remove slices from the list like
del lis[4:7]
# print(lis)
lis.clear()#remove all the items from the list
print(lis)