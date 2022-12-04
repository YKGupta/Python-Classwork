# Write a program to display all prime numbers within a range, take start range and end range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
for i in range(start, end + 1):
    f = 0
    if(i <= 1):
        continue

    for j in range(2, i):
        if(i % j == 0):
            f = 1
            break
    if(f == 0):
        print(i, end = " ")