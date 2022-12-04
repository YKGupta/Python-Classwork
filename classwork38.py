# Write a Python program to print the even numbers from a given list.
l = []
n = int(input("Enter range: "))
for i in range(n):
    l.append(int(input("Enter the element: ")))

def even(l):
    ans = []
    for i in l:
        if(i % 2 == 0):
            ans.append(i)
    return ans

print(even(l))