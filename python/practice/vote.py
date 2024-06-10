age=int(input("Enter your age:"))
# print("you can vote" if age>=18 else "you cannot vote")
value="can" if age>=18 else "cannot"
print(f"You {value} vote")