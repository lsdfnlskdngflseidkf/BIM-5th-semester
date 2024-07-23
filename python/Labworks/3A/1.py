#this will double as thrid lab report for py
#1create  two sets with 4 items each with 2 items in common
print("\ncreate  two sets with 4 items each with 2 items in common")
set1={"Apple","Banana","Mango","Lychee"}
print(set1)
set2={"Mango","Lychee","Longan","Rambutan"}
print(set2)
#2 check if mango is present in the set
print("\ncheck if mango is present in the set")
if "Mango" in set1:
    print("Mango is present in the first set")
#4 Add an item to the set
print("\nAdd an item to the set")
set1.add("plum")
print("Plum was added into the set")
print(set1)
#5 remove an item from the set
print("\nremove an item from the set")
set1.remove("plum")
print(set1)

#6 create a new set by combining the two sets
print("\ncreate a new set by combining the two sets")
newset=set1.union(set2)
print(newset)

#7 rmeove an n item from the new set and delete the set
print("\nrmeove an n item from the new set and delete the set")
print("I'm removing mango")
newset.remove("Mango")
print(newset)
newset.clear()
print(newset)

#8 print out the union,intersection,difference,symmetric difference,disjoing,subset and superset functions
print("\nprint out the union,intersection,difference,symmetric difference,disjoing,subset and superset functions")
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set1.isdisjoint(set2))
print(set1.issuperset(set2))
print(set1.issubset(set2))