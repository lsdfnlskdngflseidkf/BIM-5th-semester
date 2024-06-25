#1
book={
    'Author':"F. Scott Fitzgerald",
    'Title':"The great Gatsby",
    'Genre':"Literary Fiction"
}
print(book)
#2
print(book['Author'])
#3
print(book.keys())
for key in book:
    print(key)
#4 
for key in book:
    print(book[key])
print(book.values())
#5
for key in book:
    print(f"{key}:{book[key]}")
print(book)
 #6
book['genre']="Tragedy"
print("The genre of the book was changed from literary fiction to Tragedy")
print(book)

#7
book['Published']=1925
print("The published date was added ")
print(book)

#8
book.pop('Published')
print("The published date was removed from the dictionary")
print(book)

#with popitem
book.popitem()
print("Popitem method was just called ")
print(book)

#9
book.clear()
print("The dictionary was cleared")
print(book)

#10
book={
    'Author':"F. Scott Fitzgerald",
    'Title':"The great Gatsby",
    'Genre':"Literary Fiction"
}
for key in book:
    print(book[key])

#11
another=book.copy()
print("this is the copy of the original dictionary")

print(another)