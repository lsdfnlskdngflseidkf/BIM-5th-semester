class Insufficientfundexception(Exception):
    pass
class Account:
    balance=0
    def __init__(self,balance):
        Account.balance=balance
    def deposit(self,amount):
        Account.balance+=amount
    def withdraw(self,amount):
        if Account.balance<amount:
            raise Insufficientfundexception("You do not have enough funds in your account to withdraw that amount")
        else:
            Account.balance-=amount
    def getbalance(self):
        print(f"Your balance is {Account.balance}")
ac=Account(1000)
print(f"1.Deposit\n2.withdraw\n3.show\n4.exit")
while True:
    choice=int(input("Enter your choice:"))
    match choice:
        case 1:
            amt=int(input("Enter the amount to deposit:"))
            ac.deposit(amt)
        case 2:
            amt=int(input("Enter the amount to withdraw:"))
            ac.withdraw(amt)
        case 3:
            ac.getbalance()
        case 4:
            exit()
        case _:
            print("Invalid Choice")
