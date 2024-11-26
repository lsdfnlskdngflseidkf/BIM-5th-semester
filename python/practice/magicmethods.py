class Currency:
    def __init__(self, rupee=0, paisa=0):
        self.rupee = rupee
        self.paisa = paisa
        if self.paisa >= 100:
            self.rupee += self.paisa // 100
            self.paisa = self.paisa % 100
    def __add__(self, other):
        newr= self.rupee + other.rupee
        newp= self.paisa + other.paisa
        return Currency(newr, newp)

    def __mul__(self, other):
        newr= self.rupee * other.rupee
        newp= self.paisa * other.paisa
        return Currency(newr, newp)

    def __eq__(self, other):
        return self.rupee == other.rupee and self.paisa == other.paisa

    def display(self):
        return f"{self.rupee} rupee(s) and {self.paisa} paisa"

currency1 = Currency(5, 120)
currency2 = Currency(3, 95)
print("Before Operations:")
print(f"first: {currency1.display()}")
print(f"Second: {currency2.display()}")
sum= currency1 + currency2
print("\nAfter addition:")
print(f"Result: {sum.display()}")

product= currency1 * currency2
print("\nAfter multiplication:")
print(f"Result: {product.display()}")
print(f"Are the two objects equal?")
print(currency1==currency2)
