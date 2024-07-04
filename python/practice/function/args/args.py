#using args
def packTuple(*thing):
    for a in thing:
        print(a)
packTuple("this","is","an","Example of","Packed","Arguments")
#using kwargs
def packDict(**thingy):
    for a in thingy.keys():
        print(f"{a}:{thingy[a]}")
packDict(FName="Ujwal",Lname="Parajuli")

#returning multiple arguments
def divwr(a,b):
    q=int(a/b)
    r=a%b
    return q,r
a,b=divwr(20,3)
print(f"{a} is the quotient\n{b} is the remainder")

