# with open("data.txt",'r') as f:
#     this=f.readlines()
#     for i in this:
#         print(i)
# li=['Ujwal','Anil','Saurav','Rijan','Nixan']
# with open("names.txt",'w') as lil:
#     for i in li:
#         lil.write(f"{i}\n")
# import os
# if os.path.exists('filename.txt'):
#     print("the file exists")
# else:
#     print("The file does not exist")

# c=0
# with open('names.txt','r') as names:
#     ba=names.readlines()
#     for i in ba:
#         c+=1
# print(c)

# with open('names.txt','r') as f1:
#     with open('filename.txt','a') as f2:
#         lines=f1.readlines()
#         f2.writelines(lines)

# lines = []

# print("Enter multiple lines of input (press Enter on an empty line to finish):")

# while True:
#     line = input()
#     if line == "stop":  # Stop when an empty line is entered
#         break
#     lines.append(line)

# # Join the list into a single string if needed
# multi_line_input = "\n".join(lines)
# with open("filename.txt",'a') as fie:
#     fie.write(multi_line_input)

# with open('num.txt','r') as numfile:
#     nums=numfile.readlines()
#     sum=0
#     for i in nums:
#         b=int(i)
#         sum+=b
#     print(sum)

# import os
# cwd=os.getcwd()
# print(cwd)
# os.mkdir('newd')


# with open("data.txt",'r') as f:
#     this=f.readlines()
#     this=this[::-1]
#     for i in this:
#         print(i)
that=[]
with open("data.txt",'r') as f:
    this=f.readlines()
    for i in this:
        i.replace("o","i")
        that.append(f"{i}\n")
        print(i)
# with open('o.txt','w') as sa:
#     sa.writelines(that)


