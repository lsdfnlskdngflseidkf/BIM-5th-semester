class currency:
    def __init__(self,rupee,paisa):
        self.rupee=rupee
        self.paisa=paisa
    def __add__(one,two):
        return currency(one.rupee+two.rupee,one.paisa+two.paisa)
    def show(self):
        print(f"{self.rupee} Rupees {self.paisa} paisa")
money=currency(100,6)
moni=currency(40,90)
muchmoney=money+moni
muchmoney.show()