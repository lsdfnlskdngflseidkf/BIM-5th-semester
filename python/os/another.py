import os

cwd=os.getcwd()
fnames=os.listdir()
print("File list in the folder are ",fnames)

os.chdir(cwd)
print(f"The directory has been now changed to {cwd}")
fnames=os.listdir()
print("File list in the folder are ",fnames)