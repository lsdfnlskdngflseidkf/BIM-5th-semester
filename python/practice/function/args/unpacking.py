#unpacking tuple
def fun(a,b,c,d,e,f,t):
    print(f"{a} {b} {c} {d} {e} {f} {t}")
nums=(1,2,3,4,5,6,7)
fun(*nums)
#dictionary
def fun2(Name,Author,Genre):
    print(f"{Name}\n{Author}\n {Genre}")
book={
    'Name':"Lord of The Rings",
    'Author':"J. R.R Tolkien",
    'Genre':"High Fantasy"
}
fun2(**book)