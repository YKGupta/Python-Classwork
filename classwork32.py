# Write a Python function to find the Max of three numbers.
a, b, c = int(input("Enter first number: ")), int(input("Enter second number: ")), int(input("Enter third number: "))
if(a > b and a > c):
    print(a)
elif(b > a and b > c):
    print(b)
else:
    print(c)