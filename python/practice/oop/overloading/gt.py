class currency:
    def __init__(self,rupee):
        self.rupee=rupee
    def __gt__(one,two):
        return True if one.rupee>two.rupee else False
money=currency(100)
moni=currency(40)
if(money>moni):
    print("Money is greater than moni")
else:
    print("Moni is greater than money")