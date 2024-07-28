import os
nd="F:/UjwalParajuli/python-class/python/test"
ndr="F:/UjwalParajuli/python-class/python/testing"
crd=os.getcwd()
print(f"{ crd} is the current directory ")
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
