# Write a Python program to reverse a string.
s = input("Enter the string: ")
# print(s[::-1])
ans = ""
for i in s:
    ans = i + ans
print(ans)