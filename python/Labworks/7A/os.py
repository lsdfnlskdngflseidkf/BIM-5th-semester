import os
curd = os.getcwd()
print(f"Current directory: {curd}")
newd = "/home/nullproj/Documents/BIM-5th-semester/python/test"
if not os.path.exists(newd):
    os.mkdir(newd)
    print(f"Directory {newd} created.")
else:
    print(f"Directory {newd} already exists.")

os.chdir(newd)
print(f"Changed to new directory: {os.getcwd()}")
print("Files in the new folder:", os.listdir())

red = "/home/nullproj/Documents/BIM-5th-semester/python/test_renamed"
os.rename(newd, red)
print(f"Directory renamed to: {red}")

os.rmdir(red)
if not os.path.exists(red):
    print("successfully deleted.")
else:
    print("Failed to delete directory")

os.chdir(curd)
print(f"Changed back to original directory: {curd}")
print("Files in the original folder:", os.listdir())
