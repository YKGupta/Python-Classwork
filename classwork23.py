# Input a number and print its table using function

def printTable(n):
    for i in range(1, 11):
        print(n , "*", i, "=", n*i)

n = int(input())
printTable(n)