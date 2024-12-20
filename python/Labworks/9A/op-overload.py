class Currency:
    def __init__(self, rupee, paisa):
        self.rupee = rupee + paisa // 100
        self.paisa = paisa % 100

    def __add__(self, other):
        newr = self.rupee + other.rupee
        newp = self.paisa + other.paisa
        return Currency(newr, newp)

    def __mul__(self, other):
        newr = self.rupee * other.rupee
        newp = self.paisa * other.paisa
        return Currency(newr, newp)

    def __eq__(self, other):
        return self.rupee == other.rupee and self.paisa == other.paisa

    def display(self):
        return f"{self.rupee} rupee(s) and {self.paisa} paisa"
currency1 = Currency(5, 120)
currency2 = Currency(3, 96)
print("Before operations:")
print(f"First: {currency1.display()}")
print(f"Second: {currency2.display()}")

print("After operations:")
print(f"Sum: {(currency1 + currency2).display()}")
print(f"Product: {(currency1 * currency2).display()}")
print(f"Equality: {currency1 == currency2}")
