#create a list
list1=["ball","apple","car","egg"]
#print the items in the list that contain an e 
[print(e) for e in list1]
# sort a list 
list1.sort() #sort a list (method 1)
print(list1)
#create a new list with the elements that contain a in them
list2=[x for x in list1 if 'a' in x]
print(list2)