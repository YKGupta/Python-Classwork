# Check if the first and last number of a list is the same.
# Expected Output - 
# A = [10, 11, 50, 58, 29, 10]
# Output - True

# B = [10000, 11, 50, 58, 29, 10]
# Output - False

l = []
n = int(input("Enter size of array: "))
for i in range(n):
    l.append(int(input("Enter element: ")))

if (l[0] == l[-1]):
    print("True")
else:
    print("False")