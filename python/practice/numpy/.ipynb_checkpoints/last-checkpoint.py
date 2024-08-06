import numpy as np
first=np.arange(0,5,1)
for x in np.nditer(first):
    print(x)



random_array = np.random.randint(0, 101, size=10)
print(random_array)
sorteda=np.sort(random_array)
print(sorteda)

# Original word lists
word = ["elderberry","apple", "banana", "cherry", "date" ]
word2 = [ "honeydew","fig", "grape", "kiwi", "lemon"]
print(word)
print(word2)
# Convert lists to NumPy arrays
word_array = np.array(word)
word2_array = np.array(word2)

# Lexically sort the arrays using np.lexsort
sorted_indices_word = np.lexsort([word_array])
sorted_indices_word2 = np.lexsort([word2_array])


sorted_word = word_array[sorted_indices_word]
sorted_word2 = word2_array[sorted_indices_word2]

print("Sorted word:", sorted_word)
print("Sorted word2:", sorted_word2)



random_= np.random.randint(0, 101, size=10)
med=np.median(random_)

ranarr = np.random.randint(1, 100, size=(3, 3))

