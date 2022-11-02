# Apending elements to a list then printing them then removing a specific element then inserting a specific
# element at a specific place and also removing elements from last and also clearing the list and deleting 
# elements.
l = []
# Appending
l.append(int(input("Enter the first element: ")))
l.append(int(input("Enter the second element: ")))
l.append(int(input("Enter the third element: ")))
l.append(int(input("Enter the fourth element: ")))

# Printing
print("\nThe list is:-")
for i in l:
    print(i, end = ' ')

# Removing last element
print("\n\nRemoving last element...")
l.pop()
print("\nThe list now is:-")
for i in l:
    print(i, end = ' ')

# Removing element at a specific index
n = int(input("\n\nEnter the index of the element you want to remove: "))
print("\nRemoving element at", n, "index...")
l.pop(n)
print("\nThe list now is:-")
for i in l:
    print(i, end = ' ')

# Inserting element at a specified index
num = int(input("\n\nEnter the number you want to insert: "))
index = int(input("Enter the index of the place you want to insert "+ str(num) + " into: "))
print("'\nInserting", num, "at", str(index) + "...")
l.insert(index, num)
print("\nThe list now is:-")
for i in l:
    print(i, end = ' ')

index = int(input("\n\nEnter the index of the element you want to delete: "))
print("\nDeleting element at", str(index) + "...")
del l[index]
print("\nThe list now is:-")
for i in l:
    print(i, end = ' ')

print("\n\nClearing the list...")
l.clear()
print("\nThe list now is:-")
for i in l:
    print(i, end = ' ')
