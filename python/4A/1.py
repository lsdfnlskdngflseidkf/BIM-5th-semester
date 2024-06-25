#this will double as thrid lab report for py
#1
set1={"Apple","Banana","Mango","Lychee"}
print(set1)
set2={"Mango","Lychee","Longan","Rambutan"}
print(set2)
#2
#blank 
#3
if "Mango" in set1:
    print("Mango is present in the first set")
#4
set1.add("plum")
print("Plum was added into the set")
print(set1)
#5
set1.remove("plum")
print(set1)

#6
newset=set1.union(set2)
print(newset)

#7
print("I'm removing mango")
newset.remove("Mango")
print(newset)
newset.clear()
print(newset)

#8
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set1.isdisjoint(set2))
print(set1.issuperset(set2))
pirint(set1.issubset(set2))