# Write a Python function to sum all the numbers in a list.
l = []
n = int(input("Enter range: "))
for i in range(n):
    l.append(int(input("Enter the element: ")))

def sumOfElements(l):
    f = 0
    for i in l:
        f += i
    print("Sum is:", f)

sumOfElements(l)