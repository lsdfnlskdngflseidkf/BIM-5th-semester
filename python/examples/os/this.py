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

#listing the directories.
fnames=os.listdir()
print("File list in the folder are ",fnames)

os.chdir(cwd)
print(f"The directory has been now changed to {cwd}")
fnames=os.listdir()
print("File list in the folder are ",fnames)
ndr="F:/UjwalParajuli/python-class/python/testing"
print(f"{ cwd} is the current directory ")
os.rename(nd,ndr)
if(os.path.exists(ndr)):
    print(f"Rename successful . The directory is now called {ndr}")
else:
    print(f"Failed to rename the directory {nd} to {ndr}")
os.rmdir(ndr)
   
if os.path.exists(ndr):
    print(f"The directory {ndr} does not exist because it was deleted")
else:
    print(f"Failed to delet {ndr}")
fnames=os.listdir()
print("File list in the folder are ",fnames)

os.chdir(cwd)
print(f"The directory has been now changed to {cwd}")
fnames=os.listdir()
print("File list in the folder are ",fnames)
