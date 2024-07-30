fname="file.txt"
this=open(fname,'r')
print(this.read())
import os
this="/home/nullproj/Documents/BIM-5th-semester/python/practice/files/this.txt"
fil=open(this,'r')
print(fil.read())
fil.close()
fil=open(this,'a')
fil.write("\nThis is the next line that i wrote using py")
fil.close()
fil=open(this,'r')
print(fil.read())
fil.close()
