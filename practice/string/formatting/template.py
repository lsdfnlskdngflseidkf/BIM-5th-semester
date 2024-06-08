from string import Template
testing=Template("Name:$name,Age:$age")
formatted_string = testing.substitute(name="Ujwal", age=19)
print(formatted_string)