#Accept a string from user and check if a is present in the string or not and print it
print("\nAccept a string from user and check if a is present in the string or not and print it")
def checkifa(Str):
    if 'a' in Str:
        print("a is present in the string")
        return True;
    else:
        print("a is not present in the string")
        return False;
this=input("Enter a string to check if there is a in it:")
checkifa(this)