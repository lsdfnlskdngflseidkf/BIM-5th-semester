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


o1=currency(100,100000)
o2=currency(80,500000000000)
print(o1)
print(o2)
if(o1>o2):
    print("o1 is greater than o2")
else:
    print("o2 is greater than o1")