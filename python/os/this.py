#display the current directory with cwd
import os
cwd=os.getcwd()
print(cwd)
#creating a new directory
nd="f:/UjwalParajuli/python-class/python/test"
os.mkdir(nd)
if(os.path.exists(nd)):
    print(f"The directory{nd} is real")
else:
    print((f"The directory {nd} does not exist"))
#changing the current directory
os.chdir(nd)
print(f"The current directory is {os.getcwd()}")


fnames=os.listdir()
print("File list in the folder are ",fnames)

os.chdir(cwd)
print(f"The directory has been now changed to {cwd}")
fnames=os.listdir()
print("File list in the folder are ",fnames)