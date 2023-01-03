# Types of recursion
# Head Recursion
def getValue(n):
    if(n == 0):
        return
    print("Value", n)
    getValue(n-1)
getValue(3)

print("-"*41)

# Tail Recursion
def getValue(n):
    if(n == 0):
        return
    getValue(n-1)
    print("Value", n)
getValue(3)