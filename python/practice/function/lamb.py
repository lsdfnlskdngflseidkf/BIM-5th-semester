fun=lambda this,that: this+that
print(fun(10,20))


another=lambda a,b,c: print(a+b+c)
another(1,4,7)

def name(x):
    return lambda a: a*x
this=name(5)
print(this(9))