name = "Ujwal"
age = 19
formatted_string = "Name: {}, Age: {}".format(name, age)
print(formatted_string) # this replaces the name and age with actual values
formatted_string = "Name: {0}, Age: {1}".format(name, age)
print(formatted_string) 
formatted_string = "Name: {name}, Age: {age}".format(name="Charlie", age=40)
print(formatted_string) 
