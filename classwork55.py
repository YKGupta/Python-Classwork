# File Handling

# Step 1- Open the file
f = open("classwork55.txt")

# Step 2- Read the file
# print(f.read())     # Reads the complete file
print(f.read(30))     # Reads the first 20 characters
print(f.readline())

# Always close the file at the end
f.close()
# :)

f = open("classwork55.txt")

# print(f.read())
print(f.read(5))
print(f.readline())