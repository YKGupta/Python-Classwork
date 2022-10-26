# Printing cube of elements as specified by user
n = int(input("Enter range(1-10): "))
l = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in l[:n]:
    print(i, "cubed =", i**3)

print("\nElements from", str(n+1) + "th", "position till end:")
for i in l[n:]:
    print(i, "cubed =", i**3)