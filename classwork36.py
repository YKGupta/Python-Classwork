# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
n = int(input("Enter a non-negative number: "))

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

print(factorial(n))