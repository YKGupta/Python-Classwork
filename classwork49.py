# Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
# Note: There will be one solution for each input and do not use the same element twice.
# Input: numbers= [10,20,10,40,50,60,70], target=50
# Output: 3, 4
l = []
n = int(input("Enter size of array: "))
for i in range(n):
    l.append(int(input("Enter the element: ")))

target = int(input("Enter the target sum: "))
for i in range(len(l)-1):
    if (l[i] + l[i+1] == target):
        print(i+1, i+2)