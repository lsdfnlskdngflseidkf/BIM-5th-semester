from multipledispatch import dispatch
class testing:
    @dispatch(int,int)
    def add(first,second):
        return first+second
    @dispatch(float,float,float)
    def add(first,second,third):
        return first+second+third
    @dispatch(str,str)
    def add(firstpart,secondpart):
        return f"{firstpart} {secondpart}"
test=testing()
print(test.add(20,50))
print(test.add(65.56,34.234,34.76))
print(test.add("Hello ","World"))