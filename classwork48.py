# Find the maximum element present in a list.
# First, you have to take 5 inputs from the user and store it in a list.
# The, find the maximum number present in it.

l = []
for i in range(5):
    l.append(int(input("Enter element: ")))

maxx = l[0]
for i in l:
    if (maxx < i):
        maxx = i
print("The maximum of all the elements:", maxx)