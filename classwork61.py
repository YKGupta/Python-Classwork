def divide(a, b):
    return a/b

try:
    print(divide(10, 10))
    print(divide(10, 0))       # We cannot divide by zero, will give ZeroDivisionError
except ZeroDivisionError:       # Handling only the ZeroDivisionError case
    print("You cannot divide a number a number by 0 :(")