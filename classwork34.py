# Write a Python function to multiply all the numbers in a list
l = []
n = int(input("Enter range: "))
for i in range(n):
    l.append(int(input("Enter the element: ")))
f = 1
for i in l:
    f *= i
print("Multiplication is:", f)