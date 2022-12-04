# Write a Python function that takes a list and returns a new list with unique elements of the first list.
l = []
n = int(input("Enter range: "))
for i in range(n):
    l.append(int(input("Enter the element: ")))

def unique(l):
    ans = []
    for i in l:
        if (i not in ans):
            ans.append(i)
    return ans

print(unique(l))