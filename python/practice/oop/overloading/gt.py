class currency:
    def __init__(self,rupee,paisa):
        self.rupee=rupee
        if paisa>100:
            quo=paisa/100
            self.rupee+quo
            paisa=paisa%100
            self.paisa=paisa
        else:
            self.paisa=paisa

    def __gt__(one,two):
        return True if one.rupee>two.rupee else False
money=currency(100)
moni=currency(40)
if(money>moni):
    print("Money is greater than moni")
else:
    print("Moni is greater than money")