#1 Initialize two dictionaries having 4 elements each
print("Initialize two dictionaries having 4 elements each")
book={
    'Author':"F. Scott Fitzgerald",
    'Title':"The great Gatsby",
    'Genre':"Literary Fiction",
    'Publisher':"Charles Scribner's Sons"
}
book2={
    'Author':"Philip Pullman",
    'Title':"His Dark Materials",
    'Genre':"Fantasy",
    'Publisher':"Scholastic"
}
print(book)
print(book2)
#2 Print any item in the dictionary using a key of your choice
print("\nPrint any item in the dictionary using a key of your choice")
print(book['Author'])
#3 Print the keys of the distionary
print("\nPrint the keys of the distionary")
print(book.keys())
for key in book:
    print(key)
#4 print only the values of the dictionary
print("\nprint only the values of the dictionary")
for key in book:
    print(book[key])
print(book.values())
#5 print all the key value pairs of the dictionary 
print("\nprint all the key value pairs of the dictionary ")
for key in book:
    print(f"{key}:{book[key]}")
print(book)
#6 Change the value of any item using the key
print("\nChange the value of any item using the key")
book['genre']="Tragedy"
print("The genre of the book was changed from literary fiction to Tragedy")
print(book)

#7 add an item to the dictionary
print("\nadd an item to the dictionary")
book['Published']=1925
print("The published date was added ")
print(book)

#8 remove the items of the dictionary using pop and popitem
print("\nremove the items of the dictionary using pop and popitem")
book.pop('Published')
print("The published date was removed from the dictionary")
print(book)

#with popitem
book.popitem()
print("Popitem method was just called ")
print(book)

#9 empty the dictionary and delete it
print("\nempty the dictionary and delete it")
book.clear()
print("The dictionary was cleared")
print(book)

#10 Loop through the values in the dictionary and print each value
print("\nLoop through the values in the dictionary and print each value")
book={
    'Author':"F. Scott Fitzgerald",
    'Title':"The great Gatsby",
    'Genre':"Literary Fiction",
    'Publisher':"Charles Scribner's Sons"
}
for value in book.values():
    print(value)

#11 create a copy of the dictionary and print it 
print("\ncreate a copy of the dictionary and print it ")
another=book.copy()
print("this is the copy of the original dictionary")
print(another)