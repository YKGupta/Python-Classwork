# Nested for loops
name = ["Yash", "Dev", "Aditya"]
chocolate = ["Dairy Milk", "5 Star", "Perk"]

for n in name:
    print(n, end = ": ")
    for i in chocolate:
        print(i, end = ", ")
    print()