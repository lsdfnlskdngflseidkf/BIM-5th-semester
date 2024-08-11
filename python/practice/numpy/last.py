import numpy as ujwal
first=ujwal.arange(0,5,1)
for x in ujwal.nditer(first):
    print(x)



random_array = ujwal.random.randint(0, 101, size=10)
print(random_array)
sorteda=ujwal.sort(random_array)
print(sorteda)

# Original word lists
word = ["elderberry","apple", "banana", "cherry", "date" ]
word2 = [ "honeydew","fig", "grape", "kiwi", "lemon"]
print(word)
print(word2)
# Convert lists to NumPy arrays
word_array = ujwal.array(word)
word2_array = ujwal.array(word2)

# Lexically sort the arrays using lexsort
sorted_indices_word = ujwal.lexsort([word_array])
sorted_indices_word2 = ujwal.lexsort([word2_array])


sorted_word = word_array[sorted_indices_word]
sorted_word2 = word2_array[sorted_indices_word2]

print("Sorted word:", sorted_word)
print("Sorted word2:", sorted_word2)



random_= ujwal.random.randint(0, 101, size=10)
med=ujwal.median(random_)

ranarr = ujwal.random.randint(1, 100, size=(3, 3))

