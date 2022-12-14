# Find the maximum element present in a list.
# First, you have to take 5 inputs from the user and store it in a list.
# The, find the maximum number present in it.

a, b, c, d, e = int(input("Enter 1st Number: ")), int(input("Enter 2nd Number: ")), int(input("Enter 3rd Number: ")), int(input("Enter 4th Number: ")), int(input("Enter 5th Number: "))
l = [a, b, c, d, e]
maxx = l[0]
for i in l:
    if (maxx < i):
        maxx = i
print("The maximum of all the elements:", maxx)