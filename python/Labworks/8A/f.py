class Parent:
    def __init__(self):
        self._protected_var = "I'm protected"
        self.__private_var = "I'm private"
    
    def display_vars(self):
        print(f"Protected variable in Parent: {self._protected_var}")
        print(f"Private variable in Parent: {self.__private_var}")

class Child(Parent):
    def access_parent_vars(self):
        print(f"protected var from Child: {self._protected_var}")
        try:
            print(f"private var from Child: {self.__private_var}")
        except AttributeError as e:
            print(f"Error : {e}")
    
    def display_vars(self):
        super().display_vars()
        print(f"protected var from Child's display_vars: {self._protected_var}")
        try:
            print(f"private var from Child's display_vars: {self.__private_var}")
        except AttributeError as e:
            print(f"Error display_vars: {e}")

# Create an instance of Child
child_instance = Child()

# Display variables from Parent class
child_instance.display_vars()

# Attempt to access protected and private variables from Child class
child_instance.access_parent_vars()
