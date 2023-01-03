# Recursion
def sayHemlo(n):
    if(n == 0):
        return
    
    print("Hemlo")
    sayHemlo(n-1)

sayHemlo(5)