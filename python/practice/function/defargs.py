def divwr(a,b=2):
    q=int(a/b)
    r=a%b
    return q,r
c,d=divwr(20)
print(f"{c} is the quotient\n{d} is the remainder\n")
a,b=divwr(20,3)
print(f"{a} is the quotient\n{b} is the remainder")
